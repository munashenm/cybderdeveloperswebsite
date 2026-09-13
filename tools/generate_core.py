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
from graphics import (
    hero_stage, tech_banner, selected_work, more_work, capabilities_editorial,
    architecture, engineering_matrix, industries_band, process_flow,
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
    """Editorial rows. Kept for older call sites; prefer row_list for new pages."""
    out = []
    for it in items:
        more = f'<span class="more">{esc(it.get("more", "Details"))}</span>' if it.get("href") else ""
        inner = f'<h3>{esc(it["title"])}</h3><p>{esc(it["text"])}</p>{more}'
        if it.get("href"):
            out.append(f'<a href="{it["href"]}">{inner}</a>')
        else:
            out.append(f"<article>{inner}</article>")
    return f'<div class="row-list">{"".join(out)}</div>'


def bullets(items: list[str]) -> str:
    return "<ul>" + "".join(f"<li>{esc(i)}</li>" for i in items) + "</ul>"


def tech_line(techs: list[str]) -> str:
    return '<p class="tech-inline">' + " · ".join(esc(t) for t in techs) + "</p>"


def homepage() -> None:
    faqs = [
        (
            "Is Cyber Developers a cybersecurity company?",
            "No. Cyber Developers is a custom software development company. We design and build business systems, web applications, mobile apps, workflow automation and integrations for organisations in South Africa.",
        ),
        (
            "Do you only build websites?",
            "A website can be part of a project. The usual brief is software people work in every day: records, approvals, billing, mobile capture and the APIs those things need.",
        ),
        (
            "Do you always start from scratch?",
            "Not if we already have a close fit. School management, workflow, logistics and municipal systems can be adapted. If the process is genuinely different, we design a new model.",
        ),
        (
            "What happens after the system is live?",
            "Hosting, backups, user issues and change requests are part of the work. Hours and response times are written into the project, not advertised as 24/7 for every client.",
        ),
    ]
    body = f"""
<section class="hero"><div class="container hero-grid">
  <div>
    <p class="eyebrow">Cyber Developers · South Africa</p>
    <h1>Software Built Around Your Business.</h1>
    <p class="lead">Custom software, business systems, web applications and mobile apps developed for organisations across South Africa.</p>
    <div class="hero-actions">
      <a class="btn btn-primary btn-lg" href="/contact/" data-track="consultation_requested" data-track-location="hero">Discuss Your Project</a>
      <a class="btn btn-secondary btn-lg" href="/our-work/">View Our Work</a>
    </div>
    <p class="hero-note">If the work still lives in spreadsheets, paper files or three disconnected tools, that is usually the brief.</p>
  </div>
  <aside>{hero_stage()}</aside>
</div></section>
{tech_banner()}
{selected_work()}
{capabilities_editorial()}
{architecture()}
{engineering_matrix()}
{industries_band()}
{process_flow()}
{more_work()}
<section class="section"><div class="container split">
  <div>
    <h2>Before you enquire</h2>
    <p>Short answers. If yours is not here, write it on the form.</p>
  </div>
  {faq_html(faqs)}
</div></section>
{cta_band("Need a system your current software cannot provide?", "Describe the process. We will tell you whether to build, adapt, or leave it.")}
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
  <h1>About Cyber Developers</h1>
  <p class="lead">Cyber Developers is a South African custom software development company building business systems, web applications, mobile apps, workflow automation and integrations.</p>
</div></section>
<section class="section"><div class="container prose">
  <p>Most organisations already run on a mix of spreadsheets, email, WhatsApp, a website and one or two packages that never quite matched the job. That holds until volumes grow, staff change, or two systems need to share the same data.</p>
  <p>We take over at that point. We map the real process, design the data, build the application, connect payments or documents where they are needed, and stay available when the first version has to change.</p>
  <p>A public website can sit inside a product we build. The product is the work. We do not sell SEO retainers or social-media packages.</p>
  <h2>How a project usually runs</h2>
  <p>It starts with a conversation about the process you need on a computer — not a pitch deck. We look at the tools you already use, write down roles, statuses, documents and reports in language your staff can check, then build a first usable slice. Later versions add the rest. When we hand over, you should have hosting, backups, notes for your team and a way to change the system without starting again.</p>
  <p>Support hours and response times are written into the project. We do not advertise 24/7 cover for every client.</p>
  <h2>What this site does not claim</h2>
  <p>We list systems we have actually built — including the school platform, VayaSA, Fluxmove, Tshira and the municipality platform. We do not publish client counts, awards, partner badges or testimonials we cannot show you. Where a product is still being finished, the case study says so.</p>
  <p>Office: {esc(ADDRESS_LINE)}. Email: {esc(EMAIL)}. Phone: {esc(PHONE_DISPLAY)}.</p>
</div></section>
{cta_band("Talk to a developer", "If the process lives in your heads and in spreadsheets, we can help you put it into software.")}
"""
    emit(
        "about/index.html",
        "About Cyber Developers | Custom Software South Africa",
        "Cyber Developers is a South African custom software development company building business systems, web applications, mobile apps, workflow automation and integrations.",
        "/about/",
        [("/", "Home"), ("/about/", "About")],
        body,
        current="/about/",
    )


def contact_page() -> None:
    body = f"""
<section class="page-hero"><div class="container">
  {crumbs_html([("/", "Home"), ("/contact/", "Contact")])}
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
    rows = []
    for b in blocks:
        href = b[2] if len(b) > 2 else None
        more = f'<span class="more">See the system</span>' if href else ""
        inner = f"<h3>{esc(b[0])}</h3><p>{esc(b[1])}</p>{more}"
        rows.append(f'<a href="{href}">{inner}</a>' if href else f"<article>{inner}</article>")
    body = f"""
<section class="page-hero"><div class="container">
  {crumbs_html([("/", "Home"), ("/industries/", "Industries")])}
  <h1>Software for organisations with real operational complexity</h1>
  <p class="lead">The software is different in each of these places. That is why we list them — not to fill a grid of industries.</p>
</div></section>
<section class="section"><div class="container">
  <nav class="industry-band" aria-label="Sectors">
    <a href="/solutions/school-management-system/">Education</a>
    <a href="/solutions/law-firm-management-software/">Legal</a>
    <a href="/solutions/municipality-management-software/">Government</a>
    <a href="/solutions/logistics-delivery-software/">Logistics</a>
    <a href="/our-work/vayasa/">Transport</a>
    <a href="/industries/">Retail</a>
    <a href="/industries/">Professional services</a>
  </nav>
</div></section>
<section class="section section-alt"><div class="container" style="max-width:48rem">
  <div class="row-list">{''.join(rows)}</div>
</div></section>
{cta_band("Talk about your organisation", "If your sector is not listed, that can still be a fit. Specialised workflows are the work we take.")}
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
