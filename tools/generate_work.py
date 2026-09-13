#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from site_lib import crumbs_html, cta_band, esc
from generate_core import emit, bullets
from graphics import (
    showcase, shot, shot_gallery, SHOTS,
    vayasa_map, fluxmove_map, tshira_map, school_map,
    lawyer_map, funeral_map, municipality_map,
)


def og_for(key: str) -> str:
    return f"/assets/img/projects/{SHOTS[key]['file']}"


def case_study(
    slug,
    title,
    h1,
    description,
    industry,
    platform,
    overview,
    problem,
    solution,
    features,
    tech,
    approach,
    status,
    shots,
    extras="",
    live_url=None,
    og=None,
    meta_title=None,
):
    canonical = f"/our-work/{slug}/"
    live = ""
    if live_url:
        host = live_url.replace("https://", "").replace("www.", "")
        live = (
            f'<p class="hero-actions" style="margin-top:1rem">'
            f'<a class="btn btn-secondary" href="{live_url}" rel="noopener">View Demo</a>'
            f"</p>"
            f'<p class="muted">Public site: <a href="{live_url}">{esc(host)}</a>. '
            f"A public URL is not a claim about commercial scale.</p>"
        )
    primary = shots[0]
    gallery = shot_gallery(shots[1:]) if len(shots) > 1 else ""
    body = f"""
<section class="page-hero"><div class="container page-hero-grid">
  <div>
    {crumbs_html([("/", "Home"), ("/our-work/", "Our Work"), (canonical, title)])}
    <p class="eyebrow">{esc(industry)} · {esc(platform)}</p>
    <h1>{esc(h1)}</h1>
    <p class="lead">{esc(overview)}</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="/contact/">Build Something Similar</a>
      <a class="btn btn-secondary" href="/contact/">Discuss Your Requirements</a>
    </div>
    {live}
  </div>
  <aside class="page-hero-visual reveal">{shot(primary, eager=True)}</aside>
</div></section>
<section class="section"><div class="container case-layout">
  <div class="prose">
  <h2>Challenge</h2>
  <p>{esc(problem)}</p>
  <h2>Solution</h2>
  <p>{esc(solution)}</p>
  <p>{esc(approach)}</p>
  <h2>Key capabilities</h2>
  {bullets(features)}
  <h2>Technology</h2>
  <p class="tech-inline">{" · ".join(esc(t) for t in tech)}</p>
  <h2>Current status</h2>
  <p>{esc(status)}</p>
  {extras}
  </div>
  <aside class="case-visual">{shot(primary)}</aside>
</div></section>
{"<section class='section section-alt'><div class='container'><h2>Interface</h2>" + gallery + "</div></section>" if gallery else ""}
<section class="section"><div class="container">
  <p class="hero-actions">
    <a class="btn btn-primary" href="/contact/">Build Something Similar</a>
    <a class="btn btn-secondary" href="/our-work/">All work</a>
  </p>
</div></section>
"""
    emit(
        f"our-work/{slug}/index.html",
        meta_title or f"{title} | Cyber Developers",
        description,
        canonical,
        [("/", "Home"), ("/our-work/", "Our Work"), (canonical, title)],
        body,
        current="/our-work/",
        priority="0.75",
        image=og or og_for(primary),
    )


