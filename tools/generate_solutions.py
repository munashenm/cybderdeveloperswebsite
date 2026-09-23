#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from site_lib import crumbs_html, enquiry_form, faq_html, service_schema, faq_schema, esc, cta_band
from generate_core import emit, bullets
from graphics import (
    school_map, lawyer_map, funeral_map, tshira_map, municipality_map,
    fluxmove_map, crm_map, feature_block, shot, shot_stack, shot_gallery, SHOTS,
)


def og_for(key: str) -> str:
    return f"/assets/img/projects/{SHOTS[key]['file']}"


SOL_VISUAL = {
    "school-management-system": school_map,
    "law-firm-management-software": lawyer_map,
    "funeral-parlour-management-software": funeral_map,
    "workflow-management-system": tshira_map,
    "municipality-management-software": municipality_map,
    "logistics-delivery-software": fluxmove_map,
    "custom-crm-development": crm_map,
}


def solution_page(
    slug,
    name,
    h1,
    title,
    description,
    intro,
    capabilities,
    notes,
    faqs,
    related,
    cta="Request a Consultation",
    gallery=None,
    og=None,
):
    canonical = f"/solutions/{slug}/"
    rel_work = "".join(f'<li><a href="{u}">{esc(n)}</a></li>' for n, u in related)
    vis_fn = SOL_VISUAL.get(slug)
    vis = f'<aside class="page-hero-visual reveal">{vis_fn()}</aside>' if vis_fn else ""
    shots = ""
    if gallery:
        shots = (
            "<section class='section section-alt'><div class='container'>"
            "<h2>Interface</h2>"
            + shot_gallery(gallery)
            + "</div></section>"
        )
    schema = [service_schema(h1, description, canonical)]
    if faqs:
        schema.append(faq_schema(faqs))
    body = f"""
<section class="page-hero"><div class="container page-hero-grid">
  <div>
    {crumbs_html([("/", "Home"), ("/solutions/", "Solutions"), (canonical, name)])}
    <h1>{esc(h1)}</h1>
    <p class="lead">{esc(intro)}</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="/contact/?intent=demo" data-track="demo_requested">{esc(cta)}</a>
      <a class="btn btn-secondary" href="/contact/">Discuss Your Project</a>
    </div>
  </div>
  {vis}
</div></section>
<section class="section"><div class="container prose">
  <h2>Capabilities</h2>
  {bullets(capabilities)}
  {notes}
  <h2>Related work and reading</h2>
  <ul>{rel_work}</ul>
</div></section>
{shots}
<section class="section section-alt"><div class="container split"><div><h2>Questions</h2></div>{faq_html(faqs)}</div></section>
<section class="section"><div class="container split">
  <div>
    <h2>Request a demo or a scoped build</h2>
    <p class="muted">Describe the organisation and the processes that matter. Budget is optional. We will show the closest system, or confirm what still needs to be built.</p>
  </div>
  {enquiry_form("demo_request", "Demo request | Cyber Developers", cta)}
</div></section>
"""
    emit(
        f"solutions/{slug}/index.html",
        title,
        description,
        canonical,
        [("/", "Home"), ("/solutions/", "Solutions"), (canonical, name)],
        body,
        extra=schema,
        current="/solutions/",
        priority="0.85",
        image=og or "/assets/img/og-default.webp",
    )


