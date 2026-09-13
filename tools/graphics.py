#!/usr/bin/env python3
"""Custom technical graphics. Schematics of real systems — not fake screenshots."""
from __future__ import annotations

from site_lib import ROOT, esc

BANNER_TECH = [
    "React",
    "Next.js",
    "TypeScript",
    "JavaScript",
    "Node.js",
    "Python",
    "C#",
    ".NET",
    "PostgreSQL",
    "Prisma",
    "Firebase",
    "Azure",
    "Railway",
    "Cloudflare",
    "GitHub",
]

SHOT_DIR = ROOT / "assets" / "img" / "work"
SHOT_EXTS = (".webp", ".avif", ".png", ".jpg", ".jpeg")
PROJECT_IMG = "/assets/img/projects"

# Real product screenshots. Dimensions match the WebP files on disk.
SHOTS: dict[str, dict] = {
    "smartcity-home": {
        "file": "smartcity/home.webp", "w": 1600, "h": 757,
        "alt": "SmartCity municipal citizen services platform",
        "title": "SmartCity Muni",
    },
    "smartcity-services": {
        "file": "smartcity/services.webp", "w": 1600, "h": 746,
        "alt": "SmartCity municipal services grid including reporting, alerts and bookings",
        "title": "SmartCity Muni",
    },
    "smartcity-report": {
        "file": "smartcity/report-issue.webp", "w": 1600, "h": 741,
        "alt": "SmartCity municipal fault reporting form for water leaks and service issues",
        "title": "SmartCity Muni",
    },
    "smartcity-emergency": {
        "file": "smartcity/emergency.webp", "w": 1600, "h": 746,
        "alt": "SmartCity emergency contacts for SAPS, ambulance, fire and disaster management",
        "title": "SmartCity Muni",
    },
    "tshira-dashboard": {
        "file": "tshira-workflow/dashboard.webp", "w": 1600, "h": 731,
        "alt": "Cyber Developers Tshira workflow management dashboard",
        "title": "Tshira",
    },
    "tshira-reports": {
        "file": "tshira-workflow/reports.webp", "w": 1600, "h": 728,
        "alt": "Tshira management reports with SLA, cases and finance metrics",
        "title": "Tshira",
    },
    "legacy-dashboard": {
        "file": "legacy-care/dashboard.webp", "w": 1600, "h": 739,
        "alt": "Legacy Care funeral management software dashboard",
        "title": "Legacy Care",
    },
    "legacy-collections": {
        "file": "legacy-care/collections.webp", "w": 1600, "h": 737,
        "alt": "Legacy Care premium collection trends and recent collections",
        "title": "Legacy Care",
    },
    "lawtech-dashboard": {
        "file": "lawtech/dashboard.webp", "w": 1600, "h": 723,
        "alt": "LawTech SA legal practice management dashboard",
        "title": "LawTech SA",
    },
    "vayasa-home": {
        "file": "vayasa/home.webp", "w": 1600, "h": 738,
        "alt": "VayaSA South African passenger transport marketplace",
        "title": "VayaSA",
    },
    "vayasa-search": {
        "file": "vayasa/search.webp", "w": 1466, "h": 878,
        "alt": "VayaSA ride sharing search results between South African cities",
        "title": "VayaSA",
    },
    "vayasa-routes": {
        "file": "vayasa/routes.webp", "w": 1496, "h": 824,
        "alt": "VayaSA operator onboarding and popular intercity routes",
        "title": "VayaSA",
    },
    "fluxmove-hero": {
        "file": "fluxmove/hero.webp", "w": 1600, "h": 727,
        "alt": "FluxMove logistics marketplace homepage",
        "title": "FluxMove",
    },
    "fluxmove-quote": {
        "file": "fluxmove/quote.webp", "w": 1270, "h": 877,
        "alt": "FluxMove logistics instant quotation platform",
        "title": "FluxMove",
    },
    "fluxmove-vehicles": {
        "file": "fluxmove/vehicles.webp", "w": 1600, "h": 731,
        "alt": "FluxMove vehicle types from motorcycle to heavy equipment transport",
        "title": "FluxMove",
    },
    "school-portal": {
        "file": "school-management/portal.webp", "w": 1600, "h": 728,
        "alt": "Smart School College management platform",
        "title": "Smart School/College",
    },
}


