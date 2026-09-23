#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from site_lib import (
    esc, crumbs_html, enquiry_form, faq_html, cta_band,
    service_schema, faq_schema, steps_ol,
)
from generate_core import emit, bullets
from graphics import capabilities_editorial, showcase, shot


def proof_blocks(items: list[dict]) -> str:
    out = []
    for i, it in enumerate(items):
        out.append(
            showcase(
                it["href"],
                it["name"],
                it["kicker"],
                it["copy"],
                it.get("tags", []),
                shot(it["shot"]),
                reverse=i % 2 == 1,
                cta=it.get("cta", "View project"),
            )
        )
    return "".join(out)


def service_page(
    slug,
    nav_title,
    h1,
    title,
    description,
    intro,
    sections,
    faqs,
    extra_schema=None,
):
    canonical = f"/services/{slug}/"
    schema = [service_schema(h1, description, canonical)]
    if faqs:
        schema.append(faq_schema(faqs))
    if extra_schema:
        schema.extend(extra_schema)
    faq_block = ""
    if faqs:
        faq_block = f"""<section class="section section-alt"><div class="container split">
  <div><h2>Questions</h2><p class="muted">If yours is not here, put it on the enquiry form.</p></div>
  {faq_html(faqs)}
</div></section>"""
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
{sections}
{faq_block}
{cta_band("Talk to Our Developers", "Describe the process you want on a computer. We will say whether to build, adapt something we already have, or leave it.", primary=("Discuss Your Project", "/contact/"), secondary=("Request a Consultation", "/contact/"))}
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
        priority="0.85",
    )


