#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path
from datetime import date

sys.path.insert(0, str(Path(__file__).resolve().parent))
from site_lib import crumbs_html, article_schema, esc
from generate_core import emit, TODAY

ARTICLES = [
    {
        "slug": "how-much-does-custom-software-development-cost-in-south-africa",
        "title": "How Much Does Custom Software Development Cost in South Africa?",
        "description": "What actually drives the cost of custom software in South Africa, without invented averages. Scope, users, integrations and support.",
        "image": "/assets/img/og-default.webp",
        "alt": "Cyber Developers — custom software, South Africa",
    },
    {
        "slug": "custom-software-vs-off-the-shelf-software",
        "title": "Custom Software vs Off-the-Shelf Software: Which Is Better?",
        "description": "When to buy a packaged product and when to build software around the business process.",
        "image": "/assets/img/og-default.webp",
        "alt": "Cyber Developers — custom software, South Africa",
    },
    {
        "slug": "how-to-choose-a-software-development-company-in-south-africa",
        "title": "How to Choose a Software Development Company in South Africa",
        "description": "A practical checklist for South African organisations hiring a software partner, including how to avoid brochure claims.",
        "image": "/assets/img/og-default.webp",
        "alt": "Cyber Developers — custom software, South Africa",
    },
    {
        "slug": "what-is-a-business-management-system",
        "title": "What Is a Business Management System?",
        "description": "A clear definition of business management systems: records, roles, money and reporting in one operational application.",
        "image": "/assets/img/og-default.webp",
        "alt": "Cyber Developers — custom software, South Africa",
    },
    {
        "slug": "how-workflow-automation-can-reduce-manual-admin",
        "title": "How Workflow Automation Can Reduce Manual Admin",
        "description": "How named stages, owners and finance locks reduce email-driven administration.",
        "image": "/assets/img/og-default.webp",
        "alt": "Cyber Developers — custom software, South Africa",
    },
    {
        "slug": "school-management-software-features",
        "title": "School Management Software: What Features Should Schools Look For?",
        "description": "Features South African schools should look for in management software, based on a real school platform — not a generic LMS checklist.",
        "image": "/assets/img/og-default.webp",
        "alt": "Cyber Developers — custom software, South Africa",
    },
    {
        "slug": "what-does-it-cost-to-build-a-mobile-app-in-south-africa",
        "title": "What Does It Cost to Build a Mobile App in South Africa?",
        "description": "Cost drivers for mobile apps in South Africa: platforms, backend, offline needs and store listing — without fake quotes.",
        "image": "/assets/img/og-default.webp",
        "alt": "Cyber Developers — custom software, South Africa",
    },
    {
        "slug": "custom-crm-vs-salesforce-microsoft-dynamics",
        "title": "Custom CRM vs Salesforce/Microsoft Dynamics: When Does Custom Make Sense?",
        "description": "When a custom CRM is justified, and when Salesforce or Dynamics is the more honest recommendation.",
        "image": "/assets/img/og-default.webp",
        "alt": "Cyber Developers — custom software, South Africa",
    },
]


def article_page(meta: dict, body_html: str) -> None:
    canonical = f"/knowledge-centre/{meta['slug']}/"
    schema = article_schema(meta["title"], meta["description"], canonical, meta["image"], TODAY)
    body = f"""
<article class="page-hero"><div class="container prose">
  {crumbs_html([("/", "Home"), ("/knowledge-centre/", "Knowledge Centre"), (canonical, meta["title"])])}
  <h1>{esc(meta["title"])}</h1>
  <p class="article-meta">Cyber Developers · Updated {TODAY} · South Africa</p>
  {body_html}
</div></article>
"""
    emit(
        f"knowledge-centre/{meta['slug']}/index.html",
        f"{meta['title']} | Cyber Developers",
        meta["description"],
        canonical,
        [("/", "Home"), ("/knowledge-centre/", "Knowledge Centre"), (canonical, meta["title"])],
        body,
        extra=[schema],
        current="/knowledge-centre/",
        image=meta["image"],
        og_type="article",
        priority="0.65",
    )