def _cls(*parts: str) -> str:
    return " ".join(p for p in parts if p)


def frame(title: str, inner: str, cls: str = "") -> str:
    return f"""<div class="{_cls("frame", cls)}">
  <div class="frame-chrome"><i></i><i></i><i></i><span>{esc(title)}</span></div>
  <div class="frame-body">{inner}</div>
</div>"""


def phone_frame(title: str, inner: str) -> str:
    return f"""<div class="frame frame-phone">
  <div class="frame-chrome"><span class="notch"></span><span>{esc(title)}</span></div>
  <div class="frame-body">{inner}</div>
  <span class="home-bar" aria-hidden="true"></span>
</div>"""


def app_shell(
    title: str,
    nav: list[str],
    panels: list[str],
    flow: list[str] | None = None,
    active: int = 0,
    cls: str = "",
) -> str:
    nav_items = []
    for i, n in enumerate(nav):
        on = ' class="is-on"' if i == active else ""
        nav_items.append(f"<li{on}>{esc(n)}</li>")
    nav_html = "".join(nav_items)
    panel_html = "".join(
        f'<div class="shell-panel"><strong>{esc(p)}</strong><span></span><span></span></div>'
        for p in panels
    )
    flow_html = ""
    if flow:
        flow_html = (
            '<ol class="shell-flow">'
            + "".join(f"<li>{esc(s)}</li>" for s in flow)
            + "</ol>"
        )
    inner = f"""<div class="shell">
  <ul class="shell-nav">{nav_html}</ul>
  <div class="shell-work">
    <div class="shell-panels">{panel_html}</div>
    {flow_html}
  </div>
</div>"""
    return frame(title, inner, cls)


def shot(key: str, *, eager: bool = False, title: str | None = None) -> str:
    """Browser-framed product screenshot. Never stretched; height follows the image."""
    meta = SHOTS[key]
    src = f"{PROJECT_IMG}/{meta['file']}"
    sm = src.replace(".webp", "-sm.webp")
    w, h = meta["w"], meta["h"]
    alt = meta["alt"]
    chrome = title if title is not None else meta["title"]
    loading = "eager" if eager else "lazy"
    fetch = ' fetchpriority="high"' if eager else ""
    sizes = "(max-width: 760px) 100vw, (max-width: 1240px) 56vw, 760px"
    return f"""<div class="frame shot-frame">
  <div class="frame-chrome"><i></i><i></i><i></i><span>{esc(chrome)}</span></div>
  <div class="frame-shot">
    <img src="{src}" srcset="{sm} 900w, {src} {w}w" sizes="{sizes}"
         alt="{esc(alt)}" width="{w}" height="{h}"
         loading="{loading}" decoding="async"{fetch}>
  </div>
</div>"""


def shot_stack(*keys: str, eager_first: bool = False) -> str:
    parts = [
        shot(k, eager=(eager_first and i == 0))
        for i, k in enumerate(keys)
    ]
    return f'<div class="shot-stack">{"".join(parts)}</div>'


def shot_gallery(keys: list[str], eager_first: bool = False) -> str:
    items = []
    for i, k in enumerate(keys):
        items.append(f'<figure class="shot-item">{shot(k, eager=(eager_first and i == 0))}</figure>')
    return f'<div class="shot-gallery">{"".join(items)}</div>'


def work_visual(slug: str, alt: str, fallback: str) -> str:
    """Legacy hook for drop-in files under assets/img/work/{slug}."""
    if SHOT_DIR.is_dir():
        for ext in SHOT_EXTS:
            if (SHOT_DIR / f"{slug}{ext}").is_file():
                src = f"/assets/img/work/{slug}{ext}"
                return (
                    f'<div class="frame shot-frame">'
                    f'<div class="frame-chrome"><i></i><i></i><i></i><span>{esc(alt)}</span></div>'
                    f'<div class="frame-shot">'
                    f'<img src="{src}" alt="{esc(alt)}" width="1440" height="900" '
                    f'loading="lazy" decoding="async">'
                    f"</div></div>"
                )
    return fallback


