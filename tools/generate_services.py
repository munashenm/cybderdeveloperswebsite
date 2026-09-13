#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from site_lib import (
    esc, crumbs_html, enquiry_form, faq_html,
    service_schema, faq_schema,
)
from generate_core import emit, bullets, cards
from graphics import capabilities_editorial


def service_page(slug, nav_title, h1, title, description, intro, problems, capabilities, approach, techs, projects, faqs, extra_body=""):
    canonical = f"/services/{slug}/"
    schema = [service_schema(h1, description, canonical), faq_schema(faqs)]
    proj = "".join(
        f'<li><a href="{p[1]}">{esc(p[0])}</a> — {esc(p[2])}</li>' for p in projects
    )
    body = f"""
<section class="page-hero"><div class="container">
  {crumbs_html([("/", "Home"), ("/services/", "Services"), (canonical, nav_title)])}
  <h1>{esc(h1)}</h1>
  <p class="lead">{esc(intro)}</p>
  <div class="hero-actions">
    <a class="btn btn-primary" href="/contact/">Discuss Your Project</a>
    <a class="btn btn-secondary" href="/our-work/">View Our Work</a>
  </div>
</div></section>
<section class="section"><div class="container prose">
  <h2>Where this usually comes from</h2>
  {bullets(problems)}
  <h2>What we typically deliver</h2>
  {bullets(capabilities)}
  <h2>How we work</h2>
  <p>{esc(approach)}</p>
  {extra_body}
  <p class="tech-inline">Tools used on this kind of work: {" · ".join(esc(t) for t in techs)}</p>
  <h2>Related systems</h2>
  <ul>{proj}</ul>
</div></section>
<section class="section section-alt"><div class="container split">
  <div><h2>Questions</h2><p class="muted">If yours is not here, put it on the enquiry form.</p></div>
  {faq_html(faqs)}
</div></section>
"""
    emit(
        f"services/{slug}/index.html",
        title,
        description,
        canonical,
        [("/", "Home"), ("/services/", "Services"), (canonical, nav_title)],
        body,
        extra=schema,
        current="/services/",
        priority="0.8",
    )


