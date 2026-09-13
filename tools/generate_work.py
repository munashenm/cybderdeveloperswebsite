#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from site_lib import crumbs_html, cta_band, esc
from generate_core import emit, bullets
from graphics import (
    showcase, more_work,
    vayasa_map, fluxmove_map, tshira_map, school_map,
    lawyer_map, funeral_map, municipality_map,
)

CASE_VISUAL = {
    "vayasa": vayasa_map,
    "fluxmove": fluxmove_map,
    "tshira-workflow-system": tshira_map,
    "school-lms": school_map,
    "lawyer-management-system": lawyer_map,
    "funeral-parlour-system": funeral_map,
    "municipality-platform": municipality_map,
}


def case_study(slug, title, h1, description, tag, overview, problem, solution, features, tech, approach, status, extras="", live_url=None):
    canonical = f"/our-work/{slug}/"
    live = ""
    if live_url:
        live = f'<p>Live product: <a href="{live_url}">{live_url.replace("https://", "").replace("www.", "")}</a></p>'
    shots = (
        f"{live}"
        '<p class="shot-note">Interface screenshots for this page are still outstanding. '
        "Request a walkthrough if you need to see the live screens.</p>"
    )
    vis_fn = CASE_VISUAL.get(slug)
    vis = f'<div class="case-visual">{vis_fn()}</div>' if vis_fn else ""
    body = f"""
<section class="page-hero"><div class="container">
  {crumbs_html([("/", "Home"), ("/our-work/", "Our Work"), (canonical, title)])}
  <p class="eyebrow">{esc(tag)}</p>
  <h1>{esc(h1)}</h1>
  <p class="lead">{esc(overview)}</p>
</div></section>
<section class="section"><div class="container case-layout">
  <div class="prose">
  <h2>What we built</h2>
  <p>{esc(solution)}</p>
  <h2>Why it was needed</h2>
  <p>{esc(problem)}</p>
  <h2>How it works</h2>
  <p>{esc(approach)}</p>
  <h2>Key functionality</h2>
  {bullets(features)}
  <h2>Technology</h2>
  <p class="tech-inline">{" · ".join(esc(t) for t in tech)}</p>
  <h2>Screenshots</h2>
  {shots}
  <h2>Current status</h2>
  <p>{esc(status)}</p>
  {extras}
  <p style="margin-top:2rem"><a class="btn btn-primary" href="/contact/">Discuss a similar project</a></p>
  </div>
  {vis}
</div></section>
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
  <h1>Our work</h1>
  <p class="lead">Systems Cyber Developers has designed and built. Each page describes what the software does, why it was needed, and how it works. We do not invent user counts, revenue figures or testimonials.</p>
</div></section>
<section class="section"><div class="container">
  {showcase("/our-work/vayasa/", "VayaSA", "Ride-hailing & transport platform",
            "Ride sharing, bus tickets and taxi seats between cities, with South African payments and driver verification.",
            ["Web App", "Mobile Experience", "Payments", "Driver Management", "Booking System"],
            vayasa_map())}
  {showcase("/our-work/fluxmove/", "Fluxmove", "Delivery marketplace",
            "Customers book a move; verified drivers with bakkies, vans or trucks accept jobs.",
            ["Web App", "Driver App", "Verification", "Vehicle Types"],
            fluxmove_map(), reverse=True)}
  {showcase("/our-work/tshira-workflow-system/", "Tshira Workflow System", "Case workflow",
            "Provincial assignment, field collection, review, requisitions, expenses and invoicing.",
            ["Workflow", "Roles", "Documents", "Invoicing"],
            tshira_map())}
</div></section>
{more_work()}
<section class="section"><div class="container">
  <p class="muted">A separate student accommodation management codebase also exists. Ask if that operational area is relevant.</p>
</div></section>
{cta_band("Need something in this shape?", "Describe the process. We will tell you whether an existing system is close, or whether to design a new one.")}
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
        "Passengers search ride shares, bus tickets and taxi seats. Drivers and operators upload documents, then an admin console handles approvals and payouts. Payments include Paystack, Ozow, Capitec Pay and cash at rank where those options are configured.",
        "A production URL is published at vayasa.co.za. Treat live commercial metrics as unpublished unless separately verified.",
        live_url="https://www.vayasa.co.za",
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
        "A customer books a pickup and drop-off. Verified drivers see open jobs and accept them. Administrators review driver applications. An optional driver app covers the on-the-road steps.",
        "A public site is published at fluxmove.co.za. No user or GMV figures are stated here.",
        live_url="https://fluxmove.co.za",
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
        "A case is received, assigned by province, collected in the field, checked, reviewed and only then invoiced. Requisitions happen before spending; expenses are claimed afterwards, so the two are not mixed.",
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
        "Each role uses a portal against the same student record. Finance sees invoices and debtors; teachers capture attendance and assessments; parents see children, fees and report cards; HR runs leave and payslips.",
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
        "Work is organised around the matter file. Clients, documents, tasks and billing sit on that file, with permissions so candidate attorneys, secretaries and directors are not the same role.",
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
        "A custom business system fitted to the parlour’s administration. Exact screens are confirmed in a demonstration because the product source is not in this public repository.",
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
        "Residents register, report faults, book queues and view bills. Staff use an administration console for the same tickets, meter readings, notices, disputes and reports.",
        "Codebase exists. A hosted demo should be linked once a non-admin staging URL is available.",
    )


if __name__ == "__main__":
    build_work()
    print("work done")