def build_solutions():
    emit(
        "solutions/index.html",
        "Business Software Solutions | Cyber Developers South Africa",
        "School, legal, funeral, workflow, municipality, logistics and custom CRM software that Cyber Developers can provide or customise.",
        "/solutions/",
        [("/", "Home"), ("/solutions/", "Solutions")],
        f"""
<section class="page-hero"><div class="container">
  {crumbs_html([("/", "Home"), ("/solutions/", "Solutions")])}
  <h1>Custom digital platforms, built as real software</h1>
  <p class="lead">Cyber Developers designs and builds custom digital platforms, business systems, mobile and web applications, and workflow solutions. The screens below are systems we have actually produced — not service cards.</p>
  <div class="hero-actions">
    <a class="btn btn-primary" href="/contact/">Discuss Your Project</a>
    <a class="btn btn-secondary" href="/our-work/">Explore Our Work</a>
  </div>
</div></section>
<section class="section"><div class="container">
  {feature_block("/solutions/workflow-management-system/", "Custom Business & Workflow Systems", "Operations software",
                 "We build the internal systems organisations run on: workflow automation, case management, SLA tracking, requisitions, billing, expenses, team management, audit trails and management reporting.",
                 ["Workflow", "Cases", "SLA", "Requisitions", "Billing", "Expenses", "Audit", "Reports"],
                 shot("tshira-dashboard"), "Explore workflow systems",
                 extra_links=[("Tshira case study", "/our-work/tshira-workflow-system/")])}
  {feature_block("/solutions/municipality-management-software/", "Municipal & Government Platforms", "Citizen services",
                 "Citizen service portals, municipal fault reporting, service-request tracking, emergency information, alerts and public notices, queue booking, tenders and local business directories.",
                 ["Citizen portal", "Fault reporting", "Tracking", "Emergency", "Alerts", "Queues", "Tenders", "Directory"],
                 shot_stack("smartcity-home", "smartcity-services"), "Explore municipality software", reverse=True,
                 extra_links=[("SmartCity case study", "/our-work/municipality-platform/")])}
  {feature_block("/solutions/school-management-system/", "School & College Management", "Education",
                 "Role-based portals for admissions, student records, attendance, marks, timetables, staff management, finance and reporting — for South African schools, colleges and TVET institutions.",
                 ["Admissions", "Student records", "Attendance", "Marks", "Timetables", "Staff", "Finance", "Reporting"],
                 school_map(), "Explore school management",
                 extra_links=[("SchoolHub SA case study", "/our-work/school-lms/")])}
  {feature_block("/solutions/law-firm-management-software/", "Legal Practice Management", "LawTech SA",
                 "Client management, matters, invoicing, fee books, trust accounting, debt recovery and document workflow for South African practices.",
                 ["Clients", "Matters", "Invoicing", "Fee book", "Trust", "Debt recovery"],
                 lawyer_map(), "Explore legal software", reverse=True,
                 extra_links=[("LawTech SA case study", "/our-work/lawyer-management-system/")])}
  {feature_block("/solutions/funeral-parlour-management-software/", "Funeral Business Management", "Legacy Care",
                 "Member management, policy products, premium collections, arrears, claims, funeral operations, mortuary, inventory, fleet and finance reporting.",
                 ["Members", "Policies", "Collections", "Arrears", "Claims", "Mortuary", "Fleet", "Finance"],
                 funeral_map(), "Explore funeral software",
                 extra_links=[("Legacy Care case study", "/our-work/funeral-parlour-system/")])}
  {feature_block("/our-work/vayasa/", "Transport & Marketplace Platforms", "VayaSA",
                 "Marketplace platforms covering ride sharing, bus ticketing, taxi bookings, driver and operator onboarding, booking engines and customer accounts.",
                 ["Ride sharing", "Bus tickets", "Taxi bookings", "Onboarding", "Accounts"],
                 shot_stack("vayasa-home", "vayasa-search"), "Explore VayaSA", reverse=True)}
  {feature_block("/solutions/logistics-delivery-software/", "Logistics & Delivery Platforms", "FluxMove",
                 "Live quotation engines, distance and pricing logic, vehicle selection, booking, driver and provider onboarding, delivery management and business accounts.",
                 ["Live quotes", "Pricing", "Vehicles", "Booking", "Onboarding", "Business accounts"],
                 shot("fluxmove-quote"), "Explore logistics software",
                 extra_links=[("FluxMove case study", "/our-work/fluxmove/")])}
  {feature_block("/solutions/custom-crm-development/", "Custom CRM Development", "When the object is not a lead",
                 "We build CRMs around repairs, learners, tickets or matters when Salesforce-shaped objects do not fit. There is no product screenshot here because the data model is the brief.",
                 ["Records", "Pipeline", "History", "Permissions"],
                 crm_map(), "Explore custom CRM", reverse=True)}
</div></section>
{cta_band("Need a system in this shape?", "Describe the process. We will show the closest system, or confirm what still needs to be built.", primary=("Discuss Your Project", "/contact/"))}
""",
        current="/solutions/",
        priority="0.8",
    )

    solution_page(
        "school-management-system",
        "School Management System",
        "School Management Software",
        "School Management Software South Africa | Cyber Developers",
        "School management software for South African schools, colleges and TVETs: students, guardians, attendance, fees, HR, communication and reporting.",
        "SchoolHub SA is Cyber Developers’ school management platform for South African schools, colleges, TVETs and training centres. It is a multi-tenant web system with separate portals rather than a single shared desktop.",
        [
            "Student management, applications and enrolment statuses.",
            "Guardian / parent portal for children, fees, attendance, results and report cards.",
            "Attendance for learners and staff, including absence notices.",
            "Academic years, terms/sessions, classes, subjects, timetables and assessments.",
            "Fees, invoices, receipts, statements, debtors, payment recording and reminders.",
            "South African payment methods configured per school (including PayFast, Ozow and Yoco where enabled).",
            "HR, staff records, leave, timesheets, payroll views and payslips.",
            "Email and SMS communication (SendGrid / Twilio when the school configures them).",
            "Student cards (PDF identity cards generated from the student record).",
            "Reporting, report cards, letters, certificates and audit trail.",
            "Online class links on the timetable where a meeting URL is captured.",
            "Backup and restore jobs, plus SA-SAMS-oriented import where that module is used.",
            "POPIA-oriented consent fields on student records.",
        ],
        """<h2>Who it is for</h2>
        <p>Independent schools, colleges, TVETs and training centres that need one student administration system for academics, fees and staff — not only an LMS for video courses. Government SA-SAMS remains a reference for imports; this product is not claimed as an official SA-SAMS replacement.</p>
        <h2>The problem it is built to solve</h2>
        <p>A school cannot answer a simple question when academics, fees, attendance and parent communication live in different tools. Staff invent spreadsheets to close the gaps. SchoolHub SA keeps those records on one student file, with portals for administrators, teachers, learners and parents.</p>
        <h2>How work typically moves</h2>
        <p>Admissions capture an application. The learner is enrolled into a class and academic session. Teachers take attendance and assessments. Finance issues invoices and records payments (including local processors where the school enables them). Parents see children, fees, attendance and report cards. HR runs leave and payslips for staff. Letters, certificates and student cards come from the same record.</p>
        <h2>Implementation and customisation</h2>
        <p>The architecture is multi-school. Licensing, hosting, payment methods and communication providers are agreed per deployment. Biometric hardware is not a built-in module; if a school already uses biometric attendance devices, integration can be scoped rather than assumed. We do not show admin screens that display revoked or restricted licence warnings.</p>
        <p>Read the <a href="/knowledge-centre/school-management-software-features/">school software features guide</a> or the <a href="/industries/#education">education industry</a> page.</p>""",
        [
            ("Is this only an LMS for video courses?", "No. It is a school administration and learning platform: people, money, attendance, assessments and communication, with student and parent access."),
            ("Can more than one school run on it?", "The architecture is multi-school. Licensing and hosting are agreed per deployment."),
            ("Do you host it?", "Deployments have used PostgreSQL-backed Next.js hosting. Hosting is part of the implementation conversation."),
            ("Is this official SA-SAMS software?", "No. SA-SAMS-oriented import exists as a module where it is used. It is not an official department product."),
        ],
        [
            ("School / College LMS case study", "/our-work/school-lms/"),
            ("Education industry", "/industries/#education"),
            ("Custom software development", "/services/custom-software-development/"),
            ("School software features article", "/knowledge-centre/school-management-software-features/"),
        ],
        gallery=["schoolhub-admin", "schoolhub-student", "schoolhub-admissions"],
        og=og_for("schoolhub-admin"),
    )

    solution_page(
        "law-firm-management-software",
        "Law Firm Management Software",
        "Law Firm Management Software",
        "Law Firm Management Software South Africa | Cyber Developers",
        "Law firm and legal practice management software for South African firms: clients, matters, invoices, fee book, trust accounts and debt collection.",
        "Cyber Developers builds practice software for law firms that need a shared file for clients and matters, not a collection of folders and spreadsheets. LawTech SA is a practice system organised around the matter file.",
        [
            "Client management and reception workflow.",
            "Case / matter management.",
            "Fee book.",
            "Invoicing against the matter.",
            "Trust accounting.",
            "Debt recovery / debt collection.",
            "Document and workflow management on the file.",
            "User permissions so candidate attorneys, secretaries and directors are not the same role.",
        ],
        """<h2>Who it is for</h2>
        <p>South African law firms and practices that need operational software around the matter — not a public marketing website. Specify litigation, RAF, conveyancing or general practice when you request a demo so we can walk the relevant file, not a generic pitch.</p>
        <h2>The problem</h2>
        <p>Practice work fails operationally when clients, matters, invoices and trust money sit in different places, and when every user has the same access. LawTech SA puts clients, billing and trust balances on the same dashboard operators actually use.</p>
        <h2>Implementation</h2>
        <p>Hosting and permissions are part of the implementation discussion. We do not make unsupported regulatory or compliance claims on this page. Trust accounting in the product is a module for recording trust money against the matter; it is not a substitute for the firm’s professional obligations.</p>
        <p>See the <a href="/our-work/lawyer-management-system/">LawTech SA case study</a> and the <a href="/industries/#legal">legal industry</a> page.</p>""",
        [
            ("Is this the same as a marketing website for a practice?", "No. A public site is a different kind of project from a matter-management system."),
            ("Can it stay on our own server?", "Hosting is part of the implementation discussion. The application is designed as a business system, not a consumer SaaS login page only."),
            ("Do you certify this for Law Society compliance?", "No. We describe the modules in the software. Professional and regulatory duties stay with the firm."),
        ],
        [
            ("LawTech SA case study", "/our-work/lawyer-management-system/"),
            ("Legal industry", "/industries/#legal"),
            ("Business systems", "/services/business-systems/"),
        ],
        gallery=["lawtech-dashboard"],
        og=og_for("lawtech-dashboard"),
    )

    solution_page(
        "funeral-parlour-management-software",
        "Funeral Parlour Management",
        "Funeral Parlour Management Software",
        "Funeral Parlour Management Software South Africa | Cyber Developers",
        "Funeral parlour and funeral policy management software for South African funeral businesses: members, premiums, claims, mortuary, fleet and finance.",
        "Legacy Care is Cyber Developers’ funeral business platform. The management dashboard covers members, policies, premium collections, arrears, claims, funeral operations, mortuary, inventory, fleet and finance.",
        [
            "Member management.",
            "Policy products.",
            "Premium collections and billing batches.",
            "Arrears dashboard.",
            "Claims processing.",
            "Funeral operations and obituaries / memorials.",
            "Mortuary register.",
            "Inventory / stock.",
            "Fleet and vehicles.",
            "Finance and reporting.",
        ],
        """<h2>Who it is for</h2>
        <p>Funeral parlours and related societies that combine member policies, premium collection, claims and the operational work of a funeral — mortuary, inventory and vehicles — in one file.</p>
        <h2>The problem</h2>
        <p>Off-the-shelf tools rarely match that file. Collections, arrears and claims drift into spreadsheets while operations run somewhere else. Legacy Care treats them as modules of the same application.</p>
        <h2>Implementation</h2>
        <p>Naming and extra steps are scoped during implementation. The screens on this site are from the live interface. A demonstration is the honest way to see the rest of the workflow.</p>""",
        [
            ("Can this match our parlour’s file?", "The modules above are in the product. Naming and extra steps are scoped during implementation."),
            ("Do you publish a full screen inventory?", "The screens on this site are from the live interface. A demonstration is the honest way to see the rest."),
        ],
        [
            ("Legacy Care case study", "/our-work/funeral-parlour-system/"),
            ("Funeral industry", "/industries/#funeral"),
            ("Business systems", "/services/business-systems/"),
        ],
        gallery=["legacy-dashboard", "legacy-collections"],
        og=og_for("legacy-dashboard"),
    )

    solution_page(
        "workflow-management-system",
        "Workflow Management System",
        "Workflow Management System",
        "Workflow Management System South Africa | Cyber Developers",
        "Workflow management software for South African organisations: cases, assignment, approval, SLA monitoring, reporting and an audit trail.",
        "The Tshira Workflow Management System is a production-style case workflow: work is received, assigned, collected in the field, reviewed, invoiced and closed, with money movement tied to status.",
        [
            "Roles including admin, provincial coordinators, field officers, consultants, reviewers and finance.",
            "Case lifecycle from intake through assignment, collection, quality check, review, invoicing and closure.",
            "Client records, documents and case history.",
            "Requisitions (bookings/clearance before work) distinct from expenses (claims after spending).",
            "Invoice generation only when a case is ready, with sequential numbering.",
            "Notifications and reporting for coordinators, field officers and finance.",
            "Organisation profile, banking details and invoice settings.",
        ],
        """<h2>Who it is for</h2>
        <p>Organisations that run case-based work across head office, branches and field staff — professional services, multi-province operations, and teams whose status currently lives in email.</p>
        <h2>The problem</h2>
        <p>Handovers disappear. Finance invoices unfinished work because there is no hard rule in the system. Tshira makes assignment, approval, SLA monitoring, reporting and the audit trail part of the same case.</p>
        <h2>Implementation</h2>
        <p>The same pattern can be adapted to other organisations: rename the stages, keep statuses, owners, documents and finance locks. It is not a blank BPM canvas.</p>
        <p><a href="/services/workflow-automation/">Workflow automation service</a> · <a href="/knowledge-centre/how-workflow-automation-can-reduce-manual-admin/">How workflow automation reduces manual admin</a></p>""",
        [
            ("Is this generic BPM software?", "It is a concrete application with named roles and statuses. We can rename the stages to match another organisation; we do not drop a blank canvas on you and call it done."),
            ("Can provinces or branches be separated?", "Yes. Assignment by province is part of the original design."),
        ],
        [
            ("Tshira case study", "/our-work/tshira-workflow-system/"),
            ("Workflow automation service", "/services/workflow-automation/"),
            ("Enterprise industry", "/industries/#enterprise"),
        ],
        gallery=["tshira-dashboard", "tshira-reports"],
        og=og_for("tshira-dashboard"),
    )

    solution_page(
        "municipality-management-software",
        "Municipality Management Software",
        "Municipality Management Software",
        "Municipality Management Software South Africa | Cyber Developers",
        "Municipality management software and citizen service portals: issue reporting, alerts, queue booking, notices, jobs, tenders and a business directory.",
        "Cyber Developers built SmartCity Muni, a municipality platform with a citizen application and an administration console. It is software for service delivery and records, not a municipal brochure website. This page describes the product. It does not claim that a named municipality has deployed it.",
        [
            "Resident registration with OTP verification.",
            "Citizen dashboard, fault/issue reporting and ticket tracking.",
            "Queue booking.",
            "Municipal billing views and bill management on the admin side.",
            "Meter reading capture (service module).",
            "Proof of residence and document services.",
            "Notices, alerts and emergency information.",
            "Business directory.",
            "Job listings with apply and track flows.",
            "Disputes, audit log and operational reports.",
        ],
        """<h2>Who it is for</h2>
        <p>Local government and related service-delivery organisations that need a citizen channel and an operations desk on the same ticket — faults, queues, notices and emergency information — rather than a brochure site.</p>
        <h2>The problem</h2>
        <p>Residents still phone, queue or arrive in person for issues that a verified account could track. Staff then reconstruct the same request in a back office. SmartCity Muni is built so the public channel and the operations desk can share one record.</p>
        <h2>Implementation</h2>
        <p>Deployments would be scoped to by-laws, billing rules and integrations. We do not claim a national government contract, and we do not imply a live municipal rollout unless you are shown that deployment in a demo.</p>""",
        [
            ("Does this replace the financial system?", "Not automatically. Billing modules can be used as built or integrated with an existing finance system after discovery."),
            ("Is there a public demo URL?", "Request a demo. We do not publish admin credentials on the marketing site."),
            ("Is SmartCity live at a named municipality?", "This site documents the software we built. It does not list municipal clients or usage statistics."),
        ],
        [
            ("SmartCity Muni case study", "/our-work/municipality-platform/"),
            ("Government industry", "/industries/#government"),
            ("Web application development", "/services/web-application-development/"),
        ],
        gallery=["smartcity-home", "smartcity-services", "smartcity-report", "smartcity-emergency"],
        og=og_for("smartcity-home"),
    )

    solution_page(
        "logistics-delivery-software",
        "Logistics & Delivery Software",
        "Logistics & Delivery Software",
        "Logistics Software South Africa | Cyber Developers",
        "Logistics and delivery management software for South Africa: instant quotations, vehicle selection, booking, drivers, providers and business accounts.",
        "FluxMove is Cyber Developers’ nationwide delivery marketplace model: customers book a move, verified drivers accept work, and administrators review driver applications. A ride-hailing / passenger product is covered separately as VayaSA.",
        [
            "Instant quotations with distance, vehicle type and urgency.",
            "Vehicle selection from smaller vehicles through trucks.",
            "Customer booking with pickup/drop-off and ZAR estimates.",
            "Delivery scheduling and booking status tracking.",
            "Driver and provider onboarding, including document verification.",
            "Open job browse and accept flow for drivers.",
            "Admin approval and rejection of provider applications.",
            "Optional Expo driver mobile app for on-the-road workflow.",
            "Business accounts, ratings, disputes and support tickets in the data model.",
        ],
        """<h2>Who it is for</h2>
        <p>Logistics, household-move and freight operators that need quotation, vehicle matching and booking in software — as a marketplace or as a closed driver pool.</p>
        <h2>The problem</h2>
        <p>Moving goods usually means phoning around for a vehicle. Price, distance, vehicle type and who is allowed to take the job stay in someone’s head. FluxMove puts quotation, selection, booking and provider review in one platform.</p>
        <h2>Passenger transport</h2>
        <p>If the requirement is passengers rather than freight, see <a href="/our-work/vayasa/">VayaSA</a> — ride shares, bus tickets and taxi seats, with South African payment options used on that product.</p>""",
        [
            ("Is FluxMove live?", "A public site exists at fluxmove.co.za. Treat production status as something to confirm on a demo; marketing pages should not invent traffic figures."),
            ("Can this run as a private fleet system?", "Yes. The marketplace model can be narrowed to a closed driver pool."),
        ],
        [
            ("FluxMove case study", "/our-work/fluxmove/"),
            ("VayaSA", "/our-work/vayasa/"),
            ("Logistics industry", "/industries/#logistics"),
            ("Mobile app development", "/services/mobile-app-development/"),
        ],
        gallery=["fluxmove-quote", "fluxmove-hero", "fluxmove-vehicles"],
        og=og_for("fluxmove-quote"),
    )

    solution_page(
        "custom-crm-development",
        "Custom CRM Development",
        "Custom CRM Development",
        "Custom CRM Development South Africa | Cyber Developers",
        "Custom CRM development in South Africa for teams whose sales, service and billing process does not fit Salesforce or Microsoft Dynamics.",
        "A custom CRM is worth building when the objects you care about are not ‘leads and opportunities’ — they might be repairs, learners, matters, bookings or municipal accounts — and the process is the product.",
        [
            "Customer or organisation records with the fields you actually use.",
            "Pipelines or case statuses that match the team’s stages.",
            "Quotations, invoices and service or job history.",
            "Permissions and reporting.",
            "Integrations to email, payments or existing finance tools where scoped.",
        ],
        """<p>We do not position custom CRM as cheaper Salesforce. It is the right choice when the data model is the business. If a well-configured off-the-shelf CRM already fits, we will say so.</p>""",
        [
            ("When is Salesforce or Dynamics a better fit?", "When you want a widely supported platform, a large app marketplace, and your process is close to standard CRM. Custom makes sense when the objects and workflows are specific and you need to own them."),
            ("Can you migrate from spreadsheets?", "Yes, with an explicit mapping and a cleanup step. Garbage in the sheet stays garbage in the CRM if you skip that."),
        ],
        [("Business systems", "/services/business-systems/"), ("Knowledge Centre: custom CRM", "/knowledge-centre/custom-crm-vs-salesforce-microsoft-dynamics/")],
    )


if __name__ == "__main__":
    build_solutions()
    print("solutions done")