def build_services():
    emit(
        "services/index.html",
        "Software Development Services | Cyber Developers South Africa",
        "Custom software, web applications, mobile apps, business systems, workflow automation, AI integrations and systems integration from Cyber Developers.",
        "/services/",
        [("/", "Home"), ("/services/", "Services")],
        f"""
<section class="page-hero"><div class="container">
  {crumbs_html([("/", "Home"), ("/services/", "Services")])}
  <h1>Services</h1>
  <p class="lead">Named pieces of work you can send to a colleague. They overlap on purpose: a school system is custom software, a web application, and often an integration job as well. If you are unsure which label fits, start with custom software or describe the process you want to replace.</p>
</div></section>
{capabilities_editorial().replace('id="services"', 'id="service-list"')}
""",
        current="/services/",
        priority="0.8",
    )

    service_page(
        "custom-software-development",
        "Custom Software Development",
        "Custom Software Development",
        "Custom Software Development South Africa | Cyber Developers",
        "Custom software development for South African organisations. Systems designed around your process, roles, data and reporting.",
        "Custom software is an application built for how your organisation already works — or how it needs to work — rather than forcing the business into a generic product.",
        [
            "Operational work still lives in spreadsheets, paper or WhatsApp groups.",
            "Off-the-shelf software almost fits, but the exceptions are the real business.",
            "Several tools hold overlapping records and nobody trusts a single report.",
            "Staff, customers or field users need different access to the same process.",
        ],
        [
            "Role-based access and audit-friendly activity history.",
            "Records, documents, statuses and reporting modelled on the real process.",
            "Web portals, and mobile apps where the work is not at a desk.",
            "Integrations to payments, SMS, identity or existing databases.",
            "Deployment, backups and ongoing change after go-live.",
        ],
        "We start with discovery: users, records, exceptions and integrations. Architecture and interface follow the process. Development is iterative so operators can react before the system is frozen. Testing covers the unhappy paths — failed payments, missing documents, permission edges — not only the demo script.",
        ["React", "Next.js", "TypeScript", "Node.js", "C#", "Python", "PostgreSQL", "Azure", "APIs"],
        [
            ("School / College LMS", "/our-work/school-lms/", "multi-role education system"),
            ("Tshira Workflow System", "/our-work/tshira-workflow-system/", "multi-province case workflow"),
            ("VayaSA", "/our-work/vayasa/", "transport marketplace"),
        ],
        [
            ("How long does custom software take?", "It depends on scope. A focused workflow tool and a multi-portal school or logistics platform are different efforts. Discovery produces a realistic sequence rather than a slogan timeline."),
            ("Do you rebuild everything from scratch?", "Not always. If an existing Cyber Developers system is close, we customise it. If the process is unique, we design a new model."),
            ("Will we own the system?", "Project terms are agreed in writing. The usual intent is that you operate a system built for your organisation, with source and hosting arrangements documented for that engagement."),
        ],
    )

    service_page(
        "web-application-development",
        "Web Application Development",
        "Web Application Development",
        "Web Application Development South Africa | Cyber Developers",
        "Web application development for South African organisations: operational portals, dashboards and browser-based business systems.",
        "A web application is software that runs in the browser with real users, permissions and data — administration portals, customer access, citizen services or internal operations.",
        [
            "A website cannot capture work, only describe the company.",
            "Teams need dashboards, queues and records, not a contact form.",
            "Users in different roles must see different slices of the same data.",
        ],
        [
            "Authenticated portals for staff, customers, parents, citizens or drivers.",
            "Operational screens: queues, records, documents, invoices and reports.",
            "Responsive interfaces that remain usable on typical office and mobile browsers.",
            "API backends and PostgreSQL or SQL Server data models.",
        ],
        "We design the information architecture first so navigation matches jobs to be done. Then we implement the application with a modern React/Next.js front end where that stack is the right fit, or a focused React SPA when the product is already structured that way.",
        ["React", "Next.js", "TypeScript", "JavaScript", "PostgreSQL", "Prisma", "APIs"],
        [
            ("Municipality Platform", "/our-work/municipality-platform/", "citizen and admin web app"),
            ("Fluxmove", "/our-work/fluxmove/", "booking and driver hub"),
            ("School / College LMS", "/our-work/school-lms/", "multiple web portals"),
        ],
        [
            ("Is this the same as web design?", "No. Visual design matters, but a web application is a working system with accounts, data and workflow."),
            ("Can it work on mobile browsers?", "Yes. Many of our systems are used on phones in the field even when a native app is not the first release."),
        ],
    )

    service_page(
        "mobile-app-development",
        "Mobile App Development",
        "Mobile App Development",
        "Mobile App Development South Africa | Cyber Developers",
        "Mobile app development for South African businesses: field operations, drivers, customers and on-the-go administration.",
        "Mobile applications are appropriate when the user is moving — drivers, field officers, parents, customers — and needs a focused interface rather than a full desktop system.",
        [
            "Staff capture work away from the office and data never comes back cleanly.",
            "Drivers or field teams need availability, jobs, navigation and proof of work.",
            "Customers expect booking, tickets or tracking on a phone.",
        ],
        [
            "Role-specific mobile experiences (driver, customer, officer).",
            "Job lists, status updates, document or photo capture where the process needs it.",
            "Integration with the same backend the web application uses.",
            "Where used on a project: Expo-based driver apps alongside a Next.js platform.",
        ],
        "We decide native, Expo or responsive web based on the job, offline needs and budget. The mobile surface should be a client of the same business rules as the web system, not a second product with a second source of truth.",
        ["React", "TypeScript", "JavaScript", "APIs", "PostgreSQL", "Firebase"],
        [
            ("Fluxmove", "/our-work/fluxmove/", "driver mobile app alongside the web platform"),
            ("VayaSA", "/our-work/vayasa/", "passenger and operator mobile-ready product"),
        ],
        [
            ("Do we need iOS and Android on day one?", "Not always. Many products launch with a responsive web app and add a native or Expo client when the workflow needs device features or a store listing."),
            ("What does a mobile app cost?", "Cost follows features, platforms and integrations. See the Knowledge Centre article on mobile app cost factors, then request a scoped conversation."),
        ],
    )

    service_page(
        "business-systems",
        "Business Systems",
        "Business Management Systems",
        "Business Software Development South Africa | Cyber Developers",
        "Business management systems for South African organisations: records, finance, people, customers and day-to-day operations.",
        "A business management system is the operational software an organisation runs on: people, customers, money, inventory or cases, with reporting that managers can trust.",
        [
            "Finance, operations and customer data live in different files.",
            "Managers cannot see workload, debtors or outstanding work without assembling a spreadsheet.",
            "Staff need self-service for leave, payslips or assigned work.",
        ],
        [
            "Ledgers, invoices, receipts, statements and payment recording.",
            "HR-style records: staff, leave, payslips and attendance where the product includes them.",
            "Customer or student or resident master data with history.",
            "Permissions so finance, operations and frontline users are not the same role.",
        ],
        "We map entities first — person, case, invoice, vehicle, student — then the statuses those records move through. Screens come after the model is honest. That is how a school platform, a workflow system and a municipal billing module stay coherent.",
        ["Next.js", "TypeScript", "PostgreSQL", "C#", "Python", "APIs"],
        [
            ("School / College LMS", "/our-work/school-lms/", "finance, HR, academics and communication"),
            ("Lawyer Management System", "/our-work/lawyer-management-system/", "practice administration"),
            ("Funeral parlour software", "/solutions/funeral-parlour-management-software/", "sector-specific operations"),
        ],
        [
            ("Is this an ERP?", "Sometimes it looks like a small ERP. We do not install a giant suite and hope the modules match. We build the modules the organisation will actually use."),
            ("Can it replace Excel?", "If Excel is the process, a system can replace the fragile parts. We do not pretend every spreadsheet belongs in software on day one."),
        ],
    )

    service_page(
        "workflow-automation",
        "Workflow Automation",
        "Workflow Automation",
        "Business Process Automation South Africa | Cyber Developers",
        "Workflow automation for South African organisations: cases, approvals, field collection, review and billing instead of manual handovers.",
        "Workflow automation is software that moves work through named stages, owners and checks. It is not a pile of disconnected notifications.",
        [
            "Handovers live in email and nobody can see where a case is stuck.",
            "Field capture, review and head-office approval are different teams with no shared status.",
            "Invoices go out before work is actually complete, or long after.",
        ],
        [
            "Explicit statuses and role permissions.",
            "Assignment by team, province or queue.",
            "Documents, forms and history attached to the case.",
            "Requisitions, expenses and invoicing tied to completion rules where the process needs them.",
        ],
        "The Tshira workflow system is the clearest public example: a case moves from intake through provincial assignment, data collection, quality checks, consultancy, review, invoicing and closure, with finance locked until the work is ready.",
        ["Next.js", "TypeScript", "PostgreSQL", "Prisma", "APIs"],
        [
            ("Tshira Workflow System", "/our-work/tshira-workflow-system/", "end-to-end case workflow"),
            ("Workflow management solution", "/solutions/workflow-management-system/", "product page"),
        ],
        [
            ("Is this RPA?", "Not in the sense of scraping someone else’s screens. We automate your process inside a system you control."),
            ("Can AI sit on this workflow?", "Yes, as a later capability: classification, drafting or extraction, with a person still responsible for the stage that matters."),
        ],
    )

    service_page(
        "ai-business-automation",
        "AI & Business Automation",
        "AI & Business Automation",
        "AI & Business Automation | Cyber Developers South Africa",
        "Practical AI and business automation inside custom software: assistants, document processing, workflow, reporting and API integrations.",
        "AI is useful when it sits inside a real business process — answering from your documents, extracting fields, routing work, or drafting a report a person still checks. It is not a substitute for a data model, permissions or an audit trail.",
        [
            "Staff spend hours searching policies, past cases or internal documents.",
            "Incoming PDFs and forms are retyped into the system.",
            "The same customer questions repeat, but answers must stay inside approved information.",
            "Managers want regular reports that still require a manual export.",
        ],
        [
            "Internal knowledge assistants constrained to your content.",
            "Document processing: classification, extraction, routing.",
            "Customer-service automation with a human handover.",
            "Workflow automation and API integrations.",
            "Scheduled or on-demand reporting from system data.",
            "AI features embedded in a custom application, not a disconnected chatbot.",
        ],
        "We treat models and APIs as components. The product remains your application: users, roles, logs and source data. If a task does not need a model, we use ordinary automation. If it does, we bound it — which collection it may read, what it may write, and who approves the result.",
        ["Python", "TypeScript", "Node.js", "APIs", "PostgreSQL", "Azure"],
        [
            ("Tshira Workflow System", "/our-work/tshira-workflow-system/", "structured workflow that automation can sit on"),
            ("Custom software", "/services/custom-software-development/", "the system AI should live inside"),
        ],
        [
            ("Will you label everything as AI-powered?", "No. If a filter or a template solves it, we say so."),
            ("Do you train a private model on our data by default?", "Not by default. Many useful assistants retrieve from your documents at query time. Training or fine-tuning is a separate, explicit decision."),
            ("Is AI the company’s identity?", "No. Cyber Developers is a software company. AI is one capability among systems, apps and integrations."),
        ],
        extra_body="""<h2>Where this belongs</h2>
        <p>Start with the system of record. Add automation where a person currently copies, searches or restates the same information. Keep a named owner for anything that affects a customer, a student, a citizen or a payment.</p>""",
    )

    service_page(
        "systems-integration",
        "Systems Integration",
        "Systems Integration",
        "Systems Integration | Cyber Developers South Africa",
        "Software integration for South African businesses: payments, SMS, identity, APIs and existing databases connected to custom systems.",
        "Integration means your custom system can send and receive data from the tools you already depend on — payments, messaging, identity checks, accounting or sector platforms — without retyping.",
        [
            "Payments happen off-system and are reconciled by hand.",
            "SMS or email notices are sent from a separate console.",
            "Identity, licensing or sector databases are copied into spreadsheets.",
        ],
        [
            "REST APIs, webhooks and signed callbacks.",
            "Payment providers used on our platforms include Paystack, Ozow and Capitec Pay where those projects required them; PayFast, Yoco and similar can be scoped when needed.",
            "Email and SMS (for example SendGrid and Twilio on the school platform).",
            "SA ID verification where a product requires it.",
            "Imports such as SA-SAMS-oriented school data where that module exists.",
            "Cloud storage and DNS (Cloudflare, object storage) as used in production systems.",
        ],
        "We integrate against documented APIs, verify signatures, and keep secrets on the server. We do not paste keys into the browser. Each integration is tested against failure: timeouts, duplicate webhooks, and users abandoning checkout.",
        ["APIs", "Node.js", "TypeScript", "C#", "Python", "PostgreSQL", "Azure", "Cloudflare"],
        [
            ("VayaSA", "/our-work/vayasa/", "payments, SMS OTP, ID verification"),
            ("School / College LMS", "/our-work/school-lms/", "email, SMS, payments, backup"),
        ],
        [
            ("Can you connect to our existing SQL database?", "Often yes. We need access rules and a clear owner for writes. We do not silently overwrite a live production database."),
            ("Do you resell Microsoft or AWS partnerships?", "No. We use the cloud and tools the project needs. We do not advertise partnerships we do not have."),
        ],
    )


if __name__ == "__main__":
    build_services()
    print("services done")