def vayasa_map() -> str:
    return shot("vayasa-home")


def fluxmove_map() -> str:
    return shot("fluxmove-quote")


def tshira_map() -> str:
    return shot("tshira-dashboard")


def school_map() -> str:
    return shot("school-portal")


def lawyer_map() -> str:
    return shot("lawtech-dashboard")


def funeral_map() -> str:
    return shot("legacy-dashboard")


def municipality_map() -> str:
    return shot("smartcity-home")


def hero_stage() -> str:
    return f"""<div class="hero-stage hero-shot">
  {shot("vayasa-home", eager=True, title="VayaSA")}
</div>
<p class="hero-visual-note">VayaSA — a passenger transport marketplace we designed and built. Operational systems such as Tshira are in Selected Work.</p>"""


def _tech_svg(name: str) -> str:
    """Simple monochrome identification marks. Not decorative cards."""
    icons = {
        "React": '<ellipse cx="12" cy="12" rx="10" ry="4"/><ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(60 12 12)"/><ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(-60 12 12)"/><circle cx="12" cy="12" r="1.5" fill="currentColor" stroke="none"/>',
        "Next.js": '<circle cx="12" cy="12" r="9.2"/><path d="M8.2 7.5h2.1L16 16.5h-2.2l-3.5-5.2V16.5H8.2z" fill="currentColor" stroke="none"/>',
        "TypeScript": '<rect x="3.5" y="3.5" width="17" height="17" rx="2"/><path d="M8 13.2V11h8v2.2h-2.7V19h-2.6v-5.8z" fill="currentColor" stroke="none"/>',
        "JavaScript": '<rect x="3.5" y="3.5" width="17" height="17" rx="2"/><path d="M10 9v7.2c0 1.6-.8 2.3-2.2 2.3-.7 0-1.4-.2-1.8-.5l.7-1.7c.2.2.5.3.8.3.4 0 .6-.2.6-.8V9zm3.2 4.8c.3-.5.8-.8 1.5-.8.6 0 1 .2 1 .6 0 .5-.4.6-1.1.8l-.4.1c-1.3.4-2 1.1-2 2.2 0 1.3 1 2.2 2.6 2.2 1.1 0 1.9-.3 2.5-.9l-1-1.3c-.4.4-.9.6-1.5.6-.5 0-.8-.2-.8-.5 0-.4.3-.5 1.1-.8l.4-.1c1.4-.4 2.1-1.1 2.1-2.3 0-1.4-1.1-2.3-2.8-2.3-1.2 0-2.2.4-2.8 1.2z" fill="currentColor" stroke="none"/>',
        "Node.js": '<path d="M12 3.2 19.2 7.4v9.2L12 20.8 4.8 16.6V7.4z"/>',
        "Python": '<path d="M12.2 4c2.4 0 3.3.8 3.3 2.6V8.4H9.6c-1.9 0-3.4 1.2-3.4 3.4 0 1.5.8 2.5 2.2 2.9.6.2 1.3.2 2 .2h1.4V13h3.8v4.4c0 1.9-1.1 3-3.5 3.2-2.1.2-3.5-.5-3.8-2.2H6.2c.4 2.7 2.4 4.2 6 4.2 3.6 0 6-1.6 6-4.6v-6.4H12.4c-1.7 0-2.4-.6-2.4-1.8 0-1.1.7-1.8 2.2-1.8z"/>',
        "C#": '<text x="12" y="16" text-anchor="middle" font-size="9" font-family="IBM Plex Mono,monospace" fill="currentColor" stroke="none">C#</text><rect x="3.5" y="3.5" width="17" height="17" rx="2"/>',
        ".NET": '<text x="12" y="16" text-anchor="middle" font-size="7" font-family="IBM Plex Mono,monospace" fill="currentColor" stroke="none">.NET</text><rect x="3.5" y="3.5" width="17" height="17" rx="2"/>',
        "PostgreSQL": '<ellipse cx="12" cy="8" rx="5.5" ry="4.2"/><path d="M8 10c0 6 1.2 10 4 10s4-4 4-10"/><path d="M9 18.5c1.2.8 2.2 1.2 3 1.2"/>',
        "Prisma": '<path d="M7 17.5 12 3.8 17.4 16.2c.3.8-.2 1.6-1 1.8L8.2 20.4c-.9.2-1.6-.6-1.2-1.5z"/>',
        "Firebase": '<path d="M6.8 16.8 9.2 4.8l4 6.4zm0 0 10.4 2.2L13.2 11 9.2 16.2zm10.4 2.2L14.6 5.4 13.2 11z"/>',
        "Azure": '<path d="M10.2 4.5h5.2L8.5 19.5H3.2zm1.4 5.2 5.8 10H20.8L13.4 4.8z"/>',
        "Railway": '<path d="M6 16.5h12M8 16.5l1.2-9h5.6l1.2 9M10 7.5V4.8h4V7.5M7.5 19h9"/>',
        "Cloudflare": '<path d="M6.5 15.2h11.2c1.3 0 2.3-1 2.3-2.2 0-1.1-.8-2-1.9-2.2.1-2.2-1.7-4-3.9-4-1.6 0-3 .9-3.6 2.2-2.2.2-3.9 2-3.9 4.2 0 1.1.4 1.8.8 2z"/>',
        "GitHub": '<path d="M12 3.5c-4.6 0-8.3 3.7-8.3 8.3 0 3.7 2.4 6.8 5.7 7.9.4.1.6-.2.6-.4v-1.5c-2.3.5-2.8-1.1-2.8-1.1-.4-.9-.9-1.1-.9-1.1-.7-.5.1-.5.1-.5.8.1 1.2.8 1.2.8.7 1.2 1.9.9 2.3.7.1-.5.3-.9.5-1.1-1.8-.2-3.7-.9-3.7-4 0-.9.3-1.6.8-2.2-.1-.2-.4-1.1.1-2.2 0 0 .7-.2 2.3.8a8 8 0 0 1 4.2 0c1.6-1 2.3-.8 2.3-.8.5 1.1.2 2 .1 2.2.5.6.8 1.3.8 2.2 0 3.1-1.9 3.8-3.7 4 .3.3.6.8.6 1.6v2.3c0 .2.2.5.6.4 3.3-1.1 5.7-4.2 5.7-7.9 0-4.6-3.7-8.3-8.3-8.3z"/>',
    }
    inner = icons.get(name, '<circle cx="12" cy="12" r="7"/>')
    return (
        f'<svg class="tech-svg" viewBox="0 0 24 24" aria-hidden="true" '
        f'fill="none" stroke="currentColor" stroke-width="1.4" '
        f'stroke-linejoin="round">{inner}</svg>'
    )


