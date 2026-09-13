#!/usr/bin/env python3
"""Shared HTML chrome for the Cyber Developers static site."""
from __future__ import annotations

import html
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://www.cyberdevelopers.co.za"
ORG_NAME = "Cyber Developers"
ORG_DESC = (
    "Cyber Developers is a South African custom software development company "
    "building business systems, web applications, mobile apps, workflow automation "
    "and integrations."
)
EMAIL = "sales@cyberdevelopers.co.za"
PHONE_DISPLAY = "087 550 1813"
PHONE_E164 = "+27875501813"
ADDRESS_LINE = "357 Oak Ave, Ferndale, Randburg"
FORM_ACTION = "https://formsubmit.co/" + EMAIL

NAV = [
    ("/", "Home"),
    ("/services/", "Services"),
    ("/solutions/", "Solutions"),
    ("/our-work/", "Our Work"),
    ("/industries/", "Industries"),
    ("/about/", "About"),
    ("/knowledge-centre/", "Knowledge Centre"),
    ("/contact/", "Contact"),
]

TECHS = [
    "React",
    "Next.js",
    "JavaScript",
    "TypeScript",
    "Node.js",
    "Python",
    "C#",
    "ASP.NET Core",
    "Azure",
    "PostgreSQL",
    "SQL Server",
    "Prisma",
    "Firebase",
    "APIs",
    "Cloudflare",
]


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def icon(name: str) -> str:
    icons = {
        "code": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><polyline points="8 6 2 12 8 18"/><polyline points="16 6 22 12 16 18"/></svg>',
        "layers": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>',
        "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/></svg>',
        "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/></svg>',
        "flow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="6" cy="6" r="3"/><circle cx="18" cy="12" r="3"/><circle cx="6" cy="18" r="3"/><path d="M9 7h5a4 4 0 0 1 4 4M9 17h5a4 4 0 0 0 4-4"/></svg>',
        "spark": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 2v6M12 16v6M2 12h6M16 12h6M5 5l4 4M15 15l4 4M19 5l-4 4M9 15l-4 4"/></svg>',
        "plug": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M9 7v4a3 3 0 0 0 6 0V7M8 7h8M12 14v7"/></svg>',
        "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 12 9 17 20 6"/></svg>',
    }
    return icons.get(name, icons["code"])


def ld_json(data: dict) -> str:
    return json.dumps(data, ensure_ascii=True)


def org_schema() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": SITE + "/#organization",
        "name": ORG_NAME,
        "legalName": "Cyber Developers (Pty) Ltd",
        "url": SITE + "/",
        "logo": SITE + "/favicon.png",
        "email": EMAIL,
        "telephone": PHONE_E164,
        "description": ORG_DESC,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "357 Oak Ave, Ferndale",
            "addressLocality": "Randburg",
            "addressRegion": "Gauteng",
            "addressCountry": "ZA",
        },
        "areaServed": {"@type": "Country", "name": "South Africa"},
        "sameAs": [
            "https://www.facebook.com/cyberdevelop",
            "https://www.instagram.com/cyber.developers/",
            "https://x.com/cyberdeveloper3",
        ],
        "knowsAbout": [
            "Custom software development",
            "Business systems",
            "Web applications",
            "Mobile applications",
            "Workflow automation",
            "Systems integration",
        ],
    }


def website_schema() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": SITE + "/#website",
        "url": SITE + "/",
        "name": ORG_NAME,
        "description": ORG_DESC,
        "publisher": {"@id": SITE + "/#organization"},
        "inLanguage": "en-ZA",
    }


def breadcrumb_schema(crumbs: list[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i + 1,
                "name": name,
                "item": SITE + url,
            }
            for i, (url, name) in enumerate(crumbs)
        ],
    }


def service_schema(name: str, desc: str, url: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": name,
        "description": desc,
        "url": SITE + url,
        "provider": {"@id": SITE + "/#organization"},
        "areaServed": {"@type": "Country", "name": "South Africa"},
        "serviceType": name,
    }


def faq_schema(items: list[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in items
        ],
    }


def article_schema(title: str, desc: str, url: str, image: str, modified: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc,
        "image": SITE + image,
        "datePublished": modified,
        "dateModified": modified,
        "author": {"@type": "Organization", "name": ORG_NAME, "url": SITE + "/"},
        "publisher": {"@id": SITE + "/#organization"},
        "mainEntityOfPage": SITE + url,
        "inLanguage": "en-ZA",
    }


def asset(prefix: str, name: str) -> str:
    return f"{prefix}assets/{name}"


