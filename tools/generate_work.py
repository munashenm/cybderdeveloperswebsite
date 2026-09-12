#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from site_lib import crumbs_html, cta_band, esc
from generate_core import emit, checks


def case_study(slug, title, h1, description, tag, overview, problem, solution, features, tech, approach, status, extras=""):
    canonical = f"/our-work/{slug}/"
    body = f"""
<section class="page-hero"><div class="container">
  {crumbs_html([("/", "Home"), ("/our-work/", "Our Work"), (canonical, title)])}
  <p class="eyebrow">{esc(tag)}</p>
  <h1>{esc(h1)}</h1>
  <p class="lead">{esc(overview)}</p>
</div></section>
<section class="section"><div class="container split">
  <div class="prose">
    <h2>Project overview</h2>
    <p>{esc(overview)}</p>
    <h2>Business problem</h2>
    <p>{esc(problem)}</p>
    <h2>Solution</h2>
    <p>{esc(solution)}</p>
    <h2>Key features</h2>
    {checks(features)}
    <h2>Development approach</h2>
    <p>{esc(approach)}</p>
    <h2>Current status</h2>
    <p>{esc(status)}</p>
    {extras}
    <h2>Need something similar?</h2>
    <p>If this shape of system is close to yours, start a conversation. We will not invent outcome statistics for this case study.</p>
    <p><a class="btn btn-primary" href="/contact/">Discuss Your Project</a></p>
  </div>
  <aside>
    <article class="card">
      <h3>Technology</h3>
      <div class="tech-pills" style="margin-top:0.8rem">{''.join(f'<li>{esc(t)}</li>' for t in tech)}</div>
    </article>
    <article class="card" style="margin-top:1rem">
      <h3>Screenshots</h3>
      <p>Product screenshots are not bundled in this marketing repository. A live walkthrough is available on request so we do not publish mock dashboards as if they were the system.</p>
    </article>
  </aside>
</div></section>
{cta_band("Need something similar?", "Discuss the process you want software to carry.", ("Discuss Your Project", "/contact/"), ("View Our Work", "/our-work/"))}
"""
    emit(
        f"our-work/{slug}/index.html",
        f"{title} | Cyber Developers Work",
        description,
        canonical,
        [("/", "Home"), ("/our-work/", "Our Work"), (canonical, title)],
        body,
        current="/our-work/",
        priority="0.75",
    )