def tech_banner() -> str:
    marks = "".join(
        f"<li>{_tech_svg(t)}<span>{esc(t)}</span></li>" for t in BANNER_TECH
    )
    row = f'<ul class="tech-track">{marks}</ul>'
    dup = f'<ul class="tech-track" aria-hidden="true">{marks}</ul>'
    return f"""<section class="tech-banner" aria-label="Technology we work with">
  <div class="container tech-banner-head">
    <h2>Technology We Work With</h2>
    <p>We choose technologies based on the requirements, scale and long-term needs of each system. The list is limited to tools used on Cyber Developers systems.</p>
  </div>
  <div class="tech-marquee">
    <div class="tech-marquee-inner">
      {row}
      {dup}
    </div>
  </div>
</section>"""


def tags(items: list[str]) -> str:
    return '<ul class="tag-row">' + "".join(f"<li>{esc(t)}</li>" for t in items) + "</ul>"


def showcase(
    href: str,
    name: str,
    kicker: str,
    copy: str,
    tag_list: list[str],
    visual: str,
    reverse: bool = False,
    cta: str = "View Case Study",
) -> str:
    cls = _cls("showcase", "reverse" if reverse else "", "reveal")
    return f"""<a class="{cls}" href="{href}">
  <div class="showcase-visual">{visual}</div>
  <div class="showcase-copy">
    <p class="eyebrow">{esc(kicker)}</p>
    <h3>{esc(name)}</h3>
    <p>{esc(copy)}</p>
    {tags(tag_list)}
    <span class="more">{esc(cta)}</span>
  </div>
</a>"""