def head(
    prefix: str,
    title: str,
    description: str,
    canonical: str,
    crumbs: list[tuple[str, str]],
    extra_schema: list[dict] | None = None,
    og_type: str = "website",
    image: str = "/assets/img/og-default.webp",
) -> str:
    schemas = [org_schema(), website_schema(), breadcrumb_schema(crumbs)]
    if extra_schema:
        schemas.extend(extra_schema)
    schema_tags = "\n".join(
        f'<script type="application/ld+json">{ld_json(s)}</script>' for s in schemas
    )
    return f"""<!DOCTYPE html>
<html lang="en-ZA">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  <link rel="canonical" href="{SITE}{canonical}">
  <link rel="icon" type="image/png" href="{prefix}favicon.png">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <meta name="theme-color" content="#0b1220">
  <meta property="og:type" content="{og_type}">
  <meta property="og:site_name" content="{ORG_NAME}">
  <meta property="og:locale" content="en_ZA">
  <meta property="og:url" content="{SITE}{canonical}">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(description)}">
  <meta property="og:image" content="{SITE}{image}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(description)}">
  <meta name="twitter:image" content="{SITE}{image}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{asset(prefix, 'css/main.css')}">
  <link rel="stylesheet" href="{asset(prefix, 'css/premium.css')}">
  {schema_tags}
</head>
"""


def header(prefix: str, current: str) -> str:
    items = []
    for url, label in NAV:
        cur = ' aria-current="page"' if url == current else ""
        items.append(f'<a href="{url}"{cur}>{esc(label)}</a>')
    return f"""<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container nav">
    <a class="logo" href="/">
      <span class="logo-lockup">
        <span><span>Cyber</span> Developers</span>
        <small>Custom software · South Africa</small>
      </span>
    </a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-label="Open menu"><span></span></button>
    <nav class="nav-links" aria-label="Primary">
      {''.join(items)}
    </nav>
  </div>
</header>
"""


def footer(prefix: str) -> str:
    year = date.today().year
    return f"""<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      <a class="logo" href="/"><span>Cyber</span> Developers</a>
      <p style="margin-top:1rem">{esc(ORG_DESC)}</p>
      <p style="margin-top:1rem">Software built around your business.</p>
    </div>
    <div>
      <h4>Company</h4>
      <ul>
        <li><a href="/about/">About</a></li>
        <li><a href="/our-work/">Our Work</a></li>
        <li><a href="/knowledge-centre/">Knowledge Centre</a></li>
        <li><a href="/contact/">Contact</a></li>
        <li><a href="/privacy/">Privacy Policy</a></li>
      </ul>
    </div>
    <div>
      <h4>Services</h4>
      <ul>
        <li><a href="/services/custom-software-development/">Custom Software</a></li>
        <li><a href="/services/web-application-development/">Web Applications</a></li>
        <li><a href="/services/mobile-app-development/">Mobile Apps</a></li>
        <li><a href="/services/business-systems/">Business Systems</a></li>
        <li><a href="/services/ai-business-automation/">AI &amp; Automation</a></li>
      </ul>
    </div>
    <div>
      <h4>Contact</h4>
      <ul>
        <li><a href="mailto:{EMAIL}" data-track="email_clicked">{EMAIL}</a></li>
        <li><a href="tel:{PHONE_E164}" data-track="phone_clicked">{PHONE_DISPLAY}</a></li>
        <li>{esc(ADDRESS_LINE)}</li>
      </ul>
    </div>
  </div>
  <div class="container footer-bottom">
    <p>&copy; {year} Cyber Developers (Pty) Ltd. All rights reserved.</p>
    <p>Custom software &amp; business systems · South Africa</p>
  </div>
</footer>
<script src="{asset(prefix, 'js/config.js')}"></script>
<script src="{asset(prefix, 'js/main.js')}" defer></script>
</body>
</html>
"""


def crumbs_html(crumbs: list[tuple[str, str]]) -> str:
    parts = []
    for i, (url, name) in enumerate(crumbs):
        if i < len(crumbs) - 1:
            parts.append(f'<a href="{url}">{esc(name)}</a><span>/</span>')
        else:
            parts.append(f"<span>{esc(name)}</span>")
    return f'<nav class="breadcrumbs" aria-label="Breadcrumb">{"".join(parts)}</nav>'


