#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path
from datetime import date

sys.path.insert(0, str(Path(__file__).resolve().parent))
from site_lib import (
    ROOT, SITE, TECHS, ORG_DESC, EMAIL, PHONE_DISPLAY, PHONE_E164, ADDRESS_LINE, WA_URL,
    icon, esc, render_page, write_page, redirect_page, crumbs_html, cta_band,
    enquiry_form, faq_html, service_schema, faq_schema, article_schema,
)

TODAY = date.today().isoformat()
SITEMAP_URLS: list[tuple[str, str]] = []


def add_url(canonical: str, priority: str = "0.7") -> None:
    SITEMAP_URLS.append((canonical, priority))


def emit(rel, title, description, canonical, crumbs, body, extra=None, current=None, image="/assets/img/og-default.webp", og_type="website", priority="0.7"):
    html = render_page(rel, title, description, canonical, crumbs, body, extra, og_type, image, current)
    write_page(rel, html)
    add_url(canonical, priority)


def checks(items: list[str]) -> str:
    lis = "".join(f"<li>{icon('check')}<span>{esc(i)}</span></li>" for i in items)
    return f'<ul class="feature-list">{lis}</ul>'


def cards(items: list[dict], cls="grid-3") -> str:
    out = []
    for it in items:
        ic = icon(it.get("icon", "code"))
        more = f'<p class="more">{esc(it.get("more", "Learn more"))} →</p>' if it.get("href") else ""
        inner = f'<div class="icon-box">{ic}</div><h3>{esc(it["title"])}</h3><p>{esc(it["text"])}</p>{more}'
        if it.get("href"):
            out.append(f'<a class="card" href="{it["href"]}">{inner}</a>')
        else:
            out.append(f'<article class="card">{inner}</article>')
    return f'<div class="{cls}">{"".join(out)}</div>'