def selected_work() -> str:
    return f"""<section class="section" id="work">
  <div class="container">
    <div class="section-intro reveal">
      <p class="eyebrow">Selected Work</p>
      <h2>Software built for real-world operations.</h2>
      <p class="lead">These are systems we designed and developed. They are not stock illustrations or invented dashboards.</p>
    </div>
    {showcase("/our-work/tshira-workflow-system/", "Enterprise Workflow Platform", "Tshira",
              "Case management, SLA monitoring, finance and operational reporting.",
              ["Workflow", "Cases", "SLA", "Finance", "Audit"],
              tshira_map(), cta="View project")}
    {showcase("/our-work/municipality-platform/", "Municipal Digital Services Platform", "SmartCity Muni",
              "Citizen reporting, alerts, municipal services and emergency access.",
              ["Citizen portal", "Fault reporting", "Alerts", "Emergency"],
              municipality_map(), reverse=True, cta="View project")}
    {showcase("/our-work/vayasa/", "Passenger Transport Marketplace", "VayaSA",
              "Ride sharing, bus ticketing and taxi booking.",
              ["Ride sharing", "Bus tickets", "Taxi bookings"],
              vayasa_map(), cta="View project")}
    {showcase("/our-work/fluxmove/", "Logistics Marketplace", "FluxMove",
              "Instant quotations, delivery booking and transport-provider workflows.",
              ["Live quotes", "Vehicle types", "Booking"],
              fluxmove_map(), reverse=True, cta="View project")}
    <p class="hero-actions reveal" style="margin-top:2.2rem">
      <a class="btn btn-primary" href="/our-work/">Explore Our Work</a>
    </p>
  </div>
</section>"""


def more_work() -> str:
    items = [
        ("/our-work/school-lms/", "School / College LMS", "Academics, fees, HR, parent portal and backups.", school_map()),
        ("/our-work/lawyer-management-system/", "Lawyer Management", "Clients, matters, documents, billing and RAF where it applies.", lawyer_map()),
        ("/our-work/funeral-parlour-system/", "Funeral Parlour System", "Custom administration. Feature detail confirmed in a demo.", funeral_map()),
        ("/our-work/municipality-platform/", "Municipality Platform", "Residents, billing, faults, queues and notices.", municipality_map()),
    ]
    cards = []
    for href, name, copy, vis in items:
        cards.append(
            f'<a class="mini-show reveal" href="{href}">{vis}<h3>{esc(name)}</h3><p>{esc(copy)}</p><span class="more">View Case Study</span></a>'
        )
    return f"""<section class="section section-alt" id="more-work">
  <div class="container">
    <div class="section-intro reveal">
      <h2>Further systems</h2>
      <p class="lead">The same engineering approach, applied to education, legal practice, funeral operations and local government.</p>
    </div>
    <div class="mini-show-grid">{''.join(cards)}</div>
  </div>
</section>"""


def architecture() -> str:
    return """<section class="section" id="architecture">
  <div class="container arch-layout">
    <div class="reveal">
      <h2>Built Beyond the Interface</h2>
      <p class="lead">A reliable system requires more than a good-looking screen. We design the application structure, data, integrations, permissions, deployment and support around how the organisation needs to operate.</p>
      <ul class="arch-labels">
        <li>Frontend</li><li>Backend</li><li>API</li><li>Database</li>
        <li>Authentication</li><li>Payments</li><li>Notifications</li><li>Cloud</li>
      </ul>
    </div>
    <div class="arch-graphic reveal" role="img" aria-label="Users connect to a web or mobile application, then an API layer, database, integrations and cloud infrastructure.">
      <div class="arch-board">
        <div class="arch-layer">Users · staff · customers · field</div>
        <span class="arch-join" aria-hidden="true"></span>
        <div class="arch-layer is-app">Web / Mobile Application</div>
        <span class="arch-join" aria-hidden="true"></span>
        <div class="arch-layer">Application / API Layer</div>
        <span class="arch-join" aria-hidden="true"></span>
        <div class="arch-trio">
          <div><strong>Database</strong><span>Records · status · history</span></div>
          <div><strong>Integrations</strong><span>Payments · SMS · identity</span></div>
          <div><strong>Cloud</strong><span>Hosting · backups · auth</span></div>
        </div>
        <span class="arch-join" aria-hidden="true"></span>
        <div class="arch-layer">Permissions &amp; support</div>
      </div>
    </div>
  </div>
</section>"""


