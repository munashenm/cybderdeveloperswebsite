#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path
from datetime import date

sys.path.insert(0, str(Path(__file__).resolve().parent))
from site_lib import (
    ROOT, SITE, TECHS, ORG_DESC, EMAIL, PHONE_DISPLAY, PHONE_E164, ADDRESS_LINE,
    icon, esc, render_page, write_page, redirect_page, crumbs_html, cta_band,
    enquiry_form, faq_html, service_schema, faq_schema, article_schema,
)
from graphics import (
    hero_stage, tech_banner, selected_work, capabilities_editorial,
    architecture, engineering_matrix, industries_band, process_flow,
    school_map, lawyer_map, funeral_map, industry_block, shot_stack, shot,
)

TODAY = date.today().isoformat()
SITEMAP_URLS: list[tuple[str, str, str]] = []
SKIP_SITEMAP = {"/404.html", "/contact/thank-you/"}


def add_url(canonical: str, priority: str = "0.7", lastmod: str | None = None) -> None:
    if canonical in SKIP_SITEMAP:
        return
    SITEMAP_URLS.append((canonical, priority, lastmod or TODAY))


def emit(
    rel,
    title,
    description,
    canonical,
    crumbs,
    body,
    extra=None,
    current=None,
    image="/assets/img/og-default.webp",
    og_type="website",
    priority="0.7",
    indexable=True,
    lastmod=None,
):
    robots = "index,follow,max-image-preview:large" if indexable else "noindex,follow"
    html = render_page(
        rel, title, description, canonical, crumbs, body, extra, og_type, image, current, robots
    )
    write_page(rel, html)
    if indexable:
        add_url(canonical, priority, lastmod)


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
    <p class="lead">Cyber Developers is a custom software development company in South Africa. We design and build business systems, web applications and mobile apps around how organisations actually work — not around a generic product.</p>
    <div class="hero-actions">
      <a class="btn btn-primary btn-lg" href="/contact/" data-track="consultation_requested" data-track-location="hero">Discuss Your Project</a>
      <a class="btn btn-secondary btn-lg" href="/our-work/">View Our Work</a>
    </div>
    <p class="hero-note">If the work still lives in spreadsheets, paper files or three disconnected tools, that is usually the brief.</p>
  </div>
  <aside>{hero_stage()}</aside>
</div></section>
{tech_banner()}
{capabilities_editorial()}
{selected_work()}
{architecture()}
{engineering_matrix()}
{industries_band()}
{process_flow()}
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
        "Custom Software Development Company South Africa | Cyber Developers",
        "Cyber Developers builds custom software, business systems, web applications and mobile apps for organisations across South Africa. Discuss your project.",
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
        "About Cyber Developers | Custom Software Company South Africa",
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
      <p><span>Address</span>135 Rivonia Road<br>Sandton<br>Gauteng<br>South Africa</p>
    </div>
  </div>
  {enquiry_form("project_enquiry", "New project enquiry | Cyber Developers", "Discuss Your Project")}
</div></section>
"""
    emit(
        "contact/index.html",
        "Contact Cyber Developers | Discuss Your Project",
        "Request a consultation with Cyber Developers in Sandton, South Africa. Enquire about custom software, business systems, web apps or mobile apps.",
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
  <p class="lead">Thank you. We will review what you sent and respond by email. If the matter is urgent, call {PHONE_DISPLAY}.</p>
  <p style="margin-top:1.5rem" class="hero-actions">
    <a class="btn btn-primary" href="mailto:{EMAIL}" data-track="email_clicked">Email us</a>
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
        indexable=False,
    )


def industries_page() -> None:
    body = f"""
<section class="page-hero"><div class="container">
  {crumbs_html([("/", "Home"), ("/industries/", "Industries")])}
  <h1>Do we understand your industry?</h1>
  <p class="lead">Each of these sectors has its own records, approvals and public-facing work. We have already built software in these operating environments — not a generic admin theme with a new logo.</p>
  <div class="hero-actions">
    <a class="btn btn-primary" href="/contact/">Discuss Your Project</a>
    <a class="btn btn-secondary" href="/our-work/">See the software</a>
  </div>
</div></section>
<section class="section"><div class="container">
  <nav class="industry-band reveal" aria-label="Sectors">
    <a href="#government">Government</a>
    <a href="#education">Education</a>
    <a href="#legal">Legal</a>
    <a href="#funeral">Funeral</a>
    <a href="#transport">Transport</a>
    <a href="#logistics">Logistics</a>
    <a href="#enterprise">Enterprise</a>
  </nav>