def homepage() -> None:
    faqs = [
        (
            "Is Cyber Developers a cybersecurity company?",
            "No. Cyber Developers is a custom software development company. We design and build business systems, web applications, mobile apps, workflow automation and integrations for organisations in South Africa.",
        ),
        (
            "Are you the same company as CyberDevs?",
            "No. Cyber Developers is a separate company. We develop custom software and business systems, and we publish under the name Cyber Developers at cyberdevelopers.co.za.",
        ),
        (
            "Do you only build websites?",
            "No. Websites can be part of a project, but the core work is custom software: operational systems, portals, mobile apps, automation and integrations that match how a business actually runs.",
        ),
        (
            "Can you customise an existing system rather than starting from scratch?",
            "Yes. Many engagements start with a system we have already built — school management, workflow, logistics, municipality or similar — and adapt it to the organisation’s process, roles and reporting.",
        ),
    ]
    body = f"""
<section class="hero"><div class="container hero-grid">
  <div>
    <p class="eyebrow">Cyber Developers — Custom Software &amp; Business Systems South Africa</p>
    <h1>Software Built Around Your Business.</h1>
    <p class="lead">Custom software, business systems, web applications and mobile apps developed for organisations across South Africa.</p>
    <div class="hero-actions">
      <a class="btn btn-primary btn-lg" href="/contact/" data-track="consultation_requested" data-track-location="hero">Discuss Your Project</a>
      <a class="btn btn-secondary btn-lg" href="/our-work/">View Our Work</a>
    </div>
    <p class="hero-note">We build operational software — not generic marketing sites. If the work already happens on paper, spreadsheets or disconnected tools, that is usually where a custom system belongs.</p>
  </div>
  <aside class="hero-visual panel" aria-hidden="true">
    <div class="panel-head"><span>Business system</span><span>Roles · workflow · records</span></div>
    <div class="ui-window">
      <div class="ui-bar"><i></i><i></i><i></i></div>
      <div class="ui-rows">
        <div class="ui-row"><b></b><span></span><i class="ui-chip"></i></div>
        <div class="ui-row"><b></b><span></span><i class="ui-chip"></i></div>
        <div class="ui-row"><b></b><span></span><i class="ui-chip"></i></div>
        <div class="ui-row"><b></b><span></span><i class="ui-chip"></i></div>
      </div>
    </div>
    <div class="ui-kpis">
      <div class="kpi"><strong>Systems</strong><span>Built to process</span></div>
      <div class="kpi"><strong>Web &amp; mobile</strong><span>Used in the field</span></div>
      <div class="kpi"><strong>Integration</strong><span>APIs &amp; data</span></div>
    </div>
  </aside>
</div></section>

<section class="section section-alt" id="services"><div class="container">
  <div class="section-head">
    <p class="eyebrow">What we build</p>
    <h2>Software that runs the work, not just the website.</h2>
    <p>Each engagement starts with the business process. The product is a system people can log into, capture work in, and report from.</p>
  </div>
  {cards([
    dict(icon="code", title="Custom Software Development", text="Applications designed around your operations, roles, data and reporting — not a template forced onto the business.", href="/services/custom-software-development/"),
    dict(icon="layers", title="Business Management Systems", text="Multi-user systems for records, finance, staff, customers and day-to-day administration.", href="/services/business-systems/"),
    dict(icon="globe", title="Web Applications", text="Browser-based applications and portals for staff, customers, students, citizens or partners.", href="/services/web-application-development/"),
    dict(icon="phone", title="Mobile App Development", text="Mobile applications for field teams, drivers, customers and other users who work away from a desk.", href="/services/mobile-app-development/"),
    dict(icon="flow", title="Workflow Automation", text="Structured case, task and approval flows that replace email chains and manual handovers.", href="/services/workflow-automation/"),
    dict(icon="spark", title="AI & Business Automation", text="Practical assistants, document processing, reporting and integrations — used inside real systems, not as a slogan.", href="/services/ai-business-automation/"),
    dict(icon="plug", title="Systems Integration", text="Connecting software, payments, SMS, identity and existing databases so information does not live in silos.", href="/services/systems-integration/"),
  ])}
</div></section>

<section class="section" id="solutions"><div class="container">
  <div class="section-head">
    <p class="eyebrow">Featured software solutions</p>
    <h2>Systems we can provide or customise.</h2>
    <p>These are commercial starting points based on software Cyber Developers has already designed. Features are adapted to the organisation, not promised as a one-size product brochure.</p>
  </div>
  {cards([
    dict(title="School Management System", text="Students, guardians, attendance, academics, fees, HR, communication and reporting for South African schools and colleges.", href="/solutions/school-management-system/"),
    dict(title="Law Firm Management Software", text="Client and case records, documents, tasks, billing, permissions and specialised legal workflows.", href="/solutions/law-firm-management-software/"),
    dict(title="Funeral Parlour Management Software", text="Custom management software for funeral businesses, scoped to the processes the parlour actually runs.", href="/solutions/funeral-parlour-management-software/"),
    dict(title="Workflow Management System", text="Multi-role case workflows, documents, provincial or team assignment, billing and audit history.", href="/solutions/workflow-management-system/"),
    dict(title="Municipality Management Platform", text="Citizen services, billing, fault reporting, queues, notices and municipal administration in one platform.", href="/solutions/municipality-management-software/"),
    dict(title="Logistics & Delivery Software", text="Bookings, driver verification, vehicle types, tracking status and admin review for delivery operations.", href="/solutions/logistics-delivery-software/"),
    dict(title="Custom CRM Development", text="Customer, quoting, invoicing and service records built around how your team sells and supports.", href="/solutions/custom-crm-development/"),
  ], "grid-3")}
  <p><a class="section-link" href="/solutions/">All solutions</a></p>
</div></section>

<section class="section section-alt"><div class="container">
  <div class="section-head">
    <p class="eyebrow">Featured projects</p>
    <h2>Real systems, described without invented results.</h2>
    <p>Project pages summarise what was built and which technologies were used. They do not invent user counts, revenue figures or testimonials.</p>
  </div>
  <div class="grid-3">
    <a class="card project-card" href="/our-work/vayasa/"><div class="visual"><span>VayaSA</span></div><div class="body"><span class="tag">Transport</span><h3>VayaSA</h3><p>Ride sharing and passenger transport marketplace for South Africa, including bus and taxi bookings.</p></div></a>
    <a class="card project-card" href="/our-work/fluxmove/"><div class="visual"><span>Fluxmove</span></div><div class="body"><span class="tag">Logistics</span><h3>Fluxmove</h3><p>Nationwide delivery marketplace connecting customers with verified drivers across vehicle types.</p></div></a>
    <a class="card project-card" href="/our-work/tshira-workflow-system/"><div class="visual"><span>Tshira</span></div><div class="body"><span class="tag">Workflow</span><h3>Tshira Workflow System</h3><p>Multi-province case workflow with field data collection, review, requisitions, expenses and invoicing.</p></div></a>
    <a class="card project-card" href="/our-work/school-lms/"><div class="visual"><span>SchoolHub SA</span></div><div class="body"><span class="tag">Education</span><h3>School / College LMS</h3><p>School management platform with portals for admin, finance, teachers, students, parents and HR.</p></div></a>
    <a class="card project-card" href="/our-work/municipality-platform/"><div class="visual"><span>Municipality</span></div><div class="body"><span class="tag">Government</span><h3>Municipality Platform</h3><p>Citizen and admin application for billing, issue reporting, queues, notices and resident services.</p></div></a>
    <a class="card project-card" href="/our-work/lawyer-management-system/"><div class="visual"><span>Legal</span></div><div class="body"><span class="tag">Legal</span><h3>Lawyer Management System</h3><p>Practice software covering clients, cases, documents, tasks, billing and user permissions.</p></div></a>
  </div>
  <p><a class="section-link" href="/our-work/">See all work</a></p>
</div></section>

<section class="section"><div class="container">
  <div class="section-head">
    <p class="eyebrow">Industries</p>
    <h2>Organisations we can serve.</h2>
  </div>
  <div class="grid-3">
    {''.join(f'<div class="industry-item">{icon("layers")}<span>{esc(n)}</span></div>' for n in [
      "Education","Legal","Government & Municipalities","Logistics","Transport","Retail","Professional Services","SMEs","Enterprise"
    ])}
  </div>
  <p><a class="section-link" href="/industries/">Industries we work with</a></p>
</div></section>

<section class="section section-alt"><div class="container">
  <div class="section-head">
    <p class="eyebrow">Development process</p>
    <h2>A straightforward path from idea to live system.</h2>
  </div>
  <ol class="process">
    <li><h3>Discovery</h3></li>
    <li><h3>Planning</h3></li>
    <li><h3>UI/UX &amp; Architecture</h3></li>
    <li><h3>Development</h3></li>
    <li><h3>Testing</h3></li>
    <li><h3>Deployment</h3></li>
    <li><h3>Support &amp; Maintenance</h3></li>
  </ol>
</div></section>

<section class="section"><div class="container">
  <div class="section-head">
    <p class="eyebrow">Technology</p>
    <h2>Tools used on real Cyber Developers systems.</h2>
    <p>This list is limited to technologies present in our public engineering work and stack. It is not a catalogue of every platform on the market.</p>
  </div>
  <div class="tech-row">{''.join(f'<span>{esc(t)}</span>' for t in TECHS)}</div>
</div></section>

<section class="section section-alt"><div class="container split">
  <div>
    <p class="eyebrow">Questions</p>
    <h2>Clear answers before you enquire.</h2>
  </div>
  {faq_html(faqs)}
</div></section>
{cta_band()}
"""
    emit(
        "index.html",
        "Cyber Developers — Custom Software & Business Systems South Africa",
        "Software built around your business. Custom software, business systems, web applications and mobile apps for organisations across South Africa.",
        "/",
        [("/", "Home")],
        body,
        extra=[faq_schema(faqs)],
        current="/",
        priority="1.0",
    )