def pipeline(steps: list[str]) -> str:
    lis = "".join(f"<li>{esc(s)}</li>" for s in steps)
    return f'<ol class="pipeline">{lis}</ol>'


def hub_diagram(center: str, spokes: list[str]) -> str:
    items = "".join(f"<li>{esc(s)}</li>" for s in spokes)
    return f"""<div class="hub">
  <p class="hub-core">{esc(center)}</p>
  <ul>{items}</ul>
</div>"""


def capability_visual(kind: str) -> str:
    if kind == "custom":
        return app_shell(
            "Application model",
            ["Roles", "Records", "Exceptions", "Reports"],
            ["Entities", "Statuses", "Permissions"],
            ["Capture", "Decide", "Record"],
        )
    if kind == "business":
        return app_shell(
            "Operational system",
            ["People", "Money", "Cases", "Audit"],
            ["Day-to-day work", "Exceptions", "Reports"],
            ["Open", "Operate", "Close"],
        )
    if kind == "web":
        return app_shell(
            "Web application",
            ["Staff", "Customer", "Documents", "Queues"],
            ["Portal", "Permissions", "Shared data"],
        )
    if kind == "mobile":
        return phone_frame(
            "Field client",
            '<ul class="phone-mods"><li>Jobs</li><li>Status</li><li>Capture</li><li>Sync</li></ul>'
            '<p class="frame-caption">Same rules as the desktop system.</p>',
        )
    if kind == "workflow":
        return frame("Named stages", pipeline(["Capture", "Assign", "Review", "Invoice", "Close"]))
    if kind == "ai":
        return frame(
            "Inside the application",
            pipeline(["Document", "Extract", "Record", "Human check"]),
        )
    return frame(
        "Connected services",
        hub_diagram("API", ["Paystack / Ozow", "SMS / Email", "SA ID", "Existing SQL"]),
    )


def capabilities_editorial(
    heading: str | None = "What We Build",
    lead: str | None = "Manage customers, documents, approvals, payments and reporting from one system — or connect the systems you already have.",
    section_id: str = "services",
) -> str:
    rows = [
        ("custom", False, "Custom software", "/services/custom-software-development/",
         "Applications modelled on your roles, records and exceptions — not a template forced onto the business."),
        ("business", True, "Business systems", "/services/business-systems/",
         "Day-to-day administration: people, money, cases and reports in one place staff can actually operate."),
        ("web", False, "Web applications", "/services/web-application-development/",
         "Portals for staff, customers, parents, citizens or partners, with permissions on the same data."),
        ("mobile", True, "Mobile apps", "/services/mobile-app-development/",
         "Field work, drivers and anyone who is not at a desk — as a client of the same business rules."),
        ("workflow", False, "Workflow automation", "/services/workflow-automation/",
         "Named stages, owners and finance rules instead of email chains and inbox handovers."),
        ("ai", True, "AI & automation", "/services/ai-business-automation/",
         "Assistants, documents and reporting inside a real application. A model is a component, not the product."),
        ("integration", False, "Systems integration", "/services/systems-integration/",
         "Payments, SMS, identity and existing databases, wired in so information is not retyped."),
    ]
    blocks = []
    for kind, rev, title, href, copy in rows:
        cls = _cls("cap-row", "reverse" if rev else "", "reveal")
        blocks.append(
            f"""<article class="{cls}">
  <div class="cap-copy">
    <h3>{esc(title)}</h3>
    <p>{esc(copy)}</p>
    <a class="more" href="{href}">Details</a>
  </div>
  <div class="cap-visual">{capability_visual(kind)}</div>
</article>"""
        )
    intro = ""
    if heading:
        intro = f"""<div class="section-intro reveal">
      <h2>{esc(heading)}</h2>
      <p class="lead">{esc(lead or "")}</p>
    </div>
    """
    return f"""<section class="section section-alt" id="{esc(section_id)}">
  <div class="container">
    {intro}{''.join(blocks)}
  </div>
</section>"""


