#!/usr/bin/env python3
"""Custom technical graphics. Schematics of real systems — not fake screenshots."""
from __future__ import annotations

from site_lib import esc

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


def _mods(items: list[str]) -> str:
    return "".join(f'<span>{esc(i)}</span>' for i in items)


def frame(title: str, inner: str, cls: str = "") -> str:
    return f"""<div class="frame {cls}">
  <div class="frame-chrome"><i></i><i></i><i></i><span>{esc(title)}</span></div>
  <div class="frame-body">{inner}</div>
</div>"""


def hero_stage() -> str:
    school = frame(
        "School / College LMS",
        f'<div class="mod-grid">{_mods(["Students", "Fees", "Attendance", "Parents", "HR", "Reports"])}</div>'
        '<p class="frame-caption">Portals for admin, finance, teachers, students and parents on one record.</p>',
        "frame-lg",
    )
    tshira = frame(
        "Tshira Workflow",
        '<ol class="flow-mini"><li>Intake</li><li>Assign</li><li>Field</li><li>Review</li><li>Invoice</li></ol>'
        '<p class="frame-caption">Finance locked until the case is ready.</p>',
        "frame-md",
    )
    mobile = frame(
        "VayaSA · Fluxmove",
        f'<div class="mod-stack">{_mods(["Bookings", "Drivers", "Payments", "Verification"])}</div>'
        '<p class="frame-caption">Passenger, driver and operator roles.</p>',
        "frame-phone",
    )
    return f"""<div class="hero-stage" aria-hidden="true">
  <div class="hero-glow"></div>
  {school}
  {tshira}
  {mobile}
</div>
<p class="hero-visual-note">System maps of software we have built. Live interface screenshots will replace these once supplied.</p>"""


def tech_banner() -> str:
    marks = "".join(
        f'<li><span class="tech-mark" aria-hidden="true"></span>{esc(t)}</li>' for t in BANNER_TECH
    )
    row = f'<ul class="tech-track">{marks}</ul>'
    return f"""<section class="tech-banner" aria-label="Technology we work with">
  <div class="container tech-banner-head">
    <h2>Technology We Work With</h2>
    <p>We choose technologies based on the requirements, scale and long-term needs of each system. The list is limited to tools used on Cyber Developers systems.</p>
  </div>
  <div class="tech-marquee">
    <div class="tech-marquee-inner">
      {row}
      {row}
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
    cls = "reverse" if reverse else ""
    return f"""<a class="showcase {cls} reveal" href="{href}">
  <div class="showcase-visual">{visual}</div>
  <div class="showcase-copy">
    <p class="eyebrow">{esc(kicker)}</p>
    <h3>{esc(name)}</h3>
    <p>{esc(copy)}</p>
    {tags(tag_list)}
    <span class="more">View Case Study</span>
  </div>
</a>"""


def vayasa_map() -> str:
    return frame(
        "VayaSA",
        f'<div class="mod-grid">{_mods(["Passenger", "Driver", "Bus operator", "Taxi operator", "Admin", "Payouts"])}</div>'
        '<ol class="flow-mini"><li>Search</li><li>Book</li><li>Pay</li><li>Ticket</li></ol>',
    )


def fluxmove_map() -> str:
    return frame(
        "Fluxmove",
        f'<div class="mod-grid">{_mods(["Customer booking", "Driver verify", "Vehicle types", "Admin review"])}</div>'
        '<ol class="flow-mini"><li>Book move</li><li>Match</li><li>Accept</li><li>Deliver</li></ol>',
    )


def tshira_map() -> str:
    return frame(
        "Tshira",
        '<ol class="flow-mini tall"><li>Intake</li><li>Provincial assign</li><li>Field collection</li><li>Quality check</li><li>Review</li><li>Invoice</li><li>Close</li></ol>',
    )


def school_map() -> str:
    return frame(
        "SchoolHub SA",
        f'<div class="mod-grid">{_mods(["Admin", "Finance", "Teachers", "Students", "Parents", "HR"])}</div>',
    )


def lawyer_map() -> str:
    return frame(
        "Practice system",
        f'<div class="mod-grid">{_mods(["Clients", "Matters", "Documents", "RAF", "Tasks", "Billing"])}</div>',
    )


def funeral_map() -> str:
    return frame(
        "Funeral parlour",
        '<p class="frame-caption">Administration software scoped to the parlour. Exact screens confirmed in a demo.</p>'
        f'<div class="mod-grid">{_mods(["Records", "Access", "Process fit"])}</div>',
    )


def municipality_map() -> str:
    return frame(
        "Municipality",
        f'<div class="mod-grid">{_mods(["Residents", "Billing", "Faults", "Queues", "Notices", "Admin"])}</div>',
    )


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


def _svg_arch() -> str:
    return """<svg class="arch-svg" viewBox="0 0 920 420" role="img" aria-labelledby="archTitle archDesc">
  <title id="archTitle">Application architecture</title>
  <desc id="archDesc">Users connect to a web or mobile application, then an API layer, database, integrations and cloud infrastructure.</desc>
  <defs>
    <linearGradient id="archLine" x1="0" x2="0" y1="0" y2="1">
      <stop offset="0" stop-color="#4c7dff" stop-opacity="0.9"/>
      <stop offset="1" stop-color="#4c7dff" stop-opacity="0.2"/>
    </linearGradient>
  </defs>
  <g class="arch-spine" stroke="url(#archLine)" stroke-width="2" fill="none">
    <path d="M460 52 V368"/>
  </g>
  <g font-family="IBM Plex Mono, ui-monospace, monospace" font-size="12" fill="#94a3b8">
    <g transform="translate(330,18)">
      <rect width="260" height="44" rx="4" fill="#141c2e" stroke="rgba(148,163,184,0.28)"/>
      <text x="130" y="27" text-anchor="middle" fill="#e8eef7" font-size="13">Users</text>
    </g>
    <g transform="translate(250,92)">
      <rect width="420" height="52" rx="4" fill="#141c2e" stroke="rgba(76,125,255,0.45)"/>
      <text x="210" y="32" text-anchor="middle" fill="#e8eef7" font-size="13">Web / Mobile Application</text>
    </g>
    <g transform="translate(280,172)">
      <rect width="360" height="48" rx="4" fill="#141c2e" stroke="rgba(148,163,184,0.28)"/>
      <text x="180" y="30" text-anchor="middle" fill="#e8eef7">Application / API Layer</text>
    </g>
    <g transform="translate(310,248)">
      <rect width="300" height="44" rx="4" fill="#141c2e" stroke="rgba(148,163,184,0.28)"/>
      <text x="150" y="27" text-anchor="middle" fill="#e8eef7">Database</text>
    </g>
    <g transform="translate(40,248)">
      <rect width="200" height="88" rx="4" fill="#0e1626" stroke="rgba(148,163,184,0.22)"/>
      <text x="100" y="28" text-anchor="middle" fill="#e8eef7">Integrations</text>
      <text x="100" y="50" text-anchor="middle">Payments · SMS</text>
      <text x="100" y="68" text-anchor="middle">Identity · Email</text>
    </g>
    <g transform="translate(680,248)">
      <rect width="200" height="88" rx="4" fill="#0e1626" stroke="rgba(148,163,184,0.22)"/>
      <text x="100" y="28" text-anchor="middle" fill="#e8eef7">Cloud</text>
      <text x="100" y="50" text-anchor="middle">Hosting · Backups</text>
      <text x="100" y="68" text-anchor="middle">Auth · Analytics</text>
    </g>
    <g transform="translate(330,348)">
      <rect width="260" height="44" rx="4" fill="#141c2e" stroke="rgba(148,163,184,0.28)"/>
      <text x="130" y="27" text-anchor="middle" fill="#e8eef7">Permissions &amp; support</text>
    </g>
  </g>
  <g stroke="#4c7dff" stroke-width="1.2" fill="none" opacity="0.55">
    <path d="M250 272 H140"/>
    <path d="M670 272 H780"/>
  </g>