def build_work():
    emit(
        "our-work/index.html",
        "Our Work | Custom Software Projects South Africa | Cyber Developers",
        "Software Cyber Developers has actually built: Tshira, SmartCity Muni, VayaSA, FluxMove, LawTech SA, Legacy Care and Smart School/College.",
        "/our-work/",
        [("/", "Home"), ("/our-work/", "Our Work")],
        f"""
<section class="page-hero"><div class="container">
  {crumbs_html([("/", "Home"), ("/our-work/", "Our Work")])}
  <h1>Software we've actually built.</h1>
  <p class="lead">Explore digital platforms, operational systems and industry-specific software designed and developed by Cyber Developers. These pages describe the products. They are not invented client deployments, testimonials or usage statistics.</p>
</div></section>
<section class="section"><div class="container">
  {showcase("/our-work/tshira-workflow-system/", "Tshira Workflow", "Enterprise · Workflow platform",
            "Case management, SLA monitoring, requisitions, billing, expenses, team access and operational reporting.",
            ["Workflow", "SLA", "Finance", "Audit"],
            tshira_map(), cta="View project")}
  {showcase("/our-work/municipality-platform/", "SmartCity Muni", "Government · Citizen services platform",
            "Citizen reporting, municipal services, alerts, queue booking and emergency access.",
            ["Citizen portal", "Fault reporting", "Alerts"],
            municipality_map(), reverse=True, cta="View project")}
  {showcase("/our-work/vayasa/", "VayaSA", "Transport · Passenger marketplace",
            "Ride sharing, bus tickets and taxi seats between South African cities.",
            ["Ride sharing", "Bus tickets", "Taxi bookings"],
            vayasa_map(), cta="View project")}
  {showcase("/our-work/fluxmove/", "FluxMove", "Logistics · Delivery marketplace",
            "Instant quotations, vehicle selection, booking and transport-provider workflows.",
            ["Live quotes", "Vehicles", "Booking"],
            fluxmove_map(), reverse=True, cta="View project")}
  {showcase("/our-work/school-lms/", "Smart School/College", "Education · School management platform",
            "Role-based portals for South African schools, colleges and TVET institutions.",
            ["Admissions", "Attendance", "Finance"],
            school_map(), cta="View project")}
  {showcase("/our-work/lawyer-management-system/", "LawTech SA", "Legal · Practice management",
            "Clients, matters, invoicing, fee book, trust accounts and debt recovery.",
            ["Clients", "Matters", "Trust", "Invoices"],
            lawyer_map(), reverse=True, cta="View project")}
  {showcase("/our-work/funeral-parlour-system/", "Legacy Care", "Funeral · Business platform",
            "Members, policies, premium collections, claims, funeral operations and fleet.",
            ["Members", "Collections", "Claims", "Operations"],
            funeral_map(), cta="View project")}
</div></section>
<section class="section"><div class="container">
  <p class="muted">A separate student accommodation management codebase also exists. Ask if that operational area is relevant.</p>
</div></section>
{cta_band("Need something in this shape?", "Describe the process. We will tell you whether an existing system is close, or whether to design a new one.", primary=("Discuss Your Project", "/contact/"))}
""",
        current="/our-work/",
        priority="0.9",
        image=og_for("tshira-dashboard"),
    )

    case_study(
        "vayasa",
        "VayaSA",
        "VayaSA",
        "VayaSA is a South African ride sharing and passenger transport marketplace built by Cyber Developers.",
        "Transport & Mobility",
        "Passenger transport marketplace",
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
        "Passengers search ride shares, bus tickets and taxi seats. Drivers and operators upload documents, then an admin console handles approvals and payouts.",
        "A production URL is published at vayasa.co.za. Treat live commercial metrics as unpublished.",
        ["vayasa-home", "vayasa-search", "vayasa-routes"],
        live_url="https://www.vayasa.co.za",
        meta_title="VayaSA Transport Marketplace | Cyber Developers",
    )

    case_study(
        "fluxmove",
        "FluxMove",
        "FluxMove",
        "FluxMove is a South African delivery marketplace built by Cyber Developers for freight bookings and verified drivers.",
        "Logistics & Delivery",
        "Logistics marketplace",
        "FluxMove is a nationwide delivery marketplace: customers get an instant quote, book a move, and verified drivers with bakkies, vans or trucks accept jobs.",
        "Moving goods across South Africa usually means phoning around for a vehicle. The software problem is matching a booking to a verified driver and a suitable vehicle type, then keeping status visible.",
        "A web platform for customers, drivers and admins, with live quotation, vehicle types and an optional Expo driver app for on-the-road steps.",
        [
            "Live quotation with distance, vehicle type and urgency.",
            "Customer booking with pickup/drop-off in South Africa and ZAR estimates.",
            "Driver verification documents and admin approval.",
            "Availability, open jobs and accept flow.",
            "Vehicle types from motorcycles through heavy equipment transport.",
            "Business accounts, ratings, disputes and support tickets in the schema.",
            "Driver mobile app module for GPS, proof and OTP on the road.",
        ],
        ["Next.js", "TypeScript", "PostgreSQL", "Prisma", "Tailwind CSS"],
        "A customer enters pickup, drop-off, vehicle and timing. The quote engine returns a ZAR estimate. Verified drivers see open jobs. Administrators review provider applications.",
        "A public site is published at fluxmove.co.za. No user or GMV figures are stated here.",
        ["fluxmove-quote", "fluxmove-hero", "fluxmove-vehicles"],
        live_url="https://fluxmove.co.za",
        meta_title="FluxMove Logistics Platform | Cyber Developers",
    )

    case_study(
        "tshira-workflow-system",
        "Tshira Workflow System",
        "Tshira Workflow System",
        "Tshira is a multi-province workflow system built by Cyber Developers for cases, field collection, review and invoicing.",
        "Enterprise / Professional Services",
        "Business workflow platform",
        "Tshira is a workflow management system for coordinating cases, client work, field data collection, document review, requisitions, expenses and invoicing across provinces.",
        "When case work is split between head office, provincial coordinators and field officers, status disappears into email. Finance also needs a hard rule: do not invoice unfinished work.",
        "A role-based Next.js application with a strict case lifecycle, separate requisition vs expense flows, SLA-aware reporting, and invoice generation gated on case status.",
        [
            "Roles: admin, provincial coordinator, data collection officer, business consultant, reviewer, finance.",
            "Sequential case statuses from intake to paid/closed, including return-for-correction paths.",
            "Clients, documents, case history and notifications.",
            "Requisitions for space/visit clearance versus expenses with receipt upload.",
            "Billing queue, sequential invoice numbers, PDF/print/email of invoices.",
            "SLA monitoring and management reports.",
            "Team management and audit trail.",
        ],
        ["Next.js", "TypeScript", "PostgreSQL", "Prisma", "NextAuth"],
        "A case is received, assigned by province, collected in the field, checked, reviewed and only then invoiced. Requisitions happen before spending; expenses are claimed afterwards.",
        "Described here from the application source and user manual. No client performance claims are added.",
        ["tshira-dashboard", "tshira-reports"],
        meta_title="Tshira Workflow System | Custom Workflow Software | Cyber Developers",
    )

    case_study(
        "school-lms",
        "Smart School/College",
        "Smart School/College (SchoolHub SA)",
        "SchoolHub SA is Cyber Developers’ school management system for South African schools, colleges and TVETs.",
        "Education",
        "School and college management platform",
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
        "Active codebase. The portal image on this page is the public sign-in. Additional operational screens are shown in a demo.",
        ["school-portal"],
        meta_title="School Management System | Cyber Developers",
    )

    case_study(
        "lawyer-management-system",
        "LawTech SA",
        "LawTech SA",
        "LawTech SA is practice management software by Cyber Developers covering clients, matters, invoicing, trust accounts and debt recovery.",
        "Legal",
        "Legal practice management platform",
        "LawTech SA is a practice management system for law firms: clients, matters, fee book, invoices, trust accounts and debt recovery, with a firm dashboard for the numbers operators actually use.",
        "Legal work fails operationally when files, deadlines and billing live in different places, and when every user has the same access.",
        "A business system organised around the matter, with role-based access and billing against completed work.",
        [
            "Reception and client management.",
            "Cases / matters.",
            "Fee book.",
            "Invoices.",
            "Trust accounts.",
            "Debt collection.",
            "Firm dashboard for clients, active matters, pending invoices, trust balance and debt recovery.",
        ],
        ["TypeScript", "Next.js", "PostgreSQL", "APIs"],
        "Work is organised around the matter file. Clients, billing and trust money sit on that file, with permissions so candidate attorneys, secretaries and directors are not the same role.",
        "Available for demonstration. The screenshot is the firm dashboard, not a login screen.",
        ["lawtech-dashboard"],
        meta_title="LawTech SA Legal Management System | Cyber Developers",
    )

    case_study(
        "funeral-parlour-system",
        "Legacy Care",
        "Legacy Care",
        "Legacy Care is funeral business management software developed by Cyber Developers for South African funeral operations.",
        "Funeral Services",
        "Funeral business platform",
        "Legacy Care is management software for funeral businesses: members, policy products, premium collections, arrears, claims, funeral operations, mortuary, inventory, fleet and finance.",
        "Funeral businesses combine records, family communication and administration. Off-the-shelf tools rarely match the parlour’s file.",
        "A custom business platform with a management dashboard, collection trends and operational modules for the parlour and related services.",
        [
            "Member management and policy products.",
            "Premium collections, billing batches and arrears.",
            "Claims processing.",
            "Funeral operations, obituaries and memorials.",
            "Mortuary register.",
            "Inventory / stock and fleet / vehicles.",
            "Finance reporting on the management dashboard.",
        ],
        ["Custom business system"],
        "Operators work from a shared dashboard. Collections, arrears, claims and operations are modules of the same application rather than separate spreadsheets.",
        "Demo on request. Screens on this page are from the live interface.",
        ["legacy-dashboard", "legacy-collections"],
        meta_title="Legacy Care Funeral Management Platform | Cyber Developers",
    )

    case_study(
        "municipality-platform",
        "SmartCity Muni",
        "SmartCity Muni",
        "SmartCity Muni is a municipality platform by Cyber Developers: citizen services, fault reporting, alerts, queues and emergency access.",
        "Government & Municipalities",
        "Municipal digital services platform",
        "SmartCity Muni is a React application for municipal citizen services: report issues, pay attention to alerts, book queues, browse local services and reach emergency numbers.",
        "Residents still queue, phone or arrive in person for issues that a verified account could track. Staff need a back office for the same tickets, bills and notices.",
        "A citizen app and an admin console sharing services for billing, documents, meter readings, queues, reports and audit.",
        [
            "Citizen homepage and service directory.",
            "Issue reporting and ticket tracking (water leaks, potholes, outages and related faults).",
            "Queue booking.",
            "Loadshedding and public alerts.",
            "Jobs, tenders and local business directory.",
            "Emergency information for SAPS, ambulance, fire and disaster management.",
            "Billing, meter readings, notices, disputes, audit and reporting on the administration side.",
        ],
        ["React", "JavaScript", "Vite"],
        "Residents report faults, book queues and view services. Staff use an administration console for the same tickets, meter readings, notices, disputes and reports.",
        "Codebase exists. The screens on this page are from the citizen application.",
        ["smartcity-home", "smartcity-services", "smartcity-report", "smartcity-emergency"],
        meta_title="SmartCity Municipal Services Platform | Cyber Developers",
    )


if __name__ == "__main__":
    build_work()
    print("work done")