def cta_band(
    heading="Discuss a software project",
    copy="Tell us what the software needs to do. We will say whether we should build it, adapt something we already have, or leave it.",
    primary=("Request a Consultation", "/contact/"),
    secondary=("View Our Work", "/our-work/"),
) -> str:
    sec = (
        f'<a class="btn btn-secondary" href="{secondary[1]}">{esc(secondary[0])}</a>'
        if secondary
        else ""
    )
    return f"""<section class="section"><div class="container">
  <div class="cta-band">
    <div>
      <h2>{esc(heading)}</h2>
      <p>{esc(copy)}</p>
    </div>
    <div class="actions">
      <a class="btn btn-primary btn-lg" href="{primary[1]}" data-track="consultation_requested" data-track-location="cta">{esc(primary[0])}</a>
      {sec}
    </div>
  </div>
</div></section>"""


def enquiry_form(
    kind: str = "project_enquiry",
    subject: str = "New project enquiry | Cyber Developers",
    cta: str = "Discuss Your Project",
) -> str:
    next_url = SITE + "/contact/thank-you/"
    return f"""<form class="form" id="enquiry-form" action="{FORM_ACTION}" method="POST" data-enquiry="{kind}">
  <input type="hidden" name="_subject" value="{esc(subject)}">
  <input type="hidden" name="_template" value="table">
  <input type="hidden" name="_captcha" value="true">
  <input type="hidden" name="_next" value="{next_url}">
  <input type="hidden" name="form_type" value="{kind}">
  <div class="hp" aria-hidden="true"><label>Website <input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
  <p class="form-error" role="alert"></p>
  <div class="form-row">
    <div class="field"><label for="name">Name</label><input id="name" name="name" required autocomplete="name"></div>
    <div class="field"><label for="company">Company</label><input id="company" name="company" autocomplete="organization"></div>
  </div>
  <div class="form-row">
    <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" required autocomplete="email"></div>
    <div class="field"><label for="phone">Phone</label><input id="phone" name="phone" type="tel" autocomplete="tel"></div>
  </div>
  <div class="form-row">
    <div class="field">
      <label for="project_type">Project Type</label>
      <select id="project_type" name="project_type" required>
        <option value="" disabled selected>Select a type</option>
        <option>Custom Software</option>
        <option>Web Application</option>
        <option>Mobile App</option>
        <option>Business Management System</option>
        <option>AI / Automation</option>
        <option>Systems Integration</option>
        <option>Existing System Support</option>
        <option>Other</option>
      </select>
    </div>
    <div class="field">
      <label for="budget">Estimated Budget <span class="optional">(optional)</span></label>
      <select id="budget" name="budget">
        <option value="" selected>Not Sure Yet</option>
        <option>Under R25,000</option>
        <option>R25,000 – R50,000</option>
        <option>R50,000 – R100,000</option>
        <option>R100,000 – R250,000</option>
        <option>R250,000+</option>
      </select>
    </div>
  </div>
  <div class="field">
    <label for="project_description">Project Description</label>
    <textarea id="project_description" name="project_description" required placeholder="What should the software do, who will use it, and what systems should it connect to?"></textarea>
  </div>
  <button class="btn btn-primary btn-lg btn-block" type="submit">{esc(cta)}</button>
  <p class="form-note">We’ll reply to your enquiry by email. You can also call {PHONE_DISPLAY}.</p>
</form>"""


def faq_html(items: list[tuple[str, str]]) -> str:
    blocks = [
        f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in items
    ]
    return f'<div class="faq">{"".join(blocks)}</div>'


def render_page(
    rel_path: str,
    title: str,
    description: str,
    canonical: str,
    crumbs: list[tuple[str, str]],
    body: str,
    extra_schema: list[dict] | None = None,
    og_type: str = "website",
    image: str = "/assets/img/og-default.webp",
    current: str | None = None,
) -> str:
    prefix = "" if rel_path == "index.html" else "../" * len(Path(rel_path).parent.parts)
    nav_current = current if current is not None else canonical
    return (
        head(prefix, title, description, canonical, crumbs, extra_schema, og_type, image)
        + header(prefix, nav_current)
        + f'<main id="main">{body}</main>'
        + footer(prefix)
    )


def write_page(rel: str, content: str) -> None:
    dest = ROOT / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content, encoding="utf-8")
    print("wrote", rel)


def redirect_page(target: str, title: str = "Redirecting") -> str:
    return f"""<!DOCTYPE html>
<html lang="en-ZA">
<head>
  <meta charset="UTF-8">
  <title>{esc(title)}</title>
  <link rel="canonical" href="{SITE}{target}">
  <meta http-equiv="refresh" content="0; url={target}">
  <script>location.replace({json.dumps(target)});</script>
</head>
<body>
  <p>This page has moved to <a href="{target}">{SITE}{target}</a>.</p>
</body>
</html>
"""