def about_page() -> None:
    body = f"""
<section class="page-hero"><div class="container">
  {crumbs_html([("/", "Home"), ("/about/", "About")])}
  <p class="eyebrow">About Cyber Developers</p>
  <h1>A South African software company that builds systems around the business.</h1>
  <p class="lead">Cyber Developers develops custom software. We are not a cybersecurity firm, and we are not CyberDevs. The work is business systems, web applications, mobile apps, workflow automation and integration.</p>
</div></section>
<section class="section"><div class="container split">
  <div class="prose">
    <h2>Who we are</h2>
    <p>Cyber Developers is a custom software development company serving organisations in South Africa. We design and implement software that matches an organisation’s actual process — students and fees, cases and documents, deliveries and drivers, municipal services, or internal workflow.</p>
    <p>The public site previously used marketing language that sounded like a generic digital agency. That is not the positioning. If you need a brochure website only, there are many agencies for that. If you need software people will work in every day, that is the brief we take.</p>
    <h2>What we build</h2>
    <p>Typical work includes multi-user web applications, role-based portals, operational mobile apps, billing and records, reporting, and connections to payments, SMS, identity and other APIs. Existing products such as the school management platform, VayaSA, Fluxmove, the Tshira workflow system and the municipality platform are the proof of that range.</p>
    <h2>Who we serve</h2>
    <p>Schools and colleges, professional firms, municipalities, logistics and transport operators, retailers, SMEs and larger organisations that need software fitted to their process rather than the other way around.</p>
    <h2>Our approach</h2>
    <p>Discovery first: who the users are, which records matter, which approvals exist, and which systems already hold data. Then architecture and interface, then development, testing, deployment, and ongoing support. We would rather ship a system that matches the work than a visually impressive demo that cannot be operated.</p>
    <h2>Support and maintenance</h2>
    <p>Live systems need hosting, backups, user support and change requests. We treat that as part of software delivery, not an afterthought. Specific support hours and response times are agreed per project rather than advertised as a blanket 24/7 claim.</p>
  </div>
  <aside class="card">
    <h3>Identity, plainly</h3>
    <p>Company name: Cyber Developers</p>
    <p style="margin-top:0.8rem">Positioning: Custom software and business systems, South Africa</p>
    <p style="margin-top:0.8rem">Primary message: Software built around your business.</p>
    <p style="margin-top:1.2rem"><a class="btn btn-primary" href="/contact/">Discuss Your Project</a></p>
  </aside>
</div></section>
{cta_band()}
"""
    emit(
        "about/index.html",
        "About Cyber Developers | Custom Software South Africa",
        "Cyber Developers is a South African custom software company building business systems, web applications, mobile apps and integrations. Not a cybersecurity firm, and not CyberDevs.",
        "/about/",
        [("/", "Home"), ("/about/", "About")],
        body,
        current="/about/",
    )