def build_knowledge():
    cards = []
    for a in ARTICLES:
        cards.append(
            f"""<a href="/knowledge-centre/{a['slug']}/">
              <h3>{esc(a['title'])}</h3>
              <p>{esc(a['description'])}</p>
              <span class="more">Read</span>
            </a>"""
        )
    emit(
        "knowledge-centre/index.html",
        "Knowledge Centre | Cyber Developers",
        "Practical guides on custom software, business systems, school software and software partners in South Africa.",
        "/knowledge-centre/",
        [("/", "Home"), ("/knowledge-centre/", "Knowledge Centre")],
        f"""
<section class="page-hero"><div class="container">
  {crumbs_html([("/", "Home"), ("/knowledge-centre/", "Knowledge Centre")])}
  <h1>Knowledge Centre</h1>
  <p class="lead">Practical writing for people buying software in South Africa. These articles explain decisions. They do not invent industry statistics, average ROI, or unnamed case results.</p>
</div></section>
<section class="section"><div class="container" style="max-width:48rem"><div class="row-list">{''.join(cards)}</div></div></section>
""",
        current="/knowledge-centre/",
        priority="0.7",
    )

    article_page(ARTICLES[0], """
<p>There is no honest single price for custom software in South Africa. Anyone publishing a national average without a defined scope is selling a headline. Cost follows the system you need, not the industry you belong to.</p>
<h2>What you are actually paying for</h2>
<p>A custom system is not a website quote. You are paying for discovery, a data model, interfaces for each role, integrations, testing, deployment and a period of support. If any of those are missing from a quote, they will reappear later as change requests.</p>
<h2>The variables that move the number</h2>
<ul>
<li><strong>Users and roles.</strong> One internal operator is not the same as parents, teachers, finance and HR on separate portals.</li>
<li><strong>Records and history.</strong> A job card is cheaper than a ledger with invoices, receipts, credit notes and audit.</li>
<li><strong>Integrations.</strong> Payments, SMS, identity and existing SQL databases each add design and failure handling.</li>
<li><strong>Mobile.</strong> A responsive web app is a different effort from iOS, Android and a driver workflow with photos and GPS.</li>
<li><strong>Compliance.</strong> POPIA, backups, permissions and hosting in a defined region add work that a demo ignores.</li>
</ul>
<h2>How we talk about budget</h2>
<p>On our enquiry form we use ranges — under R25,000, R25,000–R50,000, R50,000–R100,000, R100,000–R250,000, R250,000+ — so a first conversation can be honest. Those bands are not a price list. A small workflow tool and a school platform are not the same project.</p>
<h2>What we will not do</h2>
<p>We will not publish a fake “average project value” or a percentage saving attributed to unnamed clients. If you want a number, describe the process. The quote is the artefact of that description.</p>
<p><a href="/contact/">Discuss Your Project</a> or read <a href="/knowledge-centre/custom-software-vs-off-the-shelf-software/">custom versus off-the-shelf</a>.</p>
""")

    article_page(ARTICLES[1], """
<p>Neither custom software nor packaged software is universally better. The useful question is which one matches the process you cannot change without damaging the business.</p>
<h2>When off-the-shelf is the right answer</h2>
<p>Buy a product when your process is common, the vendor is still trading, and the exceptions are minor. Accounting, email and standard HR are usually in this category. Forcing a custom rebuild of a solved problem wastes time.</p>
<h2>When custom is the right answer</h2>
<p>Build when the objects are specific — matters, learners, funeral files, municipal tickets, provincial case work — and staff already work around the packaged tool. Those workarounds are the real specification.</p>
<h2>A hybrid that is often missed</h2>
<p>Many Cyber Developers engagements start from a system we already built (school, workflow, logistics, municipality) and customise it. That is not a marketplace plugin, and it is not a greenfield rewrite. It is usually the shortest path that still fits.</p>
<h2>Decision test</h2>
<p>Write the three reports a manager asks for every week. If a packaged product can produce them without a shadow spreadsheet, buy it. If the spreadsheet is the real system, you are already in custom territory — whether or not you have admitted it.</p>
""")

    article_page(ARTICLES[2], """
<p>Choosing a software company in South Africa is harder than comparing homepage slogans. Similar-sounding names and generic agency copy are common. Judge the firm by systems it can actually show you.</p>
<h2>Ask to see a system, not a slide</h2>
<p>Request a walkthrough of software that resembles yours. If the portfolio is only logos, stock photographs and “89+ global clients”, treat that as advertising. Ask for hosting arrangements, who writes the code, and what happens after go-live.</p>
<h2>Questions that surface reality</h2>
<ul>
<li>Who will actually write the code, and where does hosting live?</li>
<li>What happens after go-live — backups, user changes, who holds the keys?</li>
<li>Which integrations have they shipped (payments, SMS, identity), not merely listed?</li>
<li>Can they say no to an AI feature that does not belong in the process?</li>
</ul>
<h2>Local knowledge without theatrics</h2>
<p>South African delivery usually involves POPIA, local payment methods, ID numbers, and users on mixed devices. A company that has already modelled those constraints will spend less of your budget discovering them.</p>
<p>Cyber Developers is a South African custom software development company building business systems, web applications, mobile apps, workflow automation and integrations. When you are ready, <a href="/contact/">discuss the project</a> with the process, not a slogan, in the first message.</p>
""")

    article_page(ARTICLES[3], """
<p>A business management system is the operational application an organisation uses to keep records, take action, and report. It is not a website, and it is not automatically an ERP suite.</p>
<h2>The usual pieces</h2>
<ul>
<li>People: staff, customers, students, residents or clients.</li>
<li>Work: jobs, cases, classes, bookings or tickets, each with a status.</li>
<li>Money: invoices, receipts, statements, payments.</li>
<li>Control: roles, permissions, audit.</li>
</ul>
<p>If those four sit in four tools, managers assemble the truth by hand. The system’s job is to make that assembly unnecessary.</p>
<h2>What it is not</h2>
<p>A business management system is not a poster about changing how the company works. It is closer to a well-run filing office that several people can use at once without overwriting each other.</p>
<p>See also <a href="/services/business-systems/">business systems</a> and <a href="/solutions/school-management-system/">school management</a> as a concrete example of the pattern.</p>
""")

    article_page(ARTICLES[4], """
<p>Manual admin is usually a workflow problem wearing an email costume. Work arrives, someone forwards it, someone else asks for a document, finance invoices too early or too late, and nobody can point to a status.</p>
<h2>What automation should mean</h2>
<p>Named stages. A named owner. A rule for when the record may move. Documents attached to the record, not to a side chat. Finance blocked until the work is actually complete.</p>
<p>The Tshira workflow system uses that pattern: intake, provincial assignment, field collection, quality check, consultancy, review, invoicing, payment, closure — with requisitions before spending and expenses after, so the two are not confused.</p>
<h2>What it should not mean</h2>
<p>A chatbot that apologises while the queue stays invisible. A notification storm. RPA clicking through a website you do not control.</p>
<p>If your team’s week is mostly chasing status, start with <a href="/services/workflow-automation/">workflow automation</a> before you buy a more fashionable label.</p>
""")

    article_page(ARTICLES[5], """
<p>School software is often sold as an LMS: video, quizzes, certificates. South African schools also need guardians, fees, attendance, staff leave and letters. If the product cannot produce a statement and a report card, it is only part of the job.</p>
<h2>Features that matter in practice</h2>
<ul>
<li>Student records and a guardian portal.</li>
<li>Attendance, with a way to notify home.</li>
<li>Academic sessions, classes, subjects, assessments.</li>
<li>Fees, invoices, receipts, debtors, local payment options.</li>
<li>HR, leave, payslips.</li>
<li>Email and SMS that the school controls.</li>
<li>Student cards, letters, reporting, backups.</li>
<li>Timetable links for online classes where the school actually runs them.</li>
</ul>
<p>Biometrics are optional hardware, not a magic checkbox. SA-SAMS imports can help a school that already lives there; they do not make a product an official department system.</p>
<p>Cyber Developers’ SchoolHub SA platform is built around that list. <a href="/solutions/school-management-system/">Read the solution page</a> or <a href="/contact/?intent=demo">request a demo</a>.</p>
""")

    article_page(ARTICLES[6], """
<p>A mobile app quote without a backend quote is incomplete. Most of the cost sits in accounts, data, notifications and the web console staff will actually use.</p>
<h2>Cost drivers</h2>
<ul>
<li>iOS, Android, or a well-made mobile web app first.</li>
<li>Whether the app is a thin client of an existing system or a new product.</li>
<li>Offline capture, GPS, photos, OTP and store listings.</li>
<li>Driver versus customer versus internal staff — three apps is three interfaces.</li>
</ul>
<p>Fluxmove, for example, is a web marketplace with an optional driver mobile module. That split is often cheaper and clearer than pretending every user needs a store app on day one.</p>
<p>We do not publish a fake “typical South African app costs Rx”. Use the optional budget ranges on the <a href="/contact/">enquiry form</a> and describe the jobs the app must perform.</p>
""")

    article_page(ARTICLES[7], """
<p>Salesforce and Microsoft Dynamics are capable platforms. Custom CRM is not a moral upgrade. It is a fit decision.</p>
<h2>Stay on a major CRM when</h2>
<p>Your objects are accounts, contacts, leads and opportunities. You want a marketplace of add-ons. You have administrators who will live in that ecosystem. Switching cost later is acceptable because the vendor is not going away next year.</p>
<h2>Build custom when</h2>
<p>The noun is not “opportunity”. It is a matter, a learner, a municipal ticket, a repair, a booking, a provincial case. The stages are yours. Reports that managers need cannot be twisted out of a generic pipeline without a parallel spreadsheet.</p>
<h2>The honest middle</h2>
<p>Sometimes the CRM is standard and the operational system is custom, talking over an API. That is a better architecture than stuffing a workshop’s entire process into a lead object.</p>
<p>Read <a href="/solutions/custom-crm-development/">custom CRM development</a> or <a href="/contact/">request a consultation</a> with the objects and stages written down.</p>
""")


if __name__ == "__main__":
    build_knowledge()
    print("knowledge done")
