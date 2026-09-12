#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from site_lib import crumbs_html, enquiry_form, faq_html, service_schema, faq_schema, esc
from generate_core import emit, bullets


def solution_page(slug, name, h1, title, description, intro, capabilities, notes, faqs, related, cta="Request Demo"):
    canonical = f"/solutions/{slug}/"
    rel_work = "".join(f'<li><a href="{u}">{esc(n)}</a></li>' for n, u in related)
    body = f"""
<section class="page-hero"><div class="container">
  {crumbs_html([("/", "Home"), ("/solutions/", "Solutions"), (canonical, name)])}
  <h1>{esc(h1)}</h1>
  <p class="lead">{esc(intro)}</p>
  <div class="hero-actions">
    <a class="btn btn-primary" href="/contact/?intent=demo" data-track="demo_requested">{esc(cta)}</a>
    <a class="btn btn-secondary" href="/contact/">Discuss Your Project</a>
  </div>
</div></section>
<section class="section"><div class="container prose">
  <h2>Core modules</h2>
  {bullets(capabilities)}
  {notes}
  <h2>Related</h2>
  <ul>{rel_work}</ul>
</div></section>
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
        extra=[service_schema(h1, description, canonical), faq_schema(faqs)],
        current="/solutions/",
        priority="0.85",
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
  <h1>Solutions</h1>
  <p class="lead">These are systems designed around a real operating model — not a list of industries. Open a page for the problem, the modules, and the case study where one exists. Where a private system is not in this public repository, the feature list stays conservative.</p>
</div></section>
<section class="section"><div class="container" style="max-width:48rem">
  <div class="row-list">
    <a href="/solutions/school-management-system/"><h3>School Management System</h3><p>Students, guardians, attendance, fees, HR, SMS/email and reporting for South African schools, colleges and TVETs.</p><span class="more">See the system</span></a>
    <a href="/solutions/law-firm-management-software/"><h3>Law Firm Management Software</h3><p>Clients, cases, documents, tasks, billing, permissions and RAF workflow where it applies.</p><span class="more">See the system</span></a>
    <a href="/solutions/funeral-parlour-management-software/"><h3>Funeral Parlour Management</h3><p>Administration software scoped to how the parlour actually runs.</p><span class="more">See the system</span></a>
    <a href="/solutions/workflow-management-system/"><h3>Workflow Management System</h3><p>Cases, field capture, review, requisitions, expenses and invoicing.</p><span class="more">See the system</span></a>
    <a href="/solutions/municipality-management-software/"><h3>Municipality Management Software</h3><p>Residents, billing, fault reporting, queues, notices and administration.</p><span class="more">See the system</span></a>
    <a href="/solutions/logistics-delivery-software/"><h3>Logistics &amp; Delivery Software</h3><p>Bookings, driver checks, vehicle types and job status.</p><span class="more">See the system</span></a>
    <a href="/solutions/custom-crm-development/"><h3>Custom CRM Development</h3><p>When the object is not a lead — repairs, learners, tickets, matters.</p><span class="more">See the system</span></a>
  </div>
</div></section>
""",
        current="/solutions/",
        priority="0.8",
    )

    solution_page(
        "school-management-system",
        "School Management System",
        "School Management System South Africa",
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
        <p>Independent schools, colleges and training centres that need one system for academics, fees and staff. Government SA-SAMS remains a reference for imports; this product is not claimed as an official SA-SAMS replacement.</p>
        <h2>About biometrics</h2>
        <p>Biometric hardware is not a built-in module in the public school platform. If a school already uses biometric attendance devices, integration can be scoped as a project rather than assumed.</p>""",
        [
            ("Is this only an LMS for video courses?", "No. It is a school administration and learning platform: people, money, attendance, assessments and communication, with student and parent access."),
            ("Can more than one school run on it?", "The architecture is multi-school. Licensing and hosting are agreed per deployment."),
            ("Do you host it?", "Deployments have used PostgreSQL-backed Next.js hosting. Hosting is part of the implementation conversation."),
        ],
        [("School / College LMS case study", "/our-work/school-lms/"), ("Education industry", "/industries/")],
    )

    solution_page(
        "law-firm-management-software",
        "Law Firm Management Software",
        "Law Firm Management Software South Africa",
        "Law Firm Management Software South Africa | Cyber Developers",
        "Law firm management software for South African practices: clients, cases, documents, tasks, billing, permissions and RAF workflow where it applies.",
        "Cyber Developers builds practice software for law firms that need a shared file for clients and matters, not a collection of folders and spreadsheets. The public website repository does not contain the full legal-product source; the capabilities below are the modules this solution is built to cover.",
        [
            "Client management.",
            "Case / matter management.",
            "Document storage against the matter.",
            "RAF workflow where the practice handles Road Accident Fund work.",
            "Tasks and deadlines.",
            "Billing and reporting.",
            "User permissions so candidate attorneys, secretaries and directors are not the same role.",
        ],
        """<p>If your practice needs a demonstration, request a demo and specify litigation, RAF, conveyancing or general practice. We will not invent extra modules on this page.</p>""",
        [
            ("Is this the same as the Chiedza immigration website?", "No. A public marketing site for an immigration practice is a different kind of project from a matter-management system."),
            ("Can it stay on our own server?", "Hosting is part of the implementation discussion. The application is designed as a business system, not a consumer SaaS login page only."),
        ],
        [("Lawyer Management System", "/our-work/lawyer-management-system/"), ("Legal industry", "/industries/")],
    )

    solution_page(
        "funeral-parlour-management-software",
        "Funeral Parlour Management",
        "Funeral Parlour Software South Africa",
        "Funeral Parlour Software South Africa | Cyber Developers",
        "Custom funeral parlour management software for South African funeral businesses, scoped to the processes the parlour actually runs.",
        "Cyber Developers develops custom management software for funeral parlours. A full feature inventory is not published here because the product source is not in this public website repository, and we will not invent modules.",
        [
            "A management system fitted to the parlour’s administration, records and reporting.",
            "User access for the people who actually operate the business.",
            "Customisation around the parlour’s existing paper or spreadsheet process.",
        ],
        """<p>The previous marketing site listed productised names and modules that could not be verified against source. Those claims were removed. Request a demo and we will walk through the live system rather than a brochure list.</p>""",
        [
            ("Can you list every screen?", "Not from this public repository. A demonstration is the honest way to see the current build."),
            ("Will you copy a competitor’s feature page?", "No. Features are those the system actually has or that we agree to build."),
        ],
        [("Funeral Parlour System", "/our-work/funeral-parlour-system/"), ("Business systems", "/services/business-systems/")],
    )

    solution_page(
        "workflow-management-system",
        "Workflow Management System",
        "Workflow Management Software South Africa",
        "Workflow Management Software South Africa | Cyber Developers",
        "Workflow management software for South African organisations: cases, roles, field capture, review, requisitions, expenses and invoicing.",
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
        """<p>The same pattern — statuses, owners, documents, finance locks — can be adapted to other organisations that run case-based work, not only the original Tshira deployment.</p>""",
        [
            ("Is this generic BPM software?", "It is a concrete application with named roles and statuses. We can rename the stages to match another organisation; we do not drop a blank canvas on you and call it done."),
            ("Can provinces or branches be separated?", "Yes. Assignment by province is part of the original design."),
        ],
        [("Tshira case study", "/our-work/tshira-workflow-system/"), ("Workflow automation service", "/services/workflow-automation/")],
    )

    solution_page(
        "municipality-management-software",
        "Municipality Management Software",
        "Municipality Management Software",
        "Municipality Management Software | Cyber Developers South Africa",
        "Municipality management software for South African local government: residents, billing, fault reporting, queues, notices and citizen services.",
        "Cyber Developers built a municipality platform with a citizen application and an administration console. It is software for service delivery and records, not a municipal brochure website.",
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
        """<p>Deployments are scoped to the municipality’s by-laws, billing rules and integrations. We do not claim a national government contract on this page.</p>""",
        [
            ("Does this replace the financial system?", "Not automatically. Billing modules can be used as built or integrated with an existing finance system after discovery."),
            ("Is there a public demo URL?", "Request a demo. We do not publish admin credentials on the marketing site."),
        ],
        [("Municipality Platform case study", "/our-work/municipality-platform/")],
    )

    solution_page(
        "logistics-delivery-software",
        "Logistics & Delivery Software",
        "Logistics & Delivery Software",
        "Logistics & Delivery Software | Cyber Developers South Africa",
        "Logistics and delivery software for South Africa: customer bookings, driver verification, vehicle types, job status and admin review.",
        "Fluxmove is Cyber Developers’ nationwide delivery marketplace model: customers book a move, verified drivers accept work, and administrators review driver applications. A ride-hailing / passenger product is covered separately as VayaSA.",
        [
            "Customer registration, pickup/drop-off booking and ZAR fare estimates.",
            "Booking status tracking.",
            "Driver registration, ID/licence/vehicle verification and availability.",
            "Open job browse and accept flow for drivers.",
            "Vehicle types from smaller vehicles through trucks, including empty-return preference.",
            "Admin approval and rejection of driver applications.",
            "Optional driver mobile app for on-the-road workflow.",
            "Business accounts, ratings, disputes and support tickets in the data model.",
        ],
        """<h2>Ride-hailing</h2>
        <p>If the requirement is passenger transport rather than freight, see <a href="/our-work/vayasa/">VayaSA</a> — ride shares, bus tickets and taxi seats, with South African payment options used on that product.</p>""",
        [
            ("Is Fluxmove live?", "A public site exists at fluxmove.co.za. Treat production status as something to confirm on a demo; marketing pages should not invent traffic figures."),
            ("Can this run as a private fleet system?", "Yes. The marketplace model can be narrowed to a closed driver pool."),
        ],
        [("Fluxmove case study", "/our-work/fluxmove/"), ("VayaSA", "/our-work/vayasa/")],
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