</div></section>
<section class="section section-alt" id="government"><div class="container">
  {industry_block("/solutions/municipality-management-software/", "Government & Municipalities", "SmartCity Muni",
                 "Residents still phone, queue or arrive in person for faults, bills and appointments that a verified account could track. Staff then reconstruct the same request in a back office.",
                 "We digitise citizen service portals, municipal fault reporting, request tracking, emergency information, alerts and notices, queue booking, tenders and local business directories — so the public channel and the operations desk share one record.",
                 shot_stack("smartcity-home", "smartcity-report"),
                 extra_links=[("View SmartCity", "/our-work/municipality-platform/")])}
</div></section>
<section class="section" id="education"><div class="container">
  {industry_block("/solutions/school-management-system/", "Education", "Schools, colleges and TVETs",
                 "A school cannot answer a simple question when academics, fees, attendance and parent communication live in different tools. Staff invent spreadsheets to close the gaps.",
                 "We digitise admissions, student records, attendance, marks, timetables, staff administration, finance and reporting behind role-based portals for administrators, teachers and learners.",
                 school_map(), reverse=True,
                 extra_links=[("View school platform", "/our-work/school-lms/")])}
</div></section>
<section class="section section-alt" id="legal"><div class="container">
  {industry_block("/solutions/law-firm-management-software/", "Legal", "Law firms and practices",
                 "Practice work fails operationally when clients, matters, invoices and trust money sit in different places, and when every user has the same access.",
                 "We digitise client files, matters, fee books, invoicing, trust accounting, debt recovery and the workflow around a matter — with permissions that match how a firm actually staffs a file.",
                 lawyer_map(),
                 extra_links=[("View LawTech SA", "/our-work/lawyer-management-system/")])}
</div></section>
<section class="section" id="funeral"><div class="container">
  {industry_block("/solutions/funeral-parlour-management-software/", "Funeral Services", "Funeral parlours and societies",
                 "Funeral businesses combine member policies, premium collection, claims, mortuary work and vehicles. Off-the-shelf tools rarely match that file.",
                 "We digitise member management, policy products, premium collections, arrears, claims, funeral operations, mortuary records, inventory, fleet and finance reporting.",
                 funeral_map(), reverse=True,
                 extra_links=[("View Legacy Care", "/our-work/funeral-parlour-system/")])}
</div></section>
<section class="section section-alt" id="transport"><div class="container">
  {industry_block("/our-work/vayasa/", "Transport & Mobility", "Intercity passenger movement",
                 "Intercity travel in South Africa mixes private cars, bus operators and taxi associations. Passengers cannot see seats, operators cannot see bookings, and payments are inconsistent.",
                 "We digitise ride sharing, bus ticketing, taxi seat bookings, driver and operator onboarding, and customer accounts on one marketplace.",
                 shot_stack("vayasa-home", "vayasa-search"),
                 extra_links=[("View VayaSA", "/our-work/vayasa/")])}
</div></section>
<section class="section" id="logistics"><div class="container">
  {industry_block("/solutions/logistics-delivery-software/", "Logistics & Delivery", "Freight and household moves",
                 "Moving goods usually means phoning around for a vehicle. Price, distance, vehicle type and who is allowed to take the job stay in someone’s head.",
                 "We digitise live quotation, vehicle selection, booking, driver and provider onboarding, delivery management and business accounts.",
                 shot("fluxmove-quote"), reverse=True,
                 extra_links=[("View FluxMove", "/our-work/fluxmove/")])}
</div></section>
<section class="section section-alt" id="enterprise"><div class="container">
  {industry_block("/solutions/workflow-management-system/", "Enterprise / Professional Services", "Internal operations",
                 "Head office, branches and field staff lose case status in email. Finance invoices unfinished work because there is no hard rule in the system.",
                 "We digitise workflow, case management, SLA tracking, requisitions, billing, expenses, team access, audit trails and management reporting — the kind of internal software an operations team actually lives in.",
                 shot("tshira-dashboard"),
                 extra_links=[("View Tshira", "/our-work/tshira-workflow-system/")])}
</div></section>
{cta_band("If your sector is not listed, that can still be a fit.", "Specialised workflows are the work we take. Describe the process and we will say whether we have built something close.", primary=("Discuss Your Project", "/contact/"))}
"""
    emit(
        "industries/index.html",
        "Industries | Custom Software for South African Organisations",
        "Cyber Developers builds software for government, education, legal, funeral, transport, logistics and enterprise operations in South Africa.",
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
        indexable=False,
    )


if __name__ == "__main__":
    homepage()
    about_page()
    contact_page()
    industries_page()
    privacy_page()
    not_found()
    print("core pages done", len(SITEMAP_URLS))