def build_services():
    emit(
        "services/index.html",
        "Software Development Services | Cyber Developers South Africa",
        "Custom software, web applications, mobile apps, business systems and workflow automation from a South African software development company.",
        "/services/",
        [("/", "Home"), ("/services/", "Services")],
        f"""
<section class="page-hero"><div class="container">
  {crumbs_html([("/", "Home"), ("/services/", "Services")])}
  <h1>Services</h1>
  <p class="lead">Named pieces of work you can send to a colleague. They overlap on purpose: a school system is custom software, a web application, and often an integration job as well. If you are unsure which label fits, start with custom software or describe the process you want to replace.</p>
</div></section>
{capabilities_editorial(heading=None, section_id="service-list")}
{cta_band("Not sure which service to pick?", "Send the process, the users and the systems you already have. The label can wait.", primary=("Discuss Your Project", "/contact/"))}
""",
        current="/services/",
        priority="0.8",
    )

    service_page(
        "custom-software-development",
        "Custom Software Development",
        "Custom Software Development in South Africa",
        "Custom Software Development South Africa | Cyber Developers",
        "Custom software development in South Africa: business systems, web applications, mobile apps, workflow, integrations and support built around your process.",
        "Custom software is an application built for how your organisation already works — or how it needs to work — rather than forcing the business into a generic product. Cyber Developers is the custom software company that designs that application, connects it to the tools you already use, and stays available after go-live.",
        f"""
<section class="section"><div class="container prose">
  <h2>What custom software development is</h2>
  <p>It is software with named users, records, statuses and reports. Staff capture work in it. Managers trust numbers from it. Customers or partners may log in. That is different from a brochure website, and it is different from an off-the-shelf package that almost fits except for the exceptions that are the real business.</p>
  <p>When people search for a custom software company in South Africa, they usually need developers who can model those exceptions — permissions, documents, billing, field capture — not a theme with a contact form.</p>
  <h2>When custom software makes sense</h2>
  {bullets([
      "Operational work still lives in spreadsheets, paper or WhatsApp groups.",
      "Off-the-shelf software almost fits, but the exceptions are the real business.",
      "Several tools hold overlapping records and nobody trusts a single report.",
      "Staff, customers or field users need different access to the same process.",
      "You already know the process; you need it on a computer with an audit trail.",
  ])}
  <p>If a packaged product already produces the three reports a manager asks for every week, buy it. If a shadow spreadsheet is the real system, you are in custom territory. Read <a href="/knowledge-centre/custom-software-vs-off-the-shelf-software/">custom versus off-the-shelf</a> and <a href="/knowledge-centre/how-much-does-custom-software-development-cost-in-south-africa/">what actually drives cost</a>.</p>
  <h2>What Cyber Developers builds</h2>
  <p>The labels below are the same jobs, described from different angles. A school platform is custom business software, a set of web applications, and an integration project. We do not sell them as unrelated products.</p>
  <h3>Business systems</h3>
  <p>Day-to-day administration: people, cases, money, documents and reporting. See <a href="/services/business-systems/">business systems</a> and examples such as <a href="/our-work/funeral-parlour-system/">Legacy Care</a> and <a href="/our-work/lawyer-management-system/">LawTech SA</a>.</p>
  <h3>Workflow platforms</h3>
  <p>Named stages, owners, SLA checks and finance locks. <a href="/our-work/tshira-workflow-system/">Tshira</a> is the public example; the <a href="/services/workflow-automation/">workflow automation</a> page explains the pattern.</p>
  <h3>Web applications</h3>
  <p>Authenticated portals for staff, customers, parents, citizens or drivers. <a href="/our-work/vayasa/">VayaSA</a>, <a href="/our-work/municipality-platform/">SmartCity Muni</a> and the school portals are web applications with real roles. <a href="/services/web-application-development/">Web application development</a>.</p>
  <h3>Mobile applications</h3>
  <p>Where the user is moving. FluxMove includes an Expo driver app alongside the web marketplace. VayaSA is built to be used on a phone. We do not claim native iOS/Android store apps for every product. <a href="/services/mobile-app-development/">Mobile app development</a>.</p>
  <h3>Integrations</h3>
  <p>Payments, SMS, email, identity checks and existing databases, so information is not retyped. Payment processors used on our platforms include Paystack, Ozow and Capitec Pay where those projects required them. <a href="/services/systems-integration/">Systems integration</a>.</p>
  <h3>Reporting</h3>
  <p>Numbers that come from the same records operators use. Tshira’s reports cover cases, SLA and finance. School platforms produce statements, debtors and report cards from the student file.</p>
  <h3>Authentication and permissions</h3>
  <p>The finance user is not the field user. SchoolHub SA, Tshira, VayaSA and LawTech SA all separate roles on the same data.</p>
  <h3>Deployment and support</h3>
  <p>Hosting, backups, user issues and change requests are part of the work. Hours and response times are written into the project. We do not advertise 24/7 cover for every client.</p>
  <h2>Development process</h2>
</div></section>
<section class="section section-alt"><div class="container">
  {steps_ol([
      ("Discovery", "Users, records, exceptions, integrations and the reports managers actually need."),
      ("Architecture", "A data model and permissions that can survive real work, not only the demo script."),
      ("Interface", "Screens that match the jobs. Operators look at them before the system is frozen."),
      ("Build", "Iterative development against the process, with unhappy paths in the test plan."),
      ("Go-live", "Hosting, backups, accounts and notes for the team."),
      ("Support", "Fixes and change requests after the first week of real use."),
  ])}
</div></section>
<section class="section"><div class="container prose">
  <h2>Technology</h2>
  <p>We choose tools from what we already run in production, not from a trend list. Common stacks on Cyber Developers systems include React, Next.js, TypeScript, Node.js, Python, C# / ASP.NET Core, PostgreSQL, Prisma, Azure, Firebase, Railway and Cloudflare. The school, workflow, logistics and transport products are Next.js and PostgreSQL. SmartCity Muni is a React application. FluxMove’s driver client uses Expo where that module is in play.</p>
  <h2>South African considerations</h2>
  <p>Projects here usually involve ZAR pricing, POPIA-minded records, local payment options, South African identity numbers, and users on mixed office and mobile connections. We have already modelled those constraints on products such as VayaSA, FluxMove and SchoolHub SA. We do not create fake city pages or claim offices we do not have. The company works from 135 Rivonia Road, Sandton, Gauteng, and builds for organisations across South Africa.</p>
</div></section>
<section class="section section-alt" id="work">
  <div class="container">
    <div class="section-intro">
      <h2>Software we have actually built</h2>
      <p class="lead">Proof is the product, not a slogan. These systems are documented on Our Work with screenshots from the live interfaces. We do not invent outcomes, traffic figures or unnamed clients.</p>
    </div>
    {proof_blocks([
        {"href": "/our-work/tshira-workflow-system/", "name": "Tshira Workflow", "kicker": "Workflow platform",
         "copy": "Cases, provincial assignment, field collection, review, SLA monitoring, requisitions, expenses and invoicing.",
         "tags": ["Workflow", "SLA", "Finance"], "shot": "tshira-dashboard"},
        {"href": "/our-work/municipality-platform/", "name": "SmartCity Muni", "kicker": "Citizen services",
         "copy": "Issue reporting, service requests, alerts, emergency information, queue booking, notices, jobs and a business directory.",
         "tags": ["Citizen portal", "Faults", "Queues"], "shot": "smartcity-home"},
        {"href": "/our-work/vayasa/", "name": "VayaSA", "kicker": "Transport marketplace",
         "copy": "Ride sharing, bus tickets and taxi seats, with verification and South African payment options used on that product.",
         "tags": ["Bookings", "Operators", "Payments"], "shot": "vayasa-home"},
        {"href": "/our-work/fluxmove/", "name": "FluxMove", "kicker": "Logistics platform",
         "copy": "Instant quotations, vehicle selection, booking, drivers and business accounts.",
         "tags": ["Quotes", "Vehicles", "Drivers"], "shot": "fluxmove-quote"},
        {"href": "/our-work/lawyer-management-system/", "name": "LawTech SA", "kicker": "Legal practice",
         "copy": "Clients, matters, invoices, fee book, trust accounts and debt collection.",
         "tags": ["Matters", "Trust", "Invoices"], "shot": "lawtech-dashboard"},
        {"href": "/our-work/funeral-parlour-system/", "name": "Legacy Care", "kicker": "Funeral operations",
         "copy": "Members, policies, premium collections, arrears, claims, mortuary, inventory, fleet and finance.",
         "tags": ["Members", "Collections", "Claims"], "shot": "legacy-dashboard"},
        {"href": "/our-work/school-lms/", "name": "School Management System", "kicker": "Education",
         "copy": "Role-based portals for admissions, students, attendance, fees, staff and reporting.",
         "tags": ["Students", "Fees", "Portals"], "shot": "school-portal"},
    ])}
  </div>
</section>
<section class="section"><div class="container prose">
  <h2>Related reading</h2>
  <ul>
    <li><a href="/our-work/">Our Work</a></li>
    <li><a href="/solutions/">Solutions</a></li>
    <li><a href="/knowledge-centre/how-to-choose-a-software-development-company-in-south-africa/">How to choose a software development company in South Africa</a></li>
    <li><a href="/contact/">Contact</a></li>
  </ul>
</div></section>
""",
        [
            ("How long does custom software take?", "It depends on scope. A focused workflow tool and a multi-portal school or logistics platform are different efforts. Discovery produces a realistic sequence rather than a slogan timeline."),
            ("Do you rebuild everything from scratch?", "Not always. If an existing Cyber Developers system is close, we customise it. If the process is unique, we design a new model."),
            ("Will we own the system?", "Project terms are agreed in writing. The usual intent is that you operate a system built for your organisation, with source and hosting arrangements documented for that engagement."),
            ("Do you work only in Johannesburg?", "The office is in Sandton, Gauteng. We build for organisations across South Africa. We do not list fake regional offices."),
        ],
    )

    service_page(
        "business-systems",
        "Business Systems",
        "Custom Business Systems",
        "Business Management Software South Africa | Cyber Developers",
        "Custom business systems for South African organisations: CRM-style records, cases, workflow, billing, documents, stock, reporting, permissions and audit trails.",
        "A business management system is the operational software an organisation runs on: people, customers, money, inventory or cases, with reporting that managers can trust. Cyber Developers builds that software around the file the business already keeps — not as a giant ERP suite dropped on the team.",
        f"""
<section class="section"><div class="container prose">
  <h2>What business systems development covers</h2>
  <p>Staff open the system in the morning and close it at night. If they still keep a parallel spreadsheet, the system is incomplete. Typical operational capabilities, when the process needs them:</p>
  {bullets([
      "CRM-style records for customers, members, students, clients or residents.",
      "Cases or jobs with statuses, owners and history.",
      "Workflow: assignment, approval and handover instead of email chains.",
      "Billing, invoicing, receipts, statements and payment recording.",
      "Documents attached to the record, not to a side chat.",
      "Stock / inventory where the operation holds goods.",
      "Reporting from the same data operators use.",
      "Permissions so finance, operations and frontline users are not the same role.",
      "Audit trails for who changed what.",
      "Notifications when a record needs action.",
      "Integrations to payments, SMS, email or an existing database.",
  ])}
  <p>This is <a href="/services/custom-software-development/">custom software development</a> aimed at daily operations. It is not a marketing website. See also <a href="/knowledge-centre/what-is-a-business-management-system/">what a business management system is</a>.</p>
</div></section>
<section class="section section-alt" id="work">
  <div class="container">
    <div class="section-intro">
      <h2>Systems that already do this work</h2>
      <p class="lead">Screens below are from products we built. We list capabilities that are in those products. We do not invent extra modules or results.</p>
    </div>
    {proof_blocks([
        {"href": "/our-work/tshira-workflow-system/", "name": "Tshira", "kicker": "Cases, workflow, billing",
         "copy": "Client records, case lifecycle, requisitions, expenses, invoicing, SLA reporting, team access and an audit trail.",
         "tags": ["Cases", "Billing", "Audit"], "shot": "tshira-dashboard"},
        {"href": "/our-work/funeral-parlour-system/", "name": "Legacy Care", "kicker": "Members, policies, finance",
         "copy": "Members, policy products, premium collections, arrears, claims, funeral operations, mortuary, inventory, fleet and finance reporting.",
         "tags": ["Members", "Collections", "Inventory"], "shot": "legacy-dashboard"},
        {"href": "/our-work/lawyer-management-system/", "name": "LawTech SA", "kicker": "Practice administration",
         "copy": "Clients, matters, invoices, fee book, trust accounts and debt collection on a shared practice dashboard.",
         "tags": ["Clients", "Matters", "Trust"], "shot": "lawtech-dashboard"},
        {"href": "/our-work/school-lms/", "name": "School Management System", "kicker": "Academics, fees, HR",
         "copy": "Students, guardians, attendance, fees, invoices, HR, communication and reporting behind role-based portals.",
         "tags": ["Students", "Fees", "HR"], "shot": "school-portal"},
    ])}
  </div>
</section>
<section class="section"><div class="container prose">
  <h2>How we design the model</h2>
  <p>We map entities first — person, case, invoice, vehicle, student — then the statuses those records move through. Screens come after the model is honest. That is how a school platform, a workflow system and a funeral business platform stay coherent instead of becoming a pile of forms.</p>
  <p>Related: <a href="/solutions/workflow-management-system/">workflow management</a>, <a href="/solutions/funeral-parlour-management-software/">funeral parlour software</a>, <a href="/solutions/law-firm-management-software/">law firm software</a>, <a href="/solutions/school-management-system/">school management software</a>.</p>
</div></section>
""",
        [
            ("Is this an ERP?", "Sometimes it looks like a small ERP. We do not install a giant suite and hope the modules match. We build the modules the organisation will actually use."),
            ("Can it replace Excel?", "If Excel is the process, a system can replace the fragile parts. We do not pretend every spreadsheet belongs in software on day one."),
            ("Do you have a generic CRM product?", "We build CRMs around the object that matters — a matter, a learner, a member, a ticket. See custom CRM if the noun is not a standard lead."),
        ],
    )

    service_page(
        "web-application-development",
        "Web Application Development",
        "Web Application Development",
        "Web Application Development South Africa | Cyber Developers",
        "Web application development in South Africa: operational portals, dashboards and browser-based business systems with real users, permissions and data.",
        "A web application is software that runs in the browser with real users, permissions and data — administration portals, customer access, citizen services or internal operations. Cyber Developers builds those applications as the working surface of a business system, not as a marketing site with a login afterthought.",
        f"""
<section class="section"><div class="container prose">
  <h2>What we mean by a web application</h2>
  <p>Accounts. Roles. Queues. Records. Documents. Reports. If a page cannot capture work, it is a website. The products below are web applications: VayaSA’s passenger and operator consoles, SmartCity Muni’s citizen services, FluxMove’s booking and provider hub, and the school, legal and funeral portals.</p>
  {bullets([
      "Authenticated portals for staff, customers, parents, citizens, drivers or operators.",
      "Operational screens: queues, records, documents, invoices and reports.",
      "Responsive interfaces used on typical office and mobile browsers.",
      "API backends and PostgreSQL data models on the Next.js products; SmartCity Muni is a React application.",
  ])}
</div></section>
<section class="section section-alt"><div class="container">
  <div class="section-intro">
    <h2>Examples from Our Work</h2>
    <p class="lead">Each of these is a browser-based product with more than one role on the same data.</p>
  </div>
  {proof_blocks([
      {"href": "/our-work/vayasa/", "name": "VayaSA", "kicker": "Passenger and operator web app",
       "copy": "Search, booking, operator onboarding and admin review in the browser.",
       "tags": ["Search", "Tickets", "Roles"], "shot": "vayasa-search"},
      {"href": "/our-work/municipality-platform/", "name": "SmartCity Muni", "kicker": "Citizen web application",
       "copy": "Services directory, fault reporting, alerts, queues and emergency information.",
       "tags": ["Services", "Reporting", "Alerts"], "shot": "smartcity-services"},
      {"href": "/our-work/fluxmove/", "name": "FluxMove", "kicker": "Booking and provider hub",
       "copy": "Instant quotes, vehicle selection and delivery booking for customers and providers.",
       "tags": ["Quotes", "Booking"], "shot": "fluxmove-hero"},
      {"href": "/our-work/school-lms/", "name": "School portals", "kicker": "Multi-role web system",
       "copy": "Separate portals for administrators, teachers, learners and parents against one student record.",
       "tags": ["Portals", "Roles"], "shot": "school-portal"},
  ])}
</div></section>
<section class="section"><div class="container prose">
  <p>Web application development sits next to <a href="/services/custom-software-development/">custom software</a> and <a href="/services/mobile-app-development/">mobile apps</a>. Many products launch in the browser and add a store app only when the job needs device features.</p>
</div></section>
""",
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
        "Mobile app development in South Africa for field work, drivers and customers — as a client of the same business system, not a second product.",
        "Mobile applications are appropriate when the user is moving — drivers, field officers, parents, customers — and needs a focused interface rather than a full desktop system. We only claim the mobile technologies we have actually used on a project.",
        f"""
<section class="section"><div class="container prose">
  <h2>What we actually ship on mobile</h2>
  <p><a href="/our-work/fluxmove/">FluxMove</a> includes an optional Expo driver app for on-the-road workflow (jobs, status, proof) alongside the Next.js web platform. <a href="/our-work/vayasa/">VayaSA</a> is a passenger and operator product built to work on a phone in the browser; we do not list a separate native store app for it on this site. Other systems — school portals, Tshira, SmartCity Muni — are used on mobile browsers where that is how staff work.</p>
  <p>We decide Expo, responsive web, or a later store listing based on the job, offline needs and budget. We do not advertise Swift or Kotlin native apps we have not shipped on a named product here.</p>
  <h2>How the mobile surface should work</h2>
  {bullets([
      "Same business rules as the web system — not a second source of truth.",
      "Role-specific jobs: driver, customer, officer.",
      "Status updates, and photo or document capture where the process needs it.",
      "A web console for the staff who are not in the field.",
  ])}
  <p>Cost follows platforms, backend and integrations — not a national average. See <a href="/knowledge-centre/what-does-it-cost-to-build-a-mobile-app-in-south-africa/">mobile app cost factors</a>.</p>
</div></section>
<section class="section section-alt"><div class="container">
  {proof_blocks([
      {"href": "/our-work/fluxmove/", "name": "FluxMove driver workflow", "kicker": "Expo module + web platform",
       "copy": "Customers quote and book on the web. Drivers can use a mobile module for on-the-road steps.",
       "tags": ["Expo", "Drivers", "Quotes"], "shot": "fluxmove-vehicles"},
      {"href": "/our-work/vayasa/", "name": "VayaSA on a phone", "kicker": "Mobile-ready web application",
       "copy": "Passengers search ride shares, bus tickets and taxi seats from a phone-sized interface.",
       "tags": ["Search", "Tickets"], "shot": "vayasa-home"},
  ])}
</div></section>
""",
        [
            ("Do we need iOS and Android on day one?", "Not always. Many products launch with a responsive web app and add an Expo or store client when the workflow needs device features or a listing."),
            ("What does a mobile app cost?", "Cost follows features, platforms and integrations. Use the Knowledge Centre article, then request a scoped conversation."),
        ],
    )

    service_page(
        "workflow-automation",
        "Workflow Automation",
        "Workflow Automation",
        "Workflow Automation South Africa | Cyber Developers",
        "Workflow automation in South Africa: manual handovers become structured cases with assignment, approval, SLA monitoring, reporting and an audit trail.",
        "Workflow automation is software that moves work through named stages, owners and checks. It is not a pile of disconnected notifications. The Tshira workflow system is the clearest public example Cyber Developers can show.",
        f"""
<section class="section"><div class="container">
  <div class="section-intro">
    <h2>From a manual process to a system</h2>
    <p class="lead">The sequence is ordinary. Most organisations already do it in email. The software makes each step visible.</p>
  </div>
  {steps_ol([
      ("Manual process", "Work arrives in inboxes, spreadsheets and WhatsApp groups. Nobody can see where a case is stuck."),
      ("Structured workflow", "The case becomes a record with a status, documents and a history."),
      ("Assignment", "A named owner receives it — by team, province or queue."),
      ("Approval", "Quality checks, consultancy or review happen before the record may move."),
      ("SLA monitoring", "Coordinators can see what is overdue instead of discovering it in a meeting."),
      ("Reporting", "Cases, finance and workload come from the same system."),
      ("Audit trail", "Who changed the case, and when, stays with the record."),
  ])}
</div></section>
<section class="section section-alt"><div class="container page-hero-grid">
  <div class="prose">
    <h2>Tshira as proof</h2>
    <p>A case is received, assigned by province, collected in the field, checked, reviewed and only then invoiced. Requisitions happen before spending; expenses are claimed afterwards. Finance is locked until the work is ready.</p>
    <p>That pattern — statuses, owners, documents, finance locks — is what we mean by business process automation. It can be adapted to other case-based organisations. It is not robotic process automation that clicks through someone else’s screens.</p>
    <p><a href="/our-work/tshira-workflow-system/">Tshira case study</a> · <a href="/solutions/workflow-management-system/">Workflow management system</a> · <a href="/knowledge-centre/how-workflow-automation-can-reduce-manual-admin/">How workflow automation reduces manual admin</a></p>
  </div>
  <aside class="page-hero-visual">{shot("tshira-dashboard")}</aside>
</div></section>
<section class="section"><div class="container">
  <h2>Reports from the same records</h2>
  {shot("tshira-reports")}
</div></section>
""",
        [
            ("Is this RPA?", "Not in the sense of scraping someone else’s screens. We automate your process inside a system you control."),
            ("Can AI sit on this workflow?", "Yes, as a later capability: classification, drafting or extraction, with a person still responsible for the stage that matters. See AI and business automation."),
        ],
    )

    service_page(
        "ai-business-automation",
        "AI & Business Automation",
        "AI & Business Automation",
        "AI & Business Automation | Cyber Developers South Africa",
        "Practical AI and business automation inside custom software: assistants, document processing, workflow, reporting and API integrations.",
        "AI is useful when it sits inside a real business process — answering from your documents, extracting fields, routing work, or drafting a report a person still checks. It is not a substitute for a data model, permissions or an audit trail.",
        f"""
<section class="section"><div class="container prose">
  <h2>Where this belongs</h2>
  <p>Start with the system of record. Add automation where a person currently copies, searches or restates the same information. Keep a named owner for anything that affects a customer, a student, a citizen or a payment. <a href="/services/workflow-automation/">Workflow automation</a> is usually the substrate; a model is a component.</p>
  {bullets([
      "Internal knowledge assistants constrained to your content.",
      "Document processing: classification, extraction, routing.",
      "Customer-service automation with a human handover.",
      "Workflow automation and API integrations.",
      "Scheduled or on-demand reporting from system data.",
      "AI features embedded in a custom application, not a disconnected chatbot.",
  ])}
  <p>Related: <a href="/our-work/tshira-workflow-system/">Tshira</a> as a structured workflow automation can sit on, and <a href="/services/custom-software-development/">custom software development</a> as the system it should live inside.</p>
</div></section>
""",
        [
            ("Will you label everything as AI-powered?", "No. If a filter or a template solves it, we say so."),
            ("Do you train a private model on our data by default?", "Not by default. Many useful assistants retrieve from your documents at query time. Training or fine-tuning is a separate, explicit decision."),
            ("Is AI the company’s identity?", "No. Cyber Developers is a software company. AI is one capability among systems, apps and integrations."),
        ],
    )

    service_page(
        "systems-integration",
        "Systems Integration",
        "Systems Integration",
        "Systems Integration | Cyber Developers South Africa",
        "Software integration for South African businesses: payments, SMS, identity, APIs and existing databases connected to custom systems.",
        "Integration means your custom system can send and receive data from the tools you already depend on — payments, messaging, identity checks, accounting or sector platforms — without retyping.",
        f"""
<section class="section"><div class="container prose">
  <h2>What we connect</h2>
  {bullets([
      "REST APIs, webhooks and signed callbacks.",
      "Payment providers used on our platforms include Paystack, Ozow and Capitec Pay where those projects required them; PayFast, Yoco and similar can be scoped when needed.",
      "Email and SMS (for example SendGrid and Twilio on the school platform).",
      "SA ID verification where a product requires it.",
      "Imports such as SA-SAMS-oriented school data where that module exists.",
      "Cloud storage and DNS (Cloudflare, object storage) as used in production systems.",
  ])}
  <p>We integrate against documented APIs, verify signatures, and keep secrets on the server. Each integration is tested against failure: timeouts, duplicate webhooks, and users abandoning checkout.</p>
  <p>Examples: <a href="/our-work/vayasa/">VayaSA</a> (payments, SMS OTP, ID verification) and the <a href="/our-work/school-lms/">school platform</a> (email, SMS, payments, backup).</p>
</div></section>
""",
        [
            ("Can you connect to our existing SQL database?", "Often yes. We need access rules and a clear owner for writes. We do not silently overwrite a live production database."),
            ("Do you resell Microsoft or AWS partnerships?", "No. We use the cloud and tools the project needs. We do not advertise partnerships we do not have."),
        ],
    )


if __name__ == "__main__":
    build_services()
    print("services done")