def build_work():
    emit(
        "our-work/index.html",
        "Our Work | Cyber Developers Software Projects",
        "Selected software built by Cyber Developers: VayaSA, Fluxmove, Tshira, school management, municipality, legal and funeral systems.",
        "/our-work/",
        [("/", "Home"), ("/our-work/", "Our Work")],
        f"""
<section class="page-hero"><div class="container">
  {crumbs_html([("/", "Home"), ("/our-work/", "Our Work")])}
  <p class="eyebrow">Our Work</p>
  <h1>Systems you can inspect, not invented logos.</h1>
  <p class="lead">These projects exist as software Cyber Developers has designed. We removed unverifiable portfolio names, testimonials and statistics from the previous site.</p>
</div></section>
<section class="section"><div class="container">
  <div class="grid-3">
    <a class="card project-card" href="/our-work/vayasa/"><div class="visual"><span>Transport marketplace</span></div><div class="body"><span class="tag">VayaSA</span><h3>VayaSA</h3><p>Ride sharing, bus tickets and taxi seats with South African payments and verification flows.</p></div></a>
    <a class="card project-card" href="/our-work/fluxmove/"><div class="visual"><span>Delivery marketplace</span></div><div class="body"><span class="tag">Fluxmove</span><h3>Fluxmove</h3><p>Freight bookings, driver onboarding and vehicle types for deliveries across South Africa.</p></div></a>
    <a class="card project-card" href="/our-work/tshira-workflow-system/"><div class="visual"><span>Case workflow</span></div><div class="body"><span class="tag">Tshira</span><h3>Tshira Workflow System</h3><p>Provincial case assignment, field collection, review, requisitions, expenses and invoicing.</p></div></a>
    <a class="card project-card" href="/our-work/school-lms/"><div class="visual"><span>Education platform</span></div><div class="body"><span class="tag">SchoolHub SA</span><h3>School / College LMS</h3><p>Multi-portal school management: academics, fees, HR, cards, communication and backups.</p></div></a>
    <a class="card project-card" href="/our-work/lawyer-management-system/"><div class="visual"><span>Legal practice</span></div><div class="body"><span class="tag">Legal</span><h3>Lawyer Management System</h3><p>Practice administration covering clients, cases, documents, tasks, billing and permissions.</p></div></a>
    <a class="card project-card" href="/our-work/funeral-parlour-system/"><div class="visual"><span>Funeral operations</span></div><div class="body"><span class="tag">Funeral</span><h3>Funeral Parlour System</h3><p>Custom management software for funeral businesses. Feature detail is confirmed in demo, not invented here.</p></div></a>
    <a class="card project-card" href="/our-work/municipality-platform/"><div class="visual"><span>Local government</span></div><div class="body"><span class="tag">Municipality</span><h3>Municipality Platform</h3><p>Citizen and admin software for billing, issues, queues, notices and resident services.</p></div></a>
    <a class="card project-card" href="/solutions/school-management-system/"><div class="visual"><span>Also built</span></div><div class="body"><span class="tag">Related</span><h3>Student accommodation system</h3><p>A separate student accommodation management codebase exists. Ask if that operational area is relevant.</p></div></a>
  </div>
</div></section>
{cta_band()}
""",
        current="/our-work/",
        priority="0.9",
    )

    case_study(
        "vayasa",
        "VayaSA",
        "VayaSA",
        "VayaSA is a South African ride sharing and passenger transport marketplace built by Cyber Developers.",
        "Transport",
        "VayaSA is a ride sharing and passenger transport marketplace for South Africa: book ride shares, bus tickets and taxi seats between cities, with verification and payment flows designed for local use.",
        "Intercity passenger movement in South Africa mixes informal ranks, operators and private cars. A marketplace needs roles for passengers, drivers and operators, plus payments that include cash-at-rank as well as electronic options.",
        "A multi-role web application covering passenger search and booking, driver onboarding, bus and taxi operator dashboards, and an admin console for approvals and payouts.",
        [
            "Passenger, driver, bus operator, taxi operator and admin roles.",
            "Search for ride sharing, bus tickets and taxi departures.",
            "Digital tickets with QR codes for bus and taxi.",
            "Women-only ride filter and female-driver search.",
            "Chat after payment, trip sharing, SOS, ratings and reviews.",
            "SA ID verification and document uploads for drivers.",
            "Paystack, Ozow, Capitec Pay, and cash at rank — used where configured.",
            "Email verification, SMS OTP and in-app notifications.",
        ],
        ["Next.js", "TypeScript", "PostgreSQL", "Prisma", "Railway", "Cloudflare"],
        "App Router application with a PostgreSQL data model, server-side sessions and production health checks. Payments run in a documented demo mode when keys are absent so the product can be reviewed without inventing live transaction volumes.",
        "A production URL is published at vayasa.co.za. Treat live commercial metrics as unpublished unless separately verified.",
        extras='<p>Public product URL: <a href="https://www.vayasa.co.za">www.vayasa.co.za</a></p>',
    )

    case_study(
        "fluxmove",
        "Fluxmove",
        "Fluxmove",
        "Fluxmove is a South African delivery marketplace built by Cyber Developers for freight bookings and verified drivers.",
        "Logistics",
        "Fluxmove is a nationwide delivery marketplace: customers book moves; verified drivers with bakkies, vans or trucks accept jobs.",
        "Moving goods across South Africa usually means phoning around for a vehicle. The software problem is matching a booking to a verified driver and a suitable vehicle type, then keeping status visible.",
        "A web platform for customers, drivers and admins, with an optional Expo driver app for on-the-road steps.",
        [
            "Customer booking with pickup/drop-off in South Africa and ZAR estimates.",
            "Driver verification documents and admin approval.",
            "Availability, open jobs and accept flow.",
            "Vehicle types including empty-return preference.",
            "Business accounts, ratings, disputes and support tickets in the schema.",
            "Driver mobile app module for GPS, proof and OTP on the road.",
        ],
        ["Next.js", "TypeScript", "PostgreSQL", "Prisma", "Tailwind CSS"],
        "Next.js App Router with Prisma/PostgreSQL, cookie sessions and bcrypt credentials. Maps and live tracking are documented as integrations to add rather than silently claimed as finished on the marketing site.",
        "A public site is published at fluxmove.co.za. No user or GMV figures are stated here.",
        extras='<p>Public product URL: <a href="https://fluxmove.co.za">fluxmove.co.za</a></p>',
    )

    case_study(
        "tshira-workflow-system",
        "Tshira Workflow System",
        "Tshira Workflow System",
        "Tshira is a multi-province workflow system built by Cyber Developers for cases, field collection, review and invoicing.",
        "Workflow",
        "Tshira is a workflow management system for coordinating cases, client work, field data collection, document review, requisitions, expenses and invoicing across provinces.",
        "When case work is split between head office, provincial coordinators and field officers, status disappears into email. Finance also needs a hard rule: do not invoice unfinished work.",
        "A role-based Next.js application with a strict case lifecycle, separate requisition vs expense flows, and invoice generation gated on case status.",
        [
            "Roles: admin, provincial coordinator, data collection officer, business consultant, reviewer, finance.",
            "Sequential case statuses from intake to paid/closed, including return-for-correction paths.",
            "Clients, documents, case history and notifications.",
            "Requisitions for space/visit clearance versus expenses with receipt upload.",
            "Billing queue, sequential invoice numbers, PDF/print/email of invoices.",
            "Coordinator, DCO and finance reports.",
        ],
        ["Next.js", "TypeScript", "PostgreSQL", "Prisma", "NextAuth"],
        "The workflow was specified as an operations manual as much as a UI. Status transitions and finance locks are part of the product, not a later report.",
        "Described here from the application source and user manual. No client performance claims are added.",
    )

    case_study(
        "school-lms",
        "School / College LMS",
        "School / College LMS (SchoolHub SA)",
        "SchoolHub SA is Cyber Developers’ school management system for South African schools, colleges and TVETs.",
        "Education",
        "SchoolHub SA is a school management and learning platform for South African schools, colleges, TVETs and training centres, with portals for administrators, finance, teachers, students, parents, HR and staff.",
        "Schools typically split academics, fees and parent communication across different tools. Staff then cannot answer a simple question: is this learner present, up to date on fees, and progressing?",
        "A multi-tenant Next.js system with PostgreSQL, JWT sessions, finance and HR modules, email/SMS communications, student cards, backups and optional SA-SAMS import.",
        [
            "Multi-role authentication including school admin, principal, teacher, student, parent, finance, admissions, HR and staff.",
            "Student management with POPIA consent tracking and SA ID/phone validation helpers.",
            "Parent/guardian portal.",
            "Attendance, academic sessions, assessments, exams and report cards.",
            "Fees, invoices, receipts, statements, debtors and payment methods including EFT and local processors when configured.",
            "HR, leave, timesheets, payroll views and payslips.",
            "Email/SMS notices, student cards, letters, certificates, reporting and audit trail.",
            "Timetable online meeting URLs, backup/restore, SA-SAMS-oriented import.",
        ],
        ["Next.js", "React", "TypeScript", "PostgreSQL", "Prisma"],
        "Built as a multi-tenant SaaS-ready application. Demo credentials exist for local evaluation; they are not published on this marketing site.",
        "Active codebase. Screenshots should be captured from a staging instance for later use on this page.",
    )

    case_study(
        "lawyer-management-system",
        "Lawyer Management System",
        "Lawyer Management System",
        "Law firm management software by Cyber Developers covering clients, cases, documents, billing and permissions.",
        "Legal",
        "A practice management system for law firms: clients, matters, documents, tasks, billing, reporting and permissions, including RAF workflow where that work type applies.",
        "Legal work fails operationally when files, deadlines and billing live in different places, and when every user has the same access.",
        "A business system organised around the matter, with role-based access and billing against completed work.",
        [
            "Client management.",
            "Case management.",
            "Documents.",
            "RAF workflow where applicable.",
            "Tasks.",
            "Billing and reporting.",
            "User permissions.",
        ],
        ["TypeScript", "Next.js", "PostgreSQL", "APIs"],
        "Capabilities listed are those specified for this product line. The full private source is not in the public website repository, so this case study does not add unverified modules.",
        "Available for demonstration. Additional screenshots and a public feature tour are outstanding.",
    )

    case_study(
        "funeral-parlour-system",
        "Funeral Parlour System",
        "Funeral Parlour System",
        "Custom funeral parlour management software developed by Cyber Developers for South African funeral businesses.",
        "Operations",
        "Custom management software for funeral parlours, built around the administration the business actually runs.",
        "Funeral businesses combine records, family communication and administration. Off-the-shelf tools rarely match the parlour’s file.",
        "A custom business system. Exact screens are confirmed in a demo because the product source is not in this public repository.",
        [
            "Management software scoped to the parlour’s process.",
            "User access for operators.",
            "Customisation rather than a copied competitor feature list.",
        ],
        ["Custom business system"],
        "We would rather under-specify this page than republish unverifiable modules from the old marketing site.",
        "Demo on request. Screenshots and a verified feature inventory should be added when the product owner supplies them.",
    )

    case_study(
        "municipality-platform",
        "Municipality Platform",
        "Municipality Platform",
        "Municipality platform by Cyber Developers: citizen services, billing, fault reporting, queues and administration.",
        "Government",
        "A React application for municipal citizen services and administration: residents, billing, issues, queues, notices, jobs and related records.",
        "Residents still queue, phone or arrive in person for issues that a verified account could track. Staff need a back office for the same tickets, bills and notices.",
        "A citizen app and an admin console sharing services for billing, documents, meter readings, queues, reports and audit.",
        [
            "Registration, login and OTP verification.",
            "Issue reporting and ticket tracking.",
            "Queue booking.",
            "Billing and bill management.",
            "Meter readings and proof of residence modules.",
            "Notices, alerts, emergency information.",
            "Business directory and municipal job applications.",
            "Disputes, audit and reporting hubs.",
        ],
        ["React", "JavaScript", "Vite"],
        "Implemented as a React SPA with a service layer for each municipal domain. A production integration to a specific municipality’s finance backend is a deployment concern, not assumed here.",
        "Codebase exists. A hosted demo should be linked once a non-admin staging URL is available.",
    )


if __name__ == "__main__":
    build_work()
    print("work done")