def contact_page() -> None:
    body = f"""
<section class="page-hero"><div class="container">
  {crumbs_html([("/", "Home"), ("/contact/", "Contact")])}
  <p class="eyebrow">Contact</p>
  <h1>Discuss your project.</h1>
  <p class="lead">Tell us what the software needs to do. We will help you decide whether a custom system, a customised existing product, or a smaller integration is the right next step.</p>
</div></section>
<section class="section"><div class="container split">
  <div>
    <div class="contact-details">
      <p><span>Email</span><a href="mailto:{EMAIL}" data-track="email_clicked">{EMAIL}</a></p>
      <p><span>Phone</span><a href="tel:{PHONE_E164}" data-track="phone_clicked">{PHONE_DISPLAY}</a></p>
      <p><span>WhatsApp</span><a href="{WA_URL}" data-track="whatsapp_clicked" rel="noopener">Message Cyber Developers</a></p>
      <p><span>Address</span>{esc(ADDRESS_LINE)}</p>
    </div>
    <p style="margin-top:1.5rem"><a class="btn btn-whatsapp" href="{WA_URL}" data-track="whatsapp_clicked">WhatsApp: discuss a software project</a></p>
  </div>
  {enquiry_form("project_enquiry", "New project enquiry | Cyber Developers", "Discuss Your Project")}
</div></section>
"""
    emit(
        "contact/index.html",
        "Contact Cyber Developers | Discuss Your Project",
        "Request a consultation with Cyber Developers. Enquire about custom software, business systems, web apps, mobile apps or a product demo.",
        "/contact/",
        [("/", "Home"), ("/contact/", "Contact")],
        body,
        current="/contact/",
        priority="0.9",
    )

    thanks = f"""
<section class="page-hero"><div class="container">
  {crumbs_html([("/", "Home"), ("/contact/", "Contact"), ("/contact/thank-you/", "Thank you")])}
  <h1>Enquiry received.</h1>
  <p class="lead">Thank you. We will review what you sent and respond by email. If the matter is urgent, call {PHONE_DISPLAY} or use WhatsApp.</p>
  <p style="margin-top:1.5rem" class="hero-actions">
    <a class="btn btn-primary" href="{WA_URL}" data-track="whatsapp_clicked">WhatsApp</a>
    <a class="btn btn-secondary" href="/our-work/">View Our Work</a>
  </p>
</div></section>
"""
    emit(
        "contact/thank-you/index.html",
        "Thank you | Cyber Developers",
        "Your Cyber Developers enquiry has been received.",
        "/contact/thank-you/",
        [("/", "Home"), ("/contact/", "Contact"), ("/contact/thank-you/", "Thank you")],
        thanks,
        current="/contact/",
        priority="0.1",
    )


