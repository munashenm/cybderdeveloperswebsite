#!/usr/bin/env python3
"""Generate brand assets (header logo + favicon/app-icon set) from the source logo.

This is a one-off tool run manually whenever the logo changes. It requires
Pillow (``pip install Pillow``) and is intentionally NOT part of
``generate_site.py`` so the main site build stays dependency-free. Commit the
generated files it writes.

    python3 tools/generate_brand.py
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "assets" / "img" / "brand" / "logo-source.png"
IMG_DIR = ROOT / "assets" / "img"

WHITE = (255, 255, 255)


def keyed_rgba(img: Image.Image) -> Image.Image:
    """Turn a purple/dark-on-white logo into an RGBA image with white keyed out.

    Uses a luminance ramp so anti-aliased edges stay smooth instead of hard.
    """
    rgb = img.convert("RGB")
    lum = rgb.convert("L")
    # Fully transparent above 250, fully opaque below 228, linear ramp between.
    hi, lo = 250, 228
    alpha = lum.point(
        lambda x: 0 if x >= hi else (255 if x <= lo else int((hi - x) / (hi - lo) * 255))
    )
    out = rgb.convert("RGBA")
    out.putalpha(alpha)
    return out


def trim(img: Image.Image) -> Image.Image:
    bbox = img.getchannel("A").getbbox()
    return img.crop(bbox) if bbox else img


def isolate_mark(logo: Image.Image) -> Image.Image:
    """Crop the leading "Cy" letters of the wordmark's top line for the icon mark."""
    w, h = logo.size
    px = logo.getchannel("A").load()
    band_bottom = int(h * 0.5)  # scan within the upper "Cyber" line only

    def col_ink(x: int, y0: int, y1: int) -> int:
        return sum(1 for y in range(y0, y1) if px[x, y] > 40)

    # Horizontal: keep the first letter block, stop at the first real gap.
    gap_needed = max(6, int(w * 0.012))
    x = 0
    while x < w and col_ink(x, 0, band_bottom) == 0:
        x += 1
    start = x
    end = w
    empty = 0
    while x < w:
        if col_ink(x, 0, band_bottom) > 0:
            empty = 0
        else:
            empty += 1
            if empty >= gap_needed:
                end = x - empty + 1
                break
        x += 1

    # Vertical: cut at the valley between the top line and the line below it.
    def row_ink(y: int) -> int:
        return sum(1 for x in range(start, end) if px[x, y] > 40)

    lo, hi = int(h * 0.5), int(h * 0.82)
    cut = min(range(lo, hi), key=row_ink, default=h)

    return trim(logo.crop((start, 0, end, cut)))


def square(img: Image.Image, size: int, pad_ratio: float = 0.16, bg=None) -> Image.Image:
    """Fit img (preserving aspect) onto a size×size canvas with padding."""
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0) if bg is None else bg)
    inner = int(size * (1 - 2 * pad_ratio))
    w, h = img.size
    scale = min(inner / w, inner / h)
    nw, nh = max(1, round(w * scale)), max(1, round(h * scale))
    resized = img.resize((nw, nh), Image.LANCZOS)
    canvas.alpha_composite(resized, ((size - nw) // 2, (size - nh) // 2))
    if bg is not None:
        return canvas.convert("RGB")
    return canvas


def scaled_to_height(img: Image.Image, height: int) -> Image.Image:
    w, h = img.size
    nw = round(w * (height / h))
    return img.resize((nw, height), Image.LANCZOS)


def make_light(logo: Image.Image, dot=(124, 77, 255)) -> Image.Image:
    """Recolor for dark surfaces: white wordmark, brand-violet trailing dot.

    The source wordmark is a single violet on white; on a dark header the thin
    'Developers' strokes and the dark navy dot lose contrast. Here the violet
    ink becomes white and the dark dot becomes a bright violet accent.
    """
    out = logo.convert("RGBA")
    px = out.load()
    w, h = out.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a == 0:
                continue
            # The dark navy dot is dim (low max channel); the violet wordmark
            # is bright (blue channel ~240). Split on value, not luminance.
            if max(r, g, b) < 110:  # dark navy dot
                px[x, y] = (dot[0], dot[1], dot[2], a)
            else:  # violet wordmark
                px[x, y] = (255, 255, 255, a)
    return out


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"Source logo not found: {SRC}")
    source = Image.open(SRC)
    logo = trim(keyed_rgba(source))

    # 1) Colored wordmark (transparent) for light contexts + schema logo.
    wordmark = scaled_to_height(logo, 120)
    wordmark.save(IMG_DIR / "logo.png", optimize=True)
    print("wrote assets/img/logo.png", wordmark.size)

    # 1b) Light wordmark for dark surfaces (header/footer).
    light = scaled_to_height(make_light(logo), 120)
    light.save(IMG_DIR / "logo-light.png", optimize=True)
    print("wrote assets/img/logo-light.png", light.size)

    # 2) Favicon mark from the leading letters of the wordmark.
    mark = isolate_mark(logo)

    # favicon.png (transparent, crisp small mark)
    square(mark, 64).save(ROOT / "favicon.png", optimize=True)
    print("wrote favicon.png (64)")

    # Multi-size .ico for legacy/browser tab crispness.
    ico = square(mark, 256)
    ico.save(
        ROOT / "favicon.ico",
        sizes=[(16, 16), (32, 32), (48, 48), (64, 64)],
    )
    print("wrote favicon.ico")

    # Apple touch icon (no transparency on iOS): purple mark on white.
    square(mark, 180, pad_ratio=0.18, bg=(255, 255, 255, 255)).save(
        IMG_DIR / "apple-touch-icon.png", optimize=True
    )
    print("wrote assets/img/apple-touch-icon.png")

    # PWA/manifest icons on white for predictable rendering.
    for s in (192, 512):
        square(mark, s, pad_ratio=0.18, bg=(255, 255, 255, 255)).save(
            IMG_DIR / f"icon-{s}.png", optimize=True
        )
        print(f"wrote assets/img/icon-{s}.png")

    print("done")


if __name__ == "__main__":
    main()
