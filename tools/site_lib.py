#!/usr/bin/env python3
"""Shared HTML chrome for the Cyber Developers static site."""
from __future__ import annotations

import hashlib
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
ADDRESS_LINE = "135 Rivonia Road, Sandton, Gauteng, South Africa"
ADDRESS_STREET = "135 Rivonia Road"
ADDRESS_LOCALITY = "Sandton"
ADDRESS_REGION = "Gauteng"
ADDRESS_COUNTRY = "ZA"
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

# (name, url) — used for both the visible footer icons and the schema sameAs.
SOCIAL = [
    ("Facebook", "https://www.facebook.com/cyberdevelop"),
    ("X", "https://x.com/cyberdeveloper3"),
    ("Instagram", "https://www.instagram.com/cyber.developers/"),
    ("LinkedIn", "https://www.linkedin.com/company/cyber-developerssa"),
    ("YouTube", "https://www.youtube.com/@cyberdevelopers-z1w2o"),
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


def social_icon(name: str) -> str:
    icons = {
        "Facebook": '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M24 12.073c0-6.627-5.373-12-12-12S0 5.446 0 12.073c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>',
        "X": '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>',
        "Instagram": '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163C8.741 0 8.332.014 7.052.072 2.695.272.273 2.69.073 7.052.014 8.332 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.332 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>',
        "LinkedIn": '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.225 0z"/></svg>',
        "YouTube": '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>',
    }
    return icons.get(name, "")


def social_links(prefix: str = "") -> str:
    links = "".join(
        f'<a href="{url}" class="social-link" target="_blank" rel="noopener noreferrer"'
        f' aria-label="{esc(ORG_NAME)} on {esc(name)}" data-track="social_clicked"'
        f' data-track-network="{esc(name.lower())}">{social_icon(name)}</a>'
        for name, url in SOCIAL
    )
    return f'<div class="footer-social" aria-label="Social media">{links}</div>'


def ld_json(data: dict) -> str:
    return json.dumps(data, ensure_ascii=True)


def postal_address() -> dict:
    return {
        "@type": "PostalAddress",
        "streetAddress": ADDRESS_STREET,
        "addressLocality": ADDRESS_LOCALITY,
        "addressRegion": ADDRESS_REGION,
        "addressCountry": ADDRESS_COUNTRY,
    }


def org_schema() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": ["Organization", "ProfessionalService"],
        "@id": SITE + "/#organization",
        "name": ORG_NAME,
        "legalName": "Cyber Developers (Pty) Ltd",
        "url": SITE + "/",
        "logo": SITE + "/assets/img/logo.png",
        "image": SITE + "/assets/img/og-default.webp",
        "email": EMAIL,
        "telephone": PHONE_E164,
        "description": ORG_DESC,
        "address": postal_address(),
        "areaServed": {"@type": "Country", "name": "South Africa"},
        "sameAs": [url for _, url in SOCIAL],
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


def article_schema(
    title: str,
    desc: str,
    url: str,
    image: str,
    modified: str,
    published: str | None = None,
) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc,
        "image": SITE + image,
        "datePublished": published or modified,
        "dateModified": modified,
        "author": {"@type": "Organization", "name": ORG_NAME, "url": SITE + "/"},
        "publisher": {"@id": SITE + "/#organization"},
        "mainEntityOfPage": SITE + url,
        "inLanguage": "en-ZA",
    }


_ASSET_VERSIONS: dict[str, str] = {}


def _asset_version(name: str) -> str:
    if name not in _ASSET_VERSIONS:
        path = ROOT / "assets" / name
        try:
            digest = hashlib.sha256(path.read_bytes()).hexdigest()[:8]
        except OSError:
            digest = ""
        _ASSET_VERSIONS[name] = digest
    return _ASSET_VERSIONS[name]


def asset(prefix: str, name: str) -> str:
    url = f"{prefix}assets/{name}"
    # Cache-bust CSS/JS by content hash so returning visitors pick up changes
    # despite the long Expires headers set in .htaccess.
    if name.endswith((".css", ".js")):
        version = _asset_version(name)
        if version:
            url = f"{url}?v={version}"
    return url


def head(
    prefix: str,
    title: str,
    description: str,
    canonical: str,
    crumbs: list[tuple[str, str]],
    extra_schema: list[dict] | None = None,
    og_type: str = "website",
    image: str = "/assets/img/og-default.webp",
    robots: str = "index,follow,max-image-preview:large",
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
  <link rel="icon" href="{prefix}favicon.ico" sizes="any">
  <link rel="icon" type="image/png" href="{prefix}favicon.png">
  <link rel="apple-touch-icon" href="{asset(prefix, 'img/apple-touch-icon.png')}">
  <link rel="manifest" href="{prefix}site.webmanifest">
  <meta name="robots" content="{esc(robots)}">
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
    <a class="logo" href="/" aria-label="Cyber Developers home">
      <span class="logo-lockup">
        <img class="logo-img" src="{asset(prefix, 'img/logo-light.png')}" width="313" height="120" alt="Cyber Developers">
        <small>Custom software · South Africa</small>
      </span>
    </a>
    <nav class="nav-links" aria-label="Primary">
      {''.join(items)}
    </nav>
    <a class="btn btn-primary nav-cta" href="/contact/" data-track="consultation_requested" data-track-location="header">Book a Consultation</a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-label="Open menu"><span></span></button>
  </div>
</header>
"""


def footer(prefix: str) -> str:
    year = date.today().year
    return f"""<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      <a class="logo" href="/" aria-label="Cyber Developers home"><img class="logo-img" src="{asset(prefix, 'img/logo-light.png')}" width="313" height="120" alt="Cyber Developers"></a>
      <p style="margin-top:1rem">{esc(ORG_DESC)}</p>
      <p style="margin-top:1rem">Software built around your business.</p>
      {social_links(prefix)}
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
        <li><a href="/services/business-systems/">Business Systems</a></li>
        <li><a href="/services/web-application-development/">Web Applications</a></li>
        <li><a href="/services/mobile-app-development/">Mobile Apps</a></li>
        <li><a href="/services/workflow-automation/">Workflow Automation</a></li>
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


def related_links(items: list[tuple[str, str]]) -> str:
    return "<ul>" + "".join(f'<li><a href="{u}">{esc(n)}</a></li>' for n, u in items) + "</ul>"


def steps_ol(items: list[tuple[str, str]], cls: str = "lifecycle") -> str:
    lis = "".join(f"<li><h3>{esc(t)}</h3><p>{esc(d)}</p></li>" for t, d in items)
    return f'<ol class="{cls}">{lis}</ol>'


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
    robots: str = "index,follow,max-image-preview:large",
) -> str:
    prefix = "" if rel_path == "index.html" else "../" * len(Path(rel_path).parent.parts)
    nav_current = current if current is not None else canonical
    return (
        head(prefix, title, description, canonical, crumbs, extra_schema, og_type, image, robots)
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
  <meta name="robots" content="noindex,follow">
  <link rel="canonical" href="{SITE}{target}">
  <meta http-equiv="refresh" content="0; url={target}">
  <script>location.replace({json.dumps(target)});</script>
</head>
<body>
  <p>This page has moved to <a href="{target}">{SITE}{target}</a>.</p>
</body>
</html>
"""
