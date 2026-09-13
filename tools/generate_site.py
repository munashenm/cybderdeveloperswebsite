#!/usr/bin/env python3
"""Build the full Cyber Developers static site."""
from __future__ import annotations

import hashlib
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from site_lib import ROOT, SITE, ORG_DESC, redirect_page, write_page
from generate_core import (
    SITEMAP_URLS,
    homepage,
    about_page,
    contact_page,
    industries_page,
    privacy_page,
    not_found,
)
from generate_services import build_services
from generate_solutions import build_solutions
from generate_work import build_work
from generate_knowledge import build_knowledge

TODAY = date.today().isoformat()
INDEXNOW_KEY = hashlib.sha256(b"cyber-developers-indexnow-2026").hexdigest()


def write_robots() -> None:
    (ROOT / "robots.txt").write_text(
        f"""User-agent: *
Allow: /

User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Applebot
Allow: /

Disallow: /contact/thank-you/

Sitemap: {SITE}/sitemap.xml
""",
        encoding="utf-8",
    )
    print("wrote robots.txt")


def write_sitemap() -> None:
    urls = []
    seen = set()
    for loc, prio in SITEMAP_URLS:
        if loc in seen or loc in ("/404.html", "/contact/thank-you/"):
            continue
        seen.add(loc)
        urls.append(
            f"""  <url>
    <loc>{SITE}{loc}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{prio}</priority>
  </url>"""
        )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )
    (ROOT / "sitemap.xml").write_text(xml, encoding="utf-8")
    print("wrote sitemap.xml", len(urls), "urls")


def write_llms() -> None:
    (ROOT / "llms.txt").write_text(
        f"""# Cyber Developers

> {ORG_DESC}

Primary message: Software Built Around Your Business.

Site: {SITE}/

Entity: Cyber Developers (Pty) Ltd, South Africa. Office: 357 Oak Ave, Ferndale, Randburg. Email: sales@cyberdevelopers.co.za. Phone: 087 550 1813.
Not a cybersecurity company. Custom software, business systems, web applications, mobile apps, workflow automation and integrations.

## Pages

- [Home]({SITE}/)
- [Services]({SITE}/services/)
- [Solutions]({SITE}/solutions/)
- [Our Work]({SITE}/our-work/)
- [Industries]({SITE}/industries/)
- [About]({SITE}/about/)
- [Knowledge Centre]({SITE}/knowledge-centre/)
- [Contact]({SITE}/contact/)
""",
        encoding="utf-8",
    )
    print("wrote llms.txt")


def write_htaccess() -> None:
    (ROOT / ".htaccess").write_text(
        f"""RewriteEngine On
ErrorDocument 404 /404.html

# Do not redirect /index.html to / — Apache DirectoryIndex plus that rule loops forever.
RewriteRule ^projects\\.html$ /our-work/ [R=301,L]
RewriteRule ^about\\.html$ /about/ [R=301,L]
RewriteRule ^privacy\\.html$ /privacy/ [R=301,L]

<IfModule mod_headers.c>
  Header set X-Content-Type-Options "nosniff"
  Header set Referrer-Policy "strict-origin-when-cross-origin"
  Header set X-Frame-Options "SAMEORIGIN"
  Header set Permissions-Policy "camera=(), microphone=(), geolocation=()"
</IfModule>

<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType text/css "access plus 7 days"
  ExpiresByType application/javascript "access plus 7 days"
  ExpiresByType image/webp "access plus 30 days"
  ExpiresByType image/avif "access plus 30 days"
  ExpiresByType image/png "access plus 30 days"
  ExpiresByType image/svg+xml "access plus 30 days"
</IfModule>
""",
        encoding="utf-8",
    )
    print("wrote .htaccess")


def write_indexnow() -> None:
    (ROOT / f"{INDEXNOW_KEY}.txt").write_text(INDEXNOW_KEY, encoding="utf-8")
    (ROOT / "indexnow-key.txt").write_text(INDEXNOW_KEY + "\n", encoding="utf-8")
    print("wrote IndexNow key")


def write_redirects() -> None:
    write_page("projects.html", redirect_page("/our-work/", "Projects moved"))
    write_page("about.html", redirect_page("/about/", "About moved"))
    write_page("privacy.html", redirect_page("/privacy/", "Privacy moved"))


def main() -> None:
    homepage()
    about_page()
    contact_page()
    industries_page()
    privacy_page()
    not_found()
    build_services()
    build_solutions()
    build_work()
    build_knowledge()
    write_robots()
    write_sitemap()
    write_llms()
    write_htaccess()
    write_indexnow()
    write_redirects()
    print("done")


if __name__ == "__main__":
    main()
