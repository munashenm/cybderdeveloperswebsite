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


def work_visual(slug: str, alt: str, fallback: str) -> str:
    """Use a genuine screenshot when present; otherwise the schematic."""
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
    return work_visual(
        "vayasa",
        "VayaSA",
        app_shell(
            "VayaSA",
            ["Passenger", "Driver", "Bus operator", "Taxi operator", "Admin"],
            ["Search", "Bookings", "Payouts", "Verification"],
            ["Search", "Book", "Pay", "Ticket"],
        ),
    )


def fluxmove_map() -> str:
    return work_visual(
        "fluxmove",
        "Fluxmove",
        app_shell(
            "Fluxmove",
            ["Customer", "Driver", "Admin", "Support"],
            ["Booking", "Vehicle types", "Verification", "Open jobs"],
            ["Book move", "Match", "Accept", "Deliver"],
        ),
    )


def tshira_map() -> str:
    return work_visual(
        "tshira-workflow-system",
        "Tshira",
        app_shell(
            "Tshira",
            ["Intake", "Province", "Field", "Review", "Finance"],
            ["Cases", "Documents", "Requisitions", "Invoices"],
            ["Intake", "Assign", "Collect", "Review", "Invoice", "Close"],
            active=2,
        ),
    )


def school_map() -> str:
    return work_visual(
        "school-lms",
        "SchoolHub SA",
        app_shell(
            "SchoolHub SA",
            ["Admin", "Finance", "Teachers", "Students", "Parents", "HR"],
            ["Students", "Fees", "Attendance", "Reports"],
            ["Enrol", "Attend", "Assess", "Report"],
        ),
    )


def lawyer_map() -> str:
    return work_visual(
        "lawyer-management-system",
        "Practice system",
        app_shell(
            "Practice system",
            ["Clients", "Matters", "Documents", "RAF", "Billing"],
            ["Matters", "Documents", "Tasks", "Billing"],
            ["Open", "Work", "Bill", "Close"],
        ),
    )


def funeral_map() -> str:
    return work_visual(
        "funeral-parlour-system",
        "Funeral parlour",
        frame(
            "Funeral parlour",
            '<p class="frame-caption">Administration software scoped to the parlour. Exact screens confirmed in a demo.</p>'
            '<div class="shell-panels compact">'
            '<div class="shell-panel"><strong>Records</strong><span></span></div>'
            '<div class="shell-panel"><strong>Access</strong><span></span></div>'
            '<div class="shell-panel"><strong>Process fit</strong><span></span></div>'
            "</div>",
        ),
    )


def municipality_map() -> str:
    return work_visual(
        "municipality-platform",
        "Municipality",
        app_shell(
            "Municipality",
            ["Residents", "Billing", "Faults", "Queues", "Admin"],
            ["Faults", "Bills", "Queues", "Notices"],
            ["Report", "Queue", "Resolve", "Notify"],
        ),
    )


def hero_stage() -> str:
    school = app_shell(
        "School / College LMS",
        ["Admin", "Finance", "Teachers", "Students", "Parents", "HR"],
        ["Students", "Fees", "Attendance", "Reports"],
        ["Enrol", "Attend", "Assess", "Report"],
        cls="frame-lg",
    )
    tshira = app_shell(
        "Tshira Workflow",
        ["Intake", "Field", "Review", "Finance"],
        ["Cases", "Documents"],
        ["Intake", "Assign", "Collect", "Review", "Invoice"],
        active=1,
        cls="frame-md",
    )
    mobile = phone_frame(
        "VayaSA",
        '<ul class="phone-mods">'
        "<li>Bookings</li><li>Drivers</li><li>Payments</li><li>Tickets</li>"
        "</ul>"
        '<p class="frame-caption">Passenger, driver and operator roles.</p>',
    )
    return f"""<div class="hero-stage" aria-hidden="true">
  <div class="hero-grid-bg"></div>
  <div class="hero-glow"></div>
  {school}
  {tshira}
  {mobile}
</div>
<p class="hero-visual-note">Layered system maps of products we have built. Live interface screenshots will replace these maps when supplied.</p>"""


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
) -> str:
    cls = _cls("showcase", "reverse" if reverse else "", "reveal")
    return f"""<a class="{cls}" href="{href}">
  <div class="showcase-visual">{visual}</div>
  <div class="showcase-copy">
    <p class="eyebrow">{esc(kicker)}</p>
    <h3>{esc(name)}</h3>
    <p>{esc(copy)}</p>
    {tags(tag_list)}
    <span class="more">View Case Study</span>
  </div>
</a>"""


def selected_work() -> str:
    return f"""<section class="section" id="work">
  <div class="container">
    <div class="section-intro reveal">
      <h2>Selected Work</h2>
      <p class="lead">Systems designed around a real operating model. These are maps of modules we have actually built — not invented dashboards.</p>
    </div>
    {showcase("/our-work/vayasa/", "VayaSA", "Ride-hailing & transport platform",
              "Ride sharing, bus tickets and taxi seats between cities, with South African payments and driver verification.",
              ["Web App", "Mobile Experience", "Payments", "Driver Management", "Booking System"],
              vayasa_map())}
    {showcase("/our-work/fluxmove/", "Fluxmove", "Delivery marketplace",
              "Customers book a move; verified drivers with bakkies, vans or trucks accept jobs. Admin reviews applications.",
              ["Web App", "Driver App", "Verification", "Vehicle Types"],
              fluxmove_map(), reverse=True)}
    {showcase("/our-work/tshira-workflow-system/", "Tshira Workflow System", "Case workflow",
              "Provincial assignment, field collection, review, requisitions, expenses and invoicing with finance locked until work is complete.",
              ["Workflow", "Roles", "Documents", "Invoicing"],
              tshira_map())}
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
        ("Education", "/solutions/school-management-system/"),
        ("Legal", "/solutions/law-firm-management-software/"),
        ("Government", "/solutions/municipality-management-software/"),
        ("Logistics", "/solutions/logistics-delivery-software/"),
        ("Transport", "/our-work/vayasa/"),
        ("Retail", "/industries/"),
        ("Professional services", "/industries/"),
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