def engineering_matrix() -> str:
    items = [
        ("Application architecture", "Roles, screens and a data model that can survive real exceptions."),
        ("Database design", "Entities, statuses and history that reports can be trusted against."),
        ("API development", "Server-side rules, signed callbacks and failure handling."),
        ("Authentication & permissions", "The finance user is not the field user."),
        ("Payments integration", "Paystack, Ozow, Capitec Pay and related processors where a product required them."),
        ("Cloud deployment", "Hosting, backups and accounts people can actually use."),
        ("Third-party integrations", "SMS, email, identity checks and existing SQL databases."),
        ("Reporting & analytics", "The numbers come from the same records the operators use."),
        ("Workflow automation", "Named stages, owners and finance locks."),
        ("Mobile experiences", "Thin clients of the same backend, not a second source of truth."),
    ]
    lis = "".join(f"<li><h3>{esc(t)}</h3><p>{esc(d)}</p></li>" for t, d in items)
    return f"""<section class="section section-alt" id="capabilities">
  <div class="container">
    <div class="section-intro reveal">
      <h2>Engineering Capabilities</h2>
      <p class="lead">Complete systems, not a brochure website with a contact form.</p>
    </div>
    <ul class="matrix reveal">{lis}</ul>
  </div>
</section>"""


def industries_band() -> str:
    items = [
        ("Government", "/industries/#government"),
        ("Education", "/industries/#education"),
        ("Legal", "/industries/#legal"),
        ("Funeral", "/industries/#funeral"),
        ("Transport", "/industries/#transport"),
        ("Logistics", "/industries/#logistics"),
        ("Enterprise", "/industries/#enterprise"),
    ]
    links = "".join(f'<a href="{h}">{esc(n)}</a>' for n, h in items)
    return f"""<section class="section" id="industries">
  <div class="container">
    <div class="section-intro reveal">
      <h2>Software for organisations with real operational complexity</h2>
      <p class="lead">We build systems for schools, law firms, logistics companies, municipalities and other organisations with specialised workflows.</p>
    </div>
    <nav class="industry-band reveal" aria-label="Industries">{links}</nav>
    <p class="muted" style="margin-top:1.2rem"><a href="/industries/">Industries</a> · <a href="/solutions/">Solutions</a></p>
  </div>
</section>"""


def process_flow() -> str:
    steps = [
        ("Discovery", "Who the users are, which records matter, which approvals exist."),
        ("Architecture", "A data model and permissions that can survive the work."),
        ("UI/UX", "Screens that match the jobs, not a generic admin theme."),
        ("Development", "Build against the process, with operators looking at it early."),
        ("Testing", "Failed payments, missing documents, permission edges."),
        ("Deployment", "Hosting, backups and accounts people can use."),
        ("Support", "Fixes and change requests after the first week of real use."),
    ]
    lis = "".join(f"<li><h3>{esc(t)}</h3><p>{esc(d)}</p></li>" for t, d in steps)
    return f"""<section class="section section-alt" id="process">
  <div class="container">
    <div class="section-intro reveal">
      <h2>How a project usually runs</h2>
      <p class="lead">Ordinary engineering, written down so nobody is surprised at go-live.</p>
    </div>
    <ol class="lifecycle reveal">{lis}</ol>
  </div>
</section>"""


def ops_flow(steps: list[str] | None = None) -> str:
    items = steps or ["Users", "Operations", "Workflow", "Payments", "Reporting", "Integrations"]
    lis = "".join(f"<li>{esc(s)}</li>" for s in items)
    return f'<ol class="ops-flow" aria-label="How a business system typically connects">{lis}</ol>'