def industries_page() -> None:
    blocks = [
        ("Education", "Schools, colleges, TVETs and training centres need student records, guardians, attendance, fees and staff administration in one place.", "/solutions/school-management-system/"),
        ("Legal", "Practices need clients, cases, documents, tasks, billing and controlled access — including specialised workflows where they apply.", "/solutions/law-firm-management-software/"),
        ("Government & Municipalities", "Citizen portals, billing, fault reporting, queues and notices require role-based systems, not a static municipal website.", "/solutions/municipality-management-software/"),
        ("Logistics", "Delivery operations need bookings, driver onboarding, vehicle types, status tracking and admin review.", "/solutions/logistics-delivery-software/"),
        ("Transport", "Ride sharing, bus and taxi booking, driver verification and payments are software problems as much as operations problems.", "/our-work/vayasa/"),
        ("Retail", "Inventory, invoicing, customer records and store processes can be modelled as a custom system when off-the-shelf tools do not fit."),
        ("Professional Services", "Consultancies and similar firms often need workflow, documents, billing and multi-role review rather than a generic CRM."),
        ("SMEs", "Smaller organisations still need reliable records, invoices and staff access — usually with a narrower scope and a clearer process."),
        ("Enterprise", "Larger organisations typically need integration, permissions, audit trails and staged delivery onto existing systems."),
    ]
    cards_html = []
    for b in blocks:
        link = f'<p class="more">Related solution →</p>' if len(b) > 2 else ""
        href = b[2] if len(b) > 2 else None
        inner = f"<h3>{esc(b[0])}</h3><p>{esc(b[1])}</p>{link}"
        cards_html.append(f'<a class="card" href="{href}">{inner}</a>' if href else f'<article class="card">{inner}</article>')
    body = f"""
<section class="page-hero"><div class="container">
  {crumbs_html([("/", "Home"), ("/industries/", "Industries")])}
  <p class="eyebrow">Industries</p>
  <h1>Software for the way each sector actually works.</h1>
  <p class="lead">We do not claim to be a specialist agency in every industry. We do build systems whose data models, roles and workflows match the sector.</p>
</div></section>
<section class="section"><div class="container"><div class="grid-3">{''.join(cards_html)}</div></div></section>
{cta_band()}
"""
    emit(
        "industries/index.html",
        "Industries | Cyber Developers Custom Software South Africa",
        "Cyber Developers builds custom software for education, legal, municipalities, logistics, transport, retail, professional services, SMEs and enterprise organisations in South Africa.",
        "/industries/",
        [("/", "Home"), ("/industries/", "Industries")],
        body,
        current="/industries/",
    )


def privacy_page() -> None:
    body = f"""
<section class="page-hero"><div class="container">
  {crumbs_html([("/", "Home"), ("/privacy/", "Privacy")])}
  <h1>Privacy Policy</h1>
  <p class="muted">Last updated: {TODAY}</p>
</div></section>
<section class="section legal"><div class="container prose">
  <p>Cyber Developers (“we”, “our”, “us”) is committed to protecting personal information in line with the Protection of Personal Information Act (POPIA).</p>
  <h2>Information we collect</h2>
  <p>When you submit an enquiry or newsletter form we may collect your name, company, email address, phone number, project type, optional budget range, and the description you provide.</p>
  <h2>How we use it</h2>
  <p>We use this information to respond to enquiries, prepare consultations or demonstrations, and — only if you subscribe — send occasional updates. We do not sell personal information.</p>
  <h2>Form delivery</h2>
  <p>Enquiry forms are delivered using FormSubmit to {EMAIL}. That provider processes the message in order to send it to us.</p>
  <h2>Your rights</h2>
  <p>You may request access, correction or deletion of personal information we hold. Contact {EMAIL} or info@cyberdevelopers.co.za.</p>
  <h2>Cookies and analytics</h2>
  <p>If a Google Analytics 4 measurement ID is configured on this site, usage data may be collected to understand which pages are useful. You can block analytics cookies in your browser.</p>
</div></section>
"""
    emit(
        "privacy/index.html",
        "Privacy Policy | Cyber Developers",
        "Cyber Developers privacy policy. How we collect and use enquiry information under POPIA.",
        "/privacy/",
        [("/", "Home"), ("/privacy/", "Privacy")],
        body,
        current="/about/",
        priority="0.3",
    )


def not_found() -> None:
    body = f"""
<section class="not-found"><div class="container">
  <p class="eyebrow">404</p>
  <h1>This page is not available.</h1>
  <p class="lead" style="margin-inline:auto">The address may have changed. Use the links below to continue.</p>
  <p class="hero-actions" style="justify-content:center;margin-top:1.5rem">
    <a class="btn btn-primary" href="/">Home</a>
    <a class="btn btn-secondary" href="/contact/">Contact</a>
    <a class="btn btn-secondary" href="/our-work/">Our Work</a>
  </p>
</div></section>
"""
    emit(
        "404.html",
        "Page not found | Cyber Developers",
        "The page you requested is not available on the Cyber Developers website.",
        "/404.html",
        [("/", "Home"), ("/404.html", "Not found")],
        body,
        current="/",
        priority="0.1",
    )


if __name__ == "__main__":
    homepage()
    about_page()
    contact_page()
    industries_page()
    privacy_page()
    not_found()
    print("core pages done", len(SITEMAP_URLS))