</svg>"""


def architecture() -> str:
    return f"""<section class="section" id="architecture">
  <div class="container arch-layout">
    <div class="reveal">
      <h2>Built Beyond the Interface</h2>
      <p class="lead">A reliable system requires more than a good-looking screen. We design the application structure, data, integrations, permissions, deployment and support around how the organisation needs to operate.</p>
      <ul class="arch-labels">
        <li>Frontend</li><li>Backend</li><li>API</li><li>Database</li>
        <li>Authentication</li><li>Payments</li><li>Notifications</li><li>Cloud</li>
      </ul>
    </div>
    <div class="arch-graphic reveal">{_svg_arch()}</div>
  </div>
</section>"""


def capability_visual(kind: str) -> str:
    if kind == "custom":
        inner = f'<div class="mod-grid">{_mods(["Roles", "Records", "Exceptions", "Reports"])}</div>'
        return frame("Application model", inner)
    if kind == "business":
        inner = f'<div class="mod-grid">{_mods(["People", "Money", "Cases", "Audit"])}</div>'
        return frame("Operational system", inner)
    if kind == "web":
        inner = f'<div class="mod-grid">{_mods(["Staff portal", "Customer access", "Queues", "Documents"])}</div>'
        return frame("Web application", inner)
    if kind == "mobile":
        inner = f'<div class="mod-stack">{_mods(["Jobs", "Status", "Capture", "Sync"])}</div>'
        return frame("Field client", inner, "frame-phone")
    if kind == "workflow":
        inner = '<ol class="flow-mini"><li>Capture</li><li>Assign</li><li>Review</li><li>Invoice</li><li>Close</li></ol>'
        return frame("Named stages", inner)
    if kind == "ai":
        inner = '<ol class="flow-mini"><li>Document</li><li>Extract</li><li>Record</li><li>Human check</li></ol>'
        return frame("Inside the application", inner)
    inner = f'<div class="mod-grid">{_mods(["Paystack / Ozow", "SMS / Email", "SA ID", "Existing SQL"])}</div>'
    return frame("Connected services", inner)


def capabilities_editorial() -> str:
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
        cls = "cap-row reverse reveal" if rev else "cap-row reveal"
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
    return f"""<section class="section section-alt" id="services">
  <div class="container">
    <div class="section-intro reveal">
      <h2>What We Build</h2>
      <p class="lead">Manage customers, documents, approvals, payments and reporting from one system — or connect the systems you already have.</p>
    </div>
    {''.join(blocks)}
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
    lis = "".join(
        f"<li><h3>{esc(t)}</h3><p>{esc(d)}</p></li>" for t, d in steps
    )
    return f"""<section class="section section-alt" id="process">
  <div class="container">
    <div class="section-intro reveal">
      <h2>How a project usually runs</h2>
      <p class="lead">Ordinary engineering, written down so nobody is surprised at go-live.</p>
    </div>
    <ol class="lifecycle reveal">{lis}</ol>
  </div>
</section>"""