def crm_map() -> str:
    return app_shell(
        "Custom CRM",
        ["Records", "Pipeline", "Jobs", "Billing"],
        ["Customers", "Stages", "History", "Reports"],
        ["Enquire", "Work", "Invoice", "Close"],
    )


def retail_map() -> str:
    return frame(
        "Retail operations",
        pipeline(["Stock", "Sale", "Customer", "Invoice", "Reorder"]),
    )


def professional_map() -> str:
    return app_shell(
        "Professional services",
        ["Clients", "Engagements", "Documents", "Billing"],
        ["Work", "Reviews", "Invoices", "Reports"],
        ["Brief", "Deliver", "Review", "Bill"],
    )


def feature_block(
    href: str,
    name: str,
    kicker: str,
    copy: str,
    modules: list[str],
    visual: str,
    cta: str,
    reverse: bool = False,
    extra_links: list[tuple[str, str]] | None = None,
    extra_html: str = "",
) -> str:
    cls = _cls("cap-row", "reverse" if reverse else "", "reveal")
    more = "".join(
        f'<a class="more" href="{u}">{esc(n)}</a>' for n, u in (extra_links or [])
    )
    return f"""<article class="{cls}">
  <div class="cap-copy">
    <p class="eyebrow">{esc(kicker)}</p>
    <h2>{esc(name)}</h2>
    <p>{esc(copy)}</p>
    {extra_html}
    {tags(modules) if modules else ""}
    <p class="hero-actions" style="margin-top:1.1rem;margin-bottom:0">
      <a class="more" href="{href}">{esc(cta)}</a>
      {more}
    </p>
  </div>
  <div class="cap-visual">{visual}</div>
</article>"""


def industry_block(
    href: str,
    name: str,
    kicker: str,
    problem: str,
    digitise: str,
    visual: str,
    reverse: bool = False,
    cta: str = "Build a solution for your organisation",
    extra_links: list[tuple[str, str]] | None = None,
) -> str:
    extra = f"<p>{esc(digitise)}</p>"
    return feature_block(
        href, name, kicker, problem, [], visual, cta,
        reverse=reverse, extra_links=extra_links, extra_html=extra,
    )


def article_cover(kind: str) -> str:
    """Editorial 16:9 diagrams for Knowledge Centre — not stock photos or fake UIs."""
    if kind == "cost":
        inner = pipeline(["Discovery", "Design", "Development", "Testing", "Deployment", "Support"])
    elif kind == "compare":
        inner = """<div class="cover-split">
          <div><strong>Custom</strong><span>Your process</span></div>
          <p>vs</p>
          <div><strong>Off-the-shelf</strong><span>A common process</span></div>
        </div>"""
    elif kind == "choose":
        inner = pipeline(["See a system", "Ask who builds", "Ask after go-live"])
    elif kind == "bms":
        inner = hub_diagram("Operations", ["People", "Work", "Money", "Control"])
    elif kind == "workflow":
        inner = """<div class="cover-compare">
          <p class="cover-kicker">Manual</p>
          <ol class="pipeline"><li>Email</li><li>Spreadsheet</li><li>Approval</li><li>Invoice</li></ol>
          <p class="cover-kicker">In software</p>
          <ol class="pipeline"><li>System</li><li>Workflow</li><li>Approval</li><li>Reporting</li></ol>
        </div>"""
    elif kind == "school":
        inner = hub_diagram("School record", ["Students", "Attendance", "Fees", "Guardians", "HR", "Reports"])
    elif kind == "mobile":
        inner = (
            '<ul class="phone-mods" style="max-width:11rem;margin:0.8rem auto">'
            "<li>Accounts</li><li>Jobs</li><li>Sync</li></ul>"
        )
    else:
        inner = """<div class="cover-split">
          <div><strong>Custom CRM</strong><span>Your objects</span></div>
          <p>vs</p>
          <div><strong>Platform CRM</strong><span>Leads &amp; accounts</span></div>
        </div>"""
    return f'<div class="cover" data-cover="{esc(kind)}" aria-hidden="true">{inner}</div>'
