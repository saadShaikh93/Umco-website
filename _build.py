#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generates the UMCO v2 static site. Run: python3 _build.py"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

ICON = {
  "audit": '<svg width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"/></svg>',
  "tax": '<svg width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 14l6-6m-5.5.5h.01m4.99 5h.01M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16l3.5-2 3.5 2 3.5-2 3.5 2z"/></svg>',
  "advisory": '<svg width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/></svg>',
  "mgmt": '<svg width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>',
  "bpo": '<svg width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4"/></svg>',
  "digital": '<svg width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>',
  "risk": '<svg width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>',
  "corp": '<svg width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.6" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5m0 0v-3a1 1 0 011-1h2a1 1 0 011 1v3m-4 0h4m-8-9h.01M9 9h.01M9 6h.01M13 12h.01M13 9h.01M13 6h.01M17 12h.01M17 9h.01M17 6h.01"/></svg>',
  "check": '<svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>',
  "arrow": '<svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>',
  "shield": '<svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>',
  "calendar": '<svg width="30" height="30" fill="none" stroke="currentColor" stroke-width="1.6" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>',
}

SERVICES = [
  dict(slug="audit-assurance", icon="audit", name="Audit & Assurance",
       short="Independent statutory and special-purpose audits that give boards, lenders, and regulators complete confidence in your numbers.",
       h1='Assurance your stakeholders can <span class="serif-accent">build on.</span>',
       lede="Statutory audits, reviews, and agreed-upon procedures executed under International Standards on Auditing — rigorous, independent, and on schedule.",
       overview=["Financial statements are only as valuable as the confidence behind them. UMCO's audit practice combines ISA-compliant methodology with deep knowledge of Pakistan's regulatory environment — SECP, FBR, and State Bank requirements — to deliver opinions that stand up to scrutiny from boards, banks, and international investors.",
                 "We plan early, communicate continuously, and surface issues while there is still time to act on them. No surprises at sign-off."],
       offers=[("Statutory & External Audit","ISA-compliant audits of annual financial statements for companies of every scale."),
               ("Internal Audit & Controls Review","Independent assessment of control design and operating effectiveness, with pragmatic remediation plans."),
               ("Special-Purpose & Donor Audits","Grant, project, and donor-compliance audits for NGOs and internationally funded programmes."),
               ("Agreed-Upon Procedures","Targeted factual-findings engagements for acquisitions, disputes, and lender requirements.")],
       related=["tax-advisory","risk-advisory","corporate-advisory"]),
  dict(slug="tax-advisory", icon="tax", name="Tax Advisory",
       short="Proactive direct and indirect tax strategy — FBR compliance, provincial sales tax, and cross-border structuring.",
       h1='Tax advice that keeps you compliant, efficient, and <span class="serif-accent">prepared.</span>',
       lede="Corporate tax planning, sales tax compliance, and dispute representation across FBR, SRB, PRA, and KPRA — handled end to end.",
       overview=["Pakistan's tax landscape changes with every Finance Act, and the cost of getting it wrong compounds quickly. Our tax team plans across the full year — not just at filing time — to legally minimise tax exposure while keeping you fully compliant with federal and provincial tax authorities.",
                 "From withholding tax regimes, income tax, sales tax, double-tax treaties, and provincial sales tax on services, we cover the complete spectrum of direct and indirect taxation for domestic groups and foreign investors entering Pakistan.",
                 "Our services include tax advisory, registration, compliance, return filing, audit support, and representation before the Federal Board of Revenue (FBR) and provincial revenue authorities, including SRB, PRA, KPRA, and BRA."],
       offers=[("Corporate Tax Planning & Compliance","Return preparation, withholding compliance, and year-round structuring advice."),
               ("Federal and Provincial Sales Tax","Registration, monthly filings, input tax credit optimisation, refund claims, audit assistance, and compliance support before FBR and provincial revenue authorities including SRB, PRA, KPRA, and BRA."),
               ("Tax Disputes & Representation","Audit defence, appeals, and ADR representation before commissioners and tribunals."),
               ("International & Treaty Tax","Transfer pricing documentation, permanent-establishment analysis, and repatriation planning.")],
       related=["audit-assurance","corporate-advisory","financial-advisory"]),
  dict(slug="financial-advisory", icon="advisory", name="Financial Advisory",
       short="Transaction support, valuations, capital raising, and wealth structuring for decisions that can't be unmade.",
       h1='Expert guidance for <span class="serif-accent">high-stakes decisions.</span>',
       lede="M&A, due diligence, valuations, and financing advisory — delivered with the discretion and rigour consequential decisions demand.",
       overview=["Whether you are acquiring a competitor, raising capital, or planning succession, the quality of advice at the table determines the outcome. UMCO's advisory team has supported transactions across manufacturing, real estate, technology, and financial services.",
                 "We act solely in your interest — no hidden mandates, no referral arrangements — and we stay engaged from first scoping through to close."],
       offers=[("Mergers & Acquisitions","Buy-side and sell-side advisory: valuation, negotiation support, and deal structuring."),
               ("Financial Due Diligence","Quality-of-earnings, working-capital, and net-debt analysis that protects your position."),
               ("Business Valuations","Independent valuations for transactions, disputes, financial reporting, and tax."),
               ("Capital Raising & Debt Advisory","Investor-ready models, information memoranda, and lender negotiation support.")],
       related=["corporate-advisory","tax-advisory","management-consulting"]),
  dict(slug="management-consulting", icon="mgmt", name="Management Consulting",
       short="Strategy, performance improvement, and restructuring grounded in financial evidence — not frameworks.",
       h1='Strategy backed by numbers, <span class="serif-accent">not guesswork.</span>',
       lede="We diagnose where value leaks from your business and stay embedded through execution until the results are on the P&L.",
       overview=["Most consulting reports end up in a drawer. Ours end up implemented — because we build recommendations with your team, from your actual financial and operational data, and we stay through the rollout.",
                 "Engagements typically focus on margin improvement, working-capital release, organisational redesign, and turnaround situations where speed matters."],
       offers=[("Business Planning & Forecasting","Budgets, KPI frameworks, and scenario models that leadership actually uses."),
               ("Performance Improvement","Cost-structure analysis, pricing review, and operational re-engineering with tracked ROI."),
               ("Corporate Restructuring","Financial restructuring, post-merger integration, and turnaround management."),
               ("Family Business & Succession","Governance structures and transition planning for founder-led groups.")],
       related=["financial-advisory","digital-transformation","bpo_rel"]),
  dict(slug="business-process-outsourcing", icon="bpo", name="Business Process Outsourcing",
       short="Your finance back office, managed by qualified professionals with partner-level oversight.",
       h1='Your back office, run to <span class="serif-accent">audit standard.</span>',
       lede="Accounting, payroll, and management reporting delivered as a managed service — accurate, on time, every month.",
       overview=["Hiring, training, and retaining a finance team is expensive — and a single departure can stall your month-end close. UMCO's outsourcing practice gives you a complete finance function staffed by qualified professionals, at a fraction of the in-house cost.",
                 "Every client receives a dedicated engagement manager, documented processes, and reporting calibrated to what your leadership team needs to see."],
       offers=[("Bookkeeping & Accounting","Full-cycle transaction processing, reconciliations, and month-end close on cloud platforms."),
               ("Payroll Management","End-to-end payroll with statutory deductions, EOBI/social security, and confidential disbursement."),
               ("Management Reporting","Monthly packs with P&L, cash flow, and KPI commentary your board can act on."),
               ("CFO-as-a-Service","Senior finance leadership on a fractional basis for growing companies.")],
       related=["digital-transformation","tax-advisory","audit-assurance"]),
  dict(slug="digital-transformation", icon="digital", name="Digital Transformation",
       short="ERP selection, cloud accounting migration, and analytics — led by accountants who understand the controls.",
       h1='Modern finance infrastructure, <span class="serif-accent">implemented right.</span>',
       lede="From spreadsheet chaos to real-time dashboards — we select, implement, and embed the systems your finance function runs on.",
       overview=["Technology projects fail when implementers don't understand accounting. Ours don't — every UMCO digital engagement is led by finance professionals who know the controls, the compliance requirements, and the reporting outcomes the system must produce.",
                 "We are vendor-neutral: we recommend the right platform for your scale and sector, not the one that pays a referral fee."],
       offers=[("ERP Selection & Implementation","Needs assessment, vendor selection, and full implementation management."),
               ("Cloud Accounting Migration","QuickBooks Online, Xero, and SAP migrations with zero data loss."),
               ("Dashboards & Analytics","Power BI reporting pipelines and cash-flow forecasting models."),
               ("Process Automation","Workflow automation for AP, AR, and approvals that removes manual error.")],
       related=["bpo_rel","management-consulting","risk-advisory"]),
  dict(slug="risk-advisory", icon="risk", name="Risk Advisory",
       short="Enterprise risk, internal controls, and regulatory compliance frameworks that protect value before it's lost.",
       h1='See risk clearly. <span class="serif-accent">Act before it costs you.</span>',
       lede="Enterprise risk frameworks, internal-control design, and compliance programmes built for Pakistan's regulatory reality.",
       overview=["Effective risk management protects business value before issues turn into losses. UMCO helps management, boards, and audit committees understand financial, operational, regulatory, and compliance risks, and implement practical controls that support governance without slowing business operations.",
                 "We design risk management frameworks, internal controls, SOPs, and reporting mechanisms aligned with COSO and ISO 31000, ensuring they are tested, owned, monitored, and embedded into daily operations."],
       offers=[("Enterprise Risk Management","Risk registers, appetite statements, and board-level reporting frameworks."),
               ("Internal Controls & SOPs","Design and review of policies, procedures, approval matrices, and control activities."),
               ("Regulatory Compliance","AML/CFT programmes, SECP code-of-governance compliance, and remediation."),
               ("Fraud Risk & Forensics","Fraud-risk assessments, investigations, and dispute support.")],
       related=["audit-assurance","corporate-advisory","management-consulting"]),
  dict(slug="corporate-advisory", icon="corp", name="Corporate Advisory",
       short="Company formation, SECP compliance, and corporate secretarial services — especially for foreign entrants to Pakistan.",
       h1='Enter and operate in Pakistan <span class="serif-accent">with confidence.</span>',
       lede="Entity structuring, SECP and State Bank compliance, and ongoing corporate secretarial support for local and foreign investors.",
       overview=["UMCO provides corporate advisory support to foreign investors and domestic groups for business setup, company registration, restructuring, share transactions, regulatory filings, and ongoing corporate compliance in Pakistan.",
                 "Our team assists with SECP, FBR, SBP, BOI, and other regulatory matters, ensuring that corporate records and filings remain accurate, compliant, and ready for audit, financing, or due diligence."],
       offers=[("Market Entry & Company Formation","Entity selection, SECP incorporation, branch/liaison office registration with BOI."),
               ("SECP Compliance & Filings","Annual returns, statutory forms, changes in directors, shareholding, and registered office."),
               ("Foreign Exchange & Repatriation","State Bank approvals, dividend repatriation, and FE manual compliance."),
               ("Group Restructuring","Mergers, schemes of arrangement, and share-capital transactions.")],
       related=["tax-advisory","financial-advisory","audit-assurance"]),
]
# resolve a forward-reference alias
for s in SERVICES:
    s["related"] = ["business-process-outsourcing" if r == "bpo_rel" else r for r in s["related"]]
SVC = {s["slug"]: s for s in SERVICES}

INDUSTRIES = [
  ("Manufacturing", "Cost accounting, export-rebate optimisation, and audit for textile, pharma, and engineering producers.", "audit"),
  ("Retail & Consumer", "Multi-location controls, POS-integrated accounting, and indirect-tax compliance at scale.", "bpo"),
  ("Technology & Startups", "Financial reporting, tax advisory, regulatory compliance, and investor due diligence support for startups and technology companies.", "digital"),
  ("Healthcare", "Regulatory compliance, donor-funded programme audits, and cost-per-outcome reporting.", "risk"),
  ("Education", "Trust and not-for-profit structures, fee-revenue assurance, and governance frameworks.", "corp"),
  ("Financial Services", "Prudential reporting, AML/CFT programmes, and SBP/SECP regulatory liaison.", "advisory"),
  ("Real Estate & Construction", "Project accounting, percentage-of-completion reporting, and capital-gains structuring.", "mgmt"),
  ("International Investors", "Market-entry structuring, repatriation planning, and a single local point of accountability.", "tax"),
]

CASES = [
  ("Tax Advisory", "Textile exporter recovers blocked sales-tax refunds",
   "A Karachi-based textile exporter had over a year of sales-tax refunds stuck in processing, straining working capital during peak season.",
   "UMCO reconstructed the refund claims with complete annexure documentation, resolved discrepancy notices, and represented the client through FBR's verification process.",
   "Refunds released in full; a documented claims process now keeps the refund cycle under 90 days."),
  ("Digital Transformation", "Distribution group replaces spreadsheets with a live ERP",
   "A 200-employee distribution business was closing its books 25 days after month-end, with inventory positions nobody trusted.",
   "We led ERP selection and implementation, migrated three years of data, redesigned the chart of accounts, and trained the finance team.",
   "Month-end close reduced to 5 working days; leadership now reviews live margin dashboards weekly."),
  ("Audit & Assurance", "Foreign subsidiary passes group audit with zero adjustments",
   "The Pakistan subsidiary of a European group faced repeated audit adjustments that delayed group consolidation every year.",
   "UMCO performed a controls remediation programme ahead of the audit, aligning local books to group IFRS policies and documenting key reconciliations.",
   "Clean audit opinion with zero post-close adjustments; group reporting deadline met for the first time in four years."),
  ("Financial Advisory", "Family-owned manufacturer completes its first acquisition",
   "A second-generation manufacturer wanted to acquire a competitor but had never run a transaction and faced an aggressive seller timeline.",
   "We delivered financial due diligence, a defensible valuation range, and deal-structure advice — then supported negotiation through closing.",
   "Acquisition closed below the initial asking price, with warranties covering every red-flag item identified in diligence."),
  ("Business Process Outsourcing", "Startup scales from 8 to 80 staff without hiring a finance team",
   "A funded technology startup was burning founder time on bookkeeping, payroll, and investor reporting.",
   "UMCO took over the full finance back office — cloud accounting, monthly payroll, and a board-ready reporting pack — under a managed-service agreement.",
   "Founders reclaimed roughly 20 hours a month; investor reporting has been delivered on schedule for 30 consecutive months."),
  ("Corporate Advisory", "International company enters Pakistan in under 8 weeks",
   "A Gulf-based services company needed a compliant Pakistan presence — entity, bank account, tax registrations — on a contract deadline.",
   "We handled SECP incorporation, FBR and provincial registrations, State Bank requirements, and banking introductions in a single coordinated workstream.",
   "Fully operational entity in 7 weeks; UMCO continues as the company's outsourced compliance function."),
]

INSIGHTS = [
  ("Tax", "2026-01-15", "What the latest Finance Act means for your effective tax rate",
   "Key corporate-tax changes, revised withholding regimes, and the planning windows that close at year-end — summarised for CFOs."),
  ("Compliance", "2025-12-02", "FBR e-invoicing: who must integrate, and by when",
   "Digital invoicing integration is being phased in by taxpayer category. A practical readiness checklist for finance teams."),
  ("Advisory", "2025-11-10", "Valuing a private business in Pakistan: what buyers actually pay for",
   "Multiples tell only part of the story. How quality of earnings, customer concentration, and documentation move real transaction prices."),
  ("Audit", "2025-10-21", "IFRS 18 is coming: how presentation of financial statements will change",
   "The new income-statement categories and management-defined performance measures, and what to prepare before adoption."),
  ("International", "2025-09-30", "A foreign investor's guide to repatriating profits from Pakistan",
   "Dividend remittance, State Bank approvals, and the documentation that prevents months of delay."),
  ("Digital", "2025-09-08", "Five signs your business has outgrown its accounting software",
   "From manual consolidations to inventory blind spots — when to move up, and how to choose without overbuying."),
]

# Calendly scheduling link.
# Leave CALENDLY_URL empty until the client provides their real Calendly link.
# When empty, the site shows a branded "request a time" panel instead of a live embed,
# and the Book Consultation buttons link to the contact page (no broken popup).
# Once you paste the real link below, the inline scheduler + popup activate automatically.
CALENDLY_URL = ""
CALENDLY_READY = CALENDLY_URL.startswith("https://calendly.com/")
CAL_ATTR = " data-calendly" if CALENDLY_READY else ""

NAV_LINKS = [("services.html","Services"),("industries.html","Industries"),("about.html","About"),
             ("case-studies.html","Case Studies"),("insights.html","Insights")]

def head(title, desc, prefix=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>UM</title>
  <meta name="description" content="{desc}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:type" content="website" />
  <meta name="referrer" content="no-referrer" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;550;600;650;700&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{prefix}assets/main.css" />
  <link rel="stylesheet" href="https://assets.calendly.com/assets/external/widget.css" />
  <script src="https://assets.calendly.com/assets/external/widget.js" async></script>
</head>
<body>"""

def navbar(prefix="", active=""):
    ACTIVE_ATTR = ' class="active"'
    links = "".join(
        f'<li><a href="{prefix}{href}"{ACTIVE_ATTR if href == active else ""}>{label}</a></li>'
        for href, label in NAV_LINKS)
    mlinks = "".join(f'<a href="{prefix}{href}">{label}</a>' for href, label in NAV_LINKS)
    return f"""
<header class="nav">
  <div class="wrap nav-row">
    <a href="{prefix}index.html" class="brand" aria-label="UMCO home"><img src="{prefix}logo.png" alt="UMCO — Umair Manzoor &amp; Co Chartered Accountants" /></a>
    <nav aria-label="Primary"><ul class="nav-menu">{links}</ul></nav>
    <div class="nav-actions">
      <a href="{prefix}contact.html" class="btn btn-navy"{CAL_ATTR}>Book Consultation</a>
      <button class="nav-burger" aria-label="Toggle menu" aria-expanded="false"><span></span></button>
    </div>
  </div>
</header>
<div class="mobile-menu">{mlinks}<a href="{prefix}careers.html">Careers</a></div>"""

def footer(prefix=""):
    svc_links = "".join(f'<li><a href="{prefix}services/{s["slug"]}.html">{s["name"]}</a></li>' for s in SERVICES[:6])
    return f"""
<footer class="footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a href="{prefix}index.html" class="brand"><img src="{prefix}logo.png" alt="UMCO" /></a>
        <p class="footer-about">Umair Manzoor &amp; Co Chartered Accountants — providing audit, tax, advisory, outsourcing, and digital consulting services to businesses operating in Pakistan and abroad.</p>
      </div>
      <div>
        <h4>Services</h4>
        <ul>{svc_links}</ul>
      </div>
      <div>
        <h4>Firm</h4>
        <ul>
          <li><a href="{prefix}about.html">About Us</a></li>
          <li><a href="{prefix}team.html">Leadership</a></li>
          <li><a href="{prefix}industries.html">Industries</a></li>
          <li><a href="{prefix}case-studies.html">Case Studies</a></li>
          <li><a href="{prefix}insights.html">Insights</a></li>
          <li><a href="{prefix}careers.html">Careers</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="mailto:info@umairmanzoor.com">info@umairmanzoor.com</a></li>
          <li><a href="tel:+922137120735">(92) 21 3712 0735</a></li>
          <li><a href="https://wa.me/923106569999" rel="noopener" target="_blank">WhatsApp</a></li>
          <li><a href="{prefix}contact.html">Shayan Iconic Tower, Karachi</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-meta">
      <p>© 2026 Umair Manzoor &amp; Co Chartered Accountants. All rights reserved.</p>
      <div class="links"><a href="#">Privacy Policy</a><a href="#">Terms of Service</a></div>
      <p>Powered by <a href="https://hexura.tech" target="_blank" rel="noopener">hexura.tech</a></p>
    </div>
  </div>
</footer>
<script src="{prefix}assets/main.js"></script>
</body>
</html>"""

def page(path, title, desc, body, active=""):
    prefix = "../" if "/" in path else ""
    html = head(title, desc, prefix) + navbar(prefix, active) + body + footer(prefix)
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(html)
    print("wrote", path)

def cta_band(prefix=""):
    return f"""
<section class="cta-band section">
  <div class="wrap cta-inner reveal">
    <div class="kicker" style="justify-content:center">Start the conversation</div>
    <h2>Clarity is one conversation <span class="serif-accent">away.</span></h2>
    <p>Speak with a senior UMCO advisor about your audit, tax, or transformation agenda. No obligation — just a clear view of where you stand.</p>
    <div class="hero-ctas">
      <a href="{prefix}contact.html" class="btn btn-gold"{CAL_ATTR}>Book Consultation {ICON["arrow"]}</a>
      <a href="https://wa.me/923106569999" target="_blank" rel="noopener" class="btn btn-ghost-light">WhatsApp Us</a>
    </div>
  </div>
</section>"""

def svc_cards(prefix="", limit=8):
    cards = []
    for i, s in enumerate(SERVICES[:limit], 1):
        cards.append(f"""
      <a class="svc-card" href="{prefix}services/{s["slug"]}.html">
        <div class="svc-num">0{i}</div>
        <div class="svc-icon">{ICON[s["icon"]]}</div>
        <h3>{s["name"]}</h3>
        <p>{s["short"]}</p>
        <span class="text-link">Explore service {ICON["arrow"]}</span>
      </a>""")
    return "".join(cards)

# ── image assets (Unsplash, royalty-free) ──
IMG = {
  "hero_growth":  "https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=1920&q=80&fit=crop",
  "hero_digital": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1920&q=80&fit=crop",
  "hero_audit":   "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=1920&q=80&fit=crop",
  "hero_risk":    "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1920&q=80&fit=crop",
  "svc": {
    "audit-assurance":            "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=700&q=78&fit=crop",
    "tax-advisory":               "https://images.unsplash.com/photo-1554224154-26032ffc0d07?w=700&q=78&fit=crop",
    "risk-advisory":              "https://images.unsplash.com/photo-1563986768609-322da13575f3?w=700&q=78&fit=crop",
    "financial-advisory":         "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=700&q=78&fit=crop",
    "digital-transformation":     "https://images.unsplash.com/photo-1518770660439-4636190af475?w=700&q=78&fit=crop",
    "business-process-outsourcing":"https://images.unsplash.com/photo-1497366216548-37526070297c?w=700&q=78&fit=crop",
    "corporate-advisory":         "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=700&q=78&fit=crop",
    "management-consulting":      "https://images.unsplash.com/photo-1497366811353-6870744d04b2?w=700&q=78&fit=crop",
  },
  "ind": {
    "Manufacturing":        "https://images.unsplash.com/photo-1565043666747-69f6646db940?w=600&q=78&fit=crop",
    "Technology & Startups":"https://images.unsplash.com/photo-1531297484001-80022131f5a1?w=600&q=78&fit=crop",
    "Healthcare":           "https://images.unsplash.com/photo-1538108149393-fbbd81895907?w=600&q=78&fit=crop",
    "Retail & Consumer":    "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600&q=78&fit=crop",
    "Education":            "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=600&q=78&fit=crop",
    "Financial Services":   "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=600&q=78&fit=crop",
    "Real Estate & Construction": "https://images.unsplash.com/photo-1486325212027-8081e485255e?w=600&q=78&fit=crop",
    "International Investors":    "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?w=600&q=78&fit=crop",
  },
  "mag_feature": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=1200&q=80&fit=crop",
}

HERO_SLIDES = [
  ("Business Growth", IMG["hero_growth"],
   'Helping businesses scale with <span class="serif-accent">confidence.</span>',
   "Audit, Tax, Advisory, and Digital Transformation services trusted by ambitious organisations across Pakistan and international markets."),
  ("Digital Transformation", IMG["hero_digital"],
   'Transforming finance through <span class="serif-accent">technology.</span>',
   "Helping organisations modernise operations through data, automation, and digital innovation — led by accountants who understand the controls."),
  ("Audit & Compliance", IMG["hero_audit"],
   'Strengthening trust through <span class="serif-accent">assurance.</span>',
   "Independent audit and compliance solutions that support confident decision-making for boards, lenders, and regulators."),
  ("Risk & Advisory", IMG["hero_risk"],
   'Managing risk in a rapidly changing <span class="serif-accent">world.</span>',
   "Risk advisory and governance solutions for resilient organisations — see exposure clearly, act before it costs you."),
]

# ───────────────────────────── HOMEPAGE ─────────────────────────────
CASE_METRICS = [
  [("100%","refunds released"),("&lt;90","day cycle")],
  [("5","day close"),("-80%","reporting lag")],
  [("0","adjustments"),("1st","on-time consolidation")],
  [("&lt;ask","final price"),("100%","red flags covered")],
  [("20h","saved monthly"),("30","on-time reports")],
  [("7","weeks to operational"),("1","point of contact")],
]

CASE_IMG = [
  "https://images.unsplash.com/photo-1554224154-26032ffc0d07?w=700&q=78&fit=crop",
  "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=700&q=78&fit=crop",
  "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=700&q=78&fit=crop",
  "https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=700&q=78&fit=crop",
  "https://images.unsplash.com/photo-1497366216548-37526070297c?w=700&q=78&fit=crop",
  "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=700&q=78&fit=crop",
]

def case_card(idx, c, with_img=False):
    tag, title, ch, sol, out = c
    chips = "".join(f"<span><b>{v}</b> {l}</span>" for v, l in CASE_METRICS[idx])
    img = f'<div class="case-img"><img src="{CASE_IMG[idx]}" alt="{tag} case study — UMCO" loading="lazy" /></div>' if with_img else ""
    return f"""
      <article class="case-card">
        {img}
        <span class="case-tag">{tag}</span>
        <div class="case-body">
          <h3>{title}</h3>
          <div class="case-metrics">{chips}</div>
          <div class="case-row"><b>Challenge</b><p>{ch}</p></div>
          <div class="case-row"><b>Solution</b><p>{sol}</p></div>
          <div class="case-outcome"><div class="case-row"><b>Outcome</b><p>{out}</p></div></div>
        </div>
      </article>"""

hero_slides_html = ""
for i, (tag, img, h1, sub) in enumerate(HERO_SLIDES):
    hero_slides_html += f"""
  <div class="hs-slide{' active' if i == 0 else ''}" role="group" aria-label="Slide {i+1} of {len(HERO_SLIDES)}">
    <div class="hs-bg" style="background-image:url('{img}')"></div>
    <div class="hs-veil"></div>
    <div class="hs-content">
      <div class="wrap">
        <div class="hs-copy">
          <span class="hs-slide-tag"><i></i>{tag}</span>
          <h1>{h1}</h1>
          <p>{sub}</p>
          <div class="hero-ctas">
            <a href="services.html" class="btn btn-ghost-light">Explore Services {ICON["arrow"]}</a>
          </div>
        </div>
      </div>
    </div>
  </div>"""

particles = "".join(f'<b style="left:{(i*37)%97+2}%;animation-delay:-{i*1.7}s"></b>' for i in range(14))
hs_dots = "".join(f'<button class="hs-dot{" active" if i==0 else ""}" aria-label="Go to slide {i+1}"><i></i></button>' for i in range(len(HERO_SLIDES)))

svcx_cards = ""
for s in SERVICES:
    bullets = "".join(f"<li>{t}</li>" for t, _ in s["offers"][:3])
    svcx_cards += f"""
      <a class="svcx" href="services/{s["slug"]}.html">
        <div class="svcx-media">
          <img src="{IMG["svc"][s["slug"]]}" alt="{s["name"]} — UMCO" loading="lazy" />
          <div class="svcx-icon">{ICON[s["icon"]]}</div>
        </div>
        <div class="svcx-body">
          <h3>{s["name"]}</h3>
          <p>{s["short"]}</p>
          <ul class="svcx-more">{bullets}</ul>
          <span class="text-link">Explore service {ICON["arrow"]}</span>
        </div>
      </a>"""

indx_cards = "".join(f"""
      <a class="indx" href="industries.html">
        <img src="{IMG["ind"][name]}" alt="{name} industry — UMCO" loading="lazy" />
        <div class="indx-body">
          <div class="indx-icon">{ICON[ic]}</div>
          <h3>{name}</h3>
          <p>{d}</p>
        </div>
      </a>""" for name, d, ic in INDUSTRIES)

FEATURES = [
  ("mgmt","Industry Expertise","Fifteen years across manufacturing, retail, technology, and financial services — we've seen your problem before.","photo-1565043666747-69f6646db940"),
  ("audit","Certified Professionals","ICAP and ACCA-qualified teams working to International Standards on Auditing and IFRS.","photo-1481627834876-b7833e8f5570"),
  ("digital","Digital-First Approach","Cloud platforms, automation, and live dashboards are our default — not an upsell.","photo-1518770660439-4636190af475"),
  ("risk","Regulatory Excellence","FBR, SECP, and State Bank requirements handled proactively, before they become findings.","photo-1486406146926-c627a92ad1ab"),
  ("bpo","Client-Centric Engagement","A partner leads every engagement and answers within one business day. No handoffs to juniors.","photo-1497366216548-37526070297c"),
  ("advisory","Strategic Advisory","Advice connected to your growth agenda — not just compliance paperwork filed on time.","photo-1460925895917-afdab827c52f"),
]
feat_cards = "".join(f"""
      <div class="feat-card has-img">
        <div class="feat-img"><img src="https://images.unsplash.com/{img}?w=600&q=78&fit=crop" alt="{t} — UMCO" loading="lazy" /></div>
        <div class="feat-body">
          <div class="feat-icon">{ICON[ic]}</div>
          <h3>{t}</h3>
          <p>{d}</p>
        </div>
      </div>""" for ic, t, d, img in FEATURES)

home_cases = "".join(case_card(i, c) for i, c in enumerate(CASES))

_fc, _fd, _ft, _fdesc = INSIGHTS[0]
mag_side = "".join(f"""
      <a class="insight-card" href="insights.html">
        <div class="insight-meta"><span>{cat}</span><time datetime="{date}">{date}</time></div>
        <h3>{t}</h3>
        <span class="read-time">⏱ {4+i} min read</span>
      </a>""" for i, (cat, date, t, d) in enumerate(INSIGHTS[1:4]))

HOME = f"""
<section class="hs" aria-roledescription="carousel" aria-label="UMCO highlights">
  {hero_slides_html}
  <div class="hs-particles" aria-hidden="true">{particles}</div>
  <div class="hs-scrollhint" aria-hidden="true">Scroll</div>
  <div class="hs-footer">
    <div class="wrap hs-footer-row">
      <div class="hs-metrics count-group">
        <div class="metric"><b data-count="15+">15+</b><span>Years of experience</span></div>
        <div class="metric"><b data-count="500+">500+</b><span>Clients advised</span></div>
        <div class="metric"><b data-count="12+">12+</b><span>Industries served</span></div>
        <div class="metric"><b data-count="1200+">1200+</b><span>Projects completed</span></div>
      </div>
      <div class="hs-nav">
        <div class="hs-dots">{hs_dots}</div>
        <div class="hs-arrows">
          <button class="hs-arrow" data-hs="-1" aria-label="Previous slide"><svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7"/></svg></button>
          <button class="hs-arrow" data-hs="1" aria-label="Next slide"><svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"/></svg></button>
        </div>
      </div>
    </div>
  </div>
</section>

<div class="trust-strip">
  <div class="wrap trust-row">
    <span class="trust-label">Credentials &amp; Standards</span>
    <div class="trust-items">
      <span class="trust-item">{ICON["shield"]} ICAP Registered Firm</span>
      <span class="trust-item">{ICON["shield"]} ACCA-Qualified Team</span>
      <span class="trust-item">{ICON["shield"]} SECP Registered Intermediary</span>
      <span class="trust-item">{ICON["shield"]} ICAP Approved Trainee Organization</span>
    </div>
  </div>
</div>

<section class="section" id="services">
  <div class="wrap">
    <div class="section-head reveal">
      <div class="kicker">What we do</div>
      <h2>One firm. Every discipline your finance agenda <span class="serif-accent">requires.</span></h2>
      <p>Eight integrated practice areas — hover any card to see what's inside.</p>
    </div>
    <div class="carousel reveal" data-carousel>
      <div class="car-track">{svcx_cards}</div>
      <div class="car-controls">
        <div class="car-progress"><i></i></div>
        <div class="car-arrows">
          <button class="car-arrow" data-dir="-1" aria-label="Scroll services left"><svg width="17" height="17" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7"/></svg></button>
          <button class="car-arrow" data-dir="1" aria-label="Scroll services right"><svg width="17" height="17" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"/></svg></button>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="industries section">
  <div class="wrap">
    <div class="section-head reveal">
      <div class="kicker">Industries</div>
      <h2 style="color:#fff">Sector knowledge that shows up in the <span class="serif-accent">detail.</span></h2>
      <p style="color:rgba(255,255,255,0.6)">We serve clients across Pakistan's core sectors — and the international investors entering them.</p>
    </div>
    <div class="carousel reveal" data-carousel>
      <div class="car-track">{indx_cards}</div>
      <div class="car-controls">
        <div class="car-progress"><i></i></div>
        <div class="car-arrows">
          <button class="car-arrow" data-dir="-1" aria-label="Scroll industries left"><svg width="17" height="17" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7"/></svg></button>
          <button class="car-arrow" data-dir="1" aria-label="Scroll industries right"><svg width="17" height="17" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"/></svg></button>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <div class="kicker">Why choose UMCO</div>
      <h2>Big-firm rigour. <span class="serif-accent">Partner-level attention.</span></h2>
      <p>Six reasons ambitious organisations choose us over larger names — and stay.</p>
    </div>
    <div class="feat-grid reveal-stagger">{feat_cards}</div>
  </div>
</section>

<section class="section" style="background:var(--paper)">
  <div class="wrap">
    <div class="section-head reveal">
      <div class="kicker">Proven outcomes</div>
      <h2>Recent client <span class="serif-accent">results.</span></h2>
      <p>Representative engagements, anonymised to protect client confidentiality.</p>
    </div>
    <div class="carousel case-car reveal" data-carousel>
      <div class="car-track">{home_cases}</div>
      <div class="car-controls">
        <div class="car-progress"><i></i></div>
        <div class="car-arrows">
          <button class="car-arrow" data-dir="-1" aria-label="Scroll case studies left"><svg width="17" height="17" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7"/></svg></button>
          <button class="car-arrow" data-dir="1" aria-label="Scroll case studies right"><svg width="17" height="17" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"/></svg></button>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <div class="kicker">Insights</div>
      <h2>Thinking that keeps you <span class="serif-accent">ahead.</span></h2>
      <p>Practical analysis of the tax, reporting, and regulatory changes that affect your business.</p>
    </div>
    <div class="mag-grid reveal-stagger">
      <a class="mag-feature" href="insights.html">
        <img src="{IMG["mag_feature"]}" alt="Finance analysis — featured UMCO insight" loading="lazy" />
        <div class="mag-feature-body">
          <div class="insight-meta"><span>{_fc} · Featured</span><time datetime="{_fd}">{_fd}</time></div>
          <h3>{_ft}</h3>
          <p>{_fdesc}</p>
          <span class="read-time">⏱ 6 min read</span><br/>
          <span class="text-link">Read insight {ICON["arrow"]}</span>
        </div>
      </a>
      <div class="mag-side">{mag_side}</div>
    </div>
  </div>
</section>
{cta_band()}"""

page("index.html",
     "UMCO — Chartered Accountants | Audit, Tax & Advisory in Pakistan",
     "Umair Manzoor & Co Chartered Accountants: audit, tax advisory, financial advisory, and digital consulting for businesses across Pakistan and international markets.",
     HOME)

# ───────────────────────────── SERVICES OVERVIEW ─────────────────────────────
page("services.html",
     "Services — UMCO Chartered Accountants",
     "Eight integrated practice areas: audit & assurance, tax advisory, financial advisory, management consulting, BPO, digital transformation, risk advisory, and corporate advisory.",
     f"""
<section class="page-hero">
  <div class="ph-bg" style="background-image:url('{IMG["hero_audit"]}')"></div>
  <div class="ph-veil"></div>
  <div class="wrap">
    <div class="crumb"><a href="index.html">Home</a><span>/</span><span>Services</span></div>
    <h1>Every discipline your finance agenda requires — <span class="serif-accent">integrated.</span></h1>
    <p class="lede">Strategy, compliance, and execution rarely fail in isolation. Our eight practices work as one team, so nothing falls between them.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="svcx-grid reveal-stagger">{svcx_cards}</div>
  </div>
</section>
<section class="section-tight" style="background:var(--paper)">
  <div class="wrap">
    <div class="section-head center reveal">
      <div class="kicker">How we engage</div>
      <h2>A disciplined path from first call to <span class="serif-accent">results.</span></h2>
    </div>
    <div class="process-grid reveal-stagger">
      <div class="process-cell has-img">
        <div class="pc-img"><img src="https://images.unsplash.com/photo-1497366216548-37526070297c?w=600&q=78&fit=crop" alt="Discovery meeting space — UMCO" loading="lazy" /><i class="pc-step">STEP 01</i></div>
        <div class="pc-body"><h4>Discovery</h4><p>A structured conversation to understand your situation, constraints, and what success looks like.</p></div>
      </div>
      <div class="process-cell has-img">
        <div class="pc-img"><img src="https://images.unsplash.com/photo-1554224154-26032ffc0d07?w=600&q=78&fit=crop" alt="Scoping and proposal documents — UMCO" loading="lazy" /><i class="pc-step">STEP 02</i></div>
        <div class="pc-body"><h4>Scoping &amp; Proposal</h4><p>A fixed-fee proposal with named team members, deliverables, and a timeline you can hold us to.</p></div>
      </div>
      <div class="process-cell has-img">
        <div class="pc-img"><img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&q=78&fit=crop" alt="Execution dashboards — UMCO" loading="lazy" /><i class="pc-step">STEP 03</i></div>
        <div class="pc-body"><h4>Execution</h4><p>Partner-led delivery with scheduled checkpoints — issues surfaced early, never at the deadline.</p></div>
      </div>
      <div class="process-cell has-img">
        <div class="pc-img"><img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=600&q=78&fit=crop" alt="Ongoing advisory — UMCO" loading="lazy" /><i class="pc-step">STEP 04</i></div>
        <div class="pc-body"><h4>Ongoing Counsel</h4><p>Most clients stay. We become the standing advisor your leadership calls before the big decisions.</p></div>
      </div>
    </div>
  </div>
</section>
{cta_band()}""",
     active="services.html")

# ───────────────────────────── INDIVIDUAL SERVICE PAGES ─────────────────────────────
for s in SERVICES:
    offers = "".join(f"""
      <div class="offer-item">{ICON["check"]}<div><h4>{t}</h4><p>{d}</p></div></div>""" for t, d in s["offers"])
    related = "".join(f"""
      <a class="svc-card" href="{SVC[r]["slug"]}.html">
        <div class="svc-icon">{ICON[SVC[r]["icon"]]}</div>
        <h3>{SVC[r]["name"]}</h3>
        <p>{SVC[r]["short"]}</p>
        <span class="text-link">Explore service {ICON["arrow"]}</span>
      </a>""" for r in s["related"])
    hero_img = IMG["svc"][s["slug"]].replace("w=700", "w=1600")
    body = f"""
<section class="page-hero">
  <div class="ph-bg" style="background-image:url('{hero_img}')"></div>
  <div class="ph-veil"></div>
  <div class="wrap">
    <div class="crumb"><a href="../index.html">Home</a><span>/</span><a href="../services.html">Services</a><span>/</span><span>{s["name"]}</span></div>
    <h1>{s["h1"]}</h1>
    <p class="lede">{s["lede"]}</p>
    <div class="hero-ctas">
      <a href="../contact.html" class="btn btn-gold"{CAL_ATTR}>Book Consultation {ICON["arrow"]}</a>
      <a href="https://wa.me/923106569999" target="_blank" rel="noopener" class="btn btn-ghost-light">WhatsApp Us</a>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap detail-grid">
    <div class="detail-body reveal">
      <div class="kicker">Overview</div>
      <h2>{s["name"]}</h2>
      {"".join(f"<p>{p}</p>" for p in s["overview"])}
    </div>
    <div class="reveal">
      <div class="kicker">What's included</div>
      <div class="offer-list">{offers}</div>
    </div>
  </div>
</section>
<section class="section-tight" style="background:var(--paper)">
  <div class="wrap">
    <div class="section-head reveal">
      <div class="kicker">Related services</div>
      <h2>Often engaged <span class="serif-accent">alongside.</span></h2>
    </div>
    <div class="svc-grid reveal-stagger" style="grid-template-columns:repeat(3,1fr)">{related}</div>
  </div>
</section>
{cta_band("../")}"""
    page(f'services/{s["slug"]}.html',
         f'{s["name"]} — UMCO Chartered Accountants',
         s["short"], body, active="services.html")

# ───────────────────────────── ABOUT ─────────────────────────────
page("about.html",
     "About Us — UMCO Chartered Accountants",
     "The story, values, and standards behind Umair Manzoor & Co Chartered Accountants — partner-led professional services in Karachi, Pakistan.",
     f"""
<section class="brand-feature brand-feature--top">
  <div class="wrap reveal">
    <img class="bf-mark" src="logo.png" alt="UM monogram" />
    <div class="bf-rule"><span></span><i>Chartered Accountants</i><span></span></div>
    <h2>Umair Manzoor <span class="amp">&amp;</span> Co</h2>
    <div class="bf-sub">Audit &middot; Tax &middot; Advisory &middot; Digital</div>
    <p class="bf-tag">The name behind every engagement — partner-led assurance and advisory, trusted by businesses across Pakistan and international markets.</p>
  </div>
</section>
<section class="section">
  <div class="wrap split">
    <div class="split-body reveal">
      <div class="kicker">Our story</div>
      <h2 style="font-size:clamp(26px,3.4vw,40px)">Why we <span class="serif-accent">started.</span></h2>
      <p>UMCO was founded in Karachi with a clear purpose: to deliver professional services with direct partner involvement, technical quality, and consistent attention from the first meeting to the final deliverable. We built the firm around a simple principle — senior professionals should remain actively involved throughout every engagement, ensuring that each assignment is handled with care, accountability, and practical insight.</p>
      <p>Today, the practice has served more than 100 businesses across Pakistan, Saudi Arabia, and Canada, including founder-led SMEs, subsidiaries of international groups, and clients requiring audit, tax, review, compilation, Local Content Audit, agreed-upon procedures, advisory, outsourcing, and digital transformation support.</p>
    </div>
    <div class="figure-panel reveal">
      <h3>What we hold ourselves to</h3>
      <div class="fig-rows">
        <div class="fig-row"><span>Engagements led by a partner</span><b>100%</b></div>
        <div class="fig-row"><span>Response time on client queries</span><b>&lt; 1 day</b></div>
        <div class="fig-row"><span>Fee surprises after scoping</span><b>None</b></div>
      </div>
    </div>
  </div>
</section>
<section class="section" style="background:var(--paper)">
  <div class="wrap">
    <div class="section-head reveal">
      <div class="kicker">Values</div>
      <h2>How we <span class="serif-accent">work.</span></h2>
    </div>
    <div class="process-grid reveal-stagger">
      <div class="process-cell"><i>01</i><h4>Independence</h4><p>Our advice has no hidden commercial agenda. We recommend what serves you — including, occasionally, doing nothing.</p></div>
      <div class="process-cell"><i>02</i><h4>Rigour</h4><p>ISA methodology, IFRS fluency, and documentation that survives regulator and investor scrutiny.</p></div>
      <div class="process-cell"><i>03</i><h4>Candour</h4><p>If there's a problem in your numbers, you hear it from us first — early, plainly, with options.</p></div>
      <div class="process-cell"><i>04</i><h4>Continuity</h4><p>The team you meet is the team that delivers. Knowledge of your business compounds year over year.</p></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <div class="kicker">Leadership</div>
      <h2>Meet the people behind the <span class="serif-accent">work.</span></h2>
    </div>
    <div class="reveal"><a href="team.html" class="btn btn-navy">View leadership team {ICON["arrow"]}</a></div>
  </div>
</section>
{cta_band()}""",
     active="about.html")

# ───────────────────────────── TEAM ─────────────────────────────
page("team.html",
     "Leadership — UMCO Chartered Accountants",
     "The leadership of Umair Manzoor & Co Chartered Accountants — partner-led practice across audit, tax, advisory, and digital.",
     f"""
<section class="page-hero">
  <div class="wrap">
    <div class="crumb"><a href="index.html">Home</a><span>/</span><span>Leadership</span></div>
    <h1>Senior people on every <span class="serif-accent">engagement.</span></h1>
    <p class="lede">UMCO is deliberately partner-heavy. The professionals below don't just review the work — they do it.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="team-grid reveal-stagger">
      <div class="team-card" tabindex="0">
        <div class="team-avatar">UM</div>
        <h3>Umair Manzoor</h3>
        <div class="team-role">Founder &amp; Managing Partner — FCA, CPA (USA)</div>
        <p class="team-bio">Fellow Chartered Accountant (FCA) and ICAP member with over 15 years across Big 4 audit, controllership, and CFO-level roles — providing audit and assurance, financial reporting, taxation, and corporate compliance with deep IFRS expertise.</p>
        <div class="team-creds"><span>FCA — ICAP</span><span>CPA (USA)</span><span>Audit, Tax &amp; Advisory</span></div>
        <div class="team-overlay">
          <h3>Umair Manzoor</h3>
          <p>Umair Manzoor is a Fellow Chartered Accountant (FCA) and member of ICAP with over 15 years of experience across Big 4 audit, controllership, and CFO-level roles. He provides audit and assurance, accounting and financial reporting, taxation, and corporate compliance services to businesses across Pakistan — combining deep technical expertise in IFRS with the practical insight of someone who has led finance functions from the inside. He offers the rigour of Big 4 experience with the personal attention of a dedicated partner.</p>
        </div>
      </div>
      <div class="team-card" tabindex="0">
        <div class="team-avatar">ZA</div>
        <h3>Zaid Abid</h3>
        <div class="team-role">Partner — FCA</div>
        <p class="team-bio">Fellow Chartered Accountant with over 15 years of professional experience across audit, finance, taxation, corporate compliance, and advisory services. Previously with Deloitte, Cherat, and Mustaqim — a blend of professional practice and industry experience.</p>
        <div class="team-creds"><span>FCA — ICAP</span><span>Audit, Tax &amp; Advisory</span></div>
        <div class="team-overlay">
          <h3>Zaid Abid</h3>
          <p>Zaid Abid is a Fellow Chartered Accountant with over 15 years professional experience across audit, finance, taxation, corporate compliance, and advisory services. He has previously worked with Deloitte, Cherat, and Mustaqim, bringing a blend of professional practice and industry experience to the firm's client engagements.</p>
        </div>
      </div>
      <div class="team-card">
        <div class="team-avatar">{ICON["advisory"]}</div>
        <h3>Advisory &amp; Digital Practice</h3>
        <div class="team-role">Practice Leadership</div>
        <p class="team-bio">Transaction, consulting, and technology specialists who lead due diligence, valuations, ERP implementations, and finance-function transformation programmes.</p>
        <div class="team-creds"><span>M&amp;A</span><span>Valuations</span><span>ERP</span></div>
      </div>
    </div>
    <p class="reveal" style="margin-top:36px; font-size:14px; color:var(--ink-faint)">Full team profiles are shared during engagement scoping — you'll know exactly who is on your file before you sign.</p>
  </div>
</section>
{cta_band()}""")

# ───────────────────────────── INDUSTRIES ─────────────────────────────
ind_cards = "".join(f"""
      <div class="indx">
        <img src="{IMG["ind"][name]}" alt="{name} industry — UMCO" loading="lazy" />
        <div class="indx-body">
          <div class="indx-icon">{ICON[ic]}</div>
          <h3>{name}</h3>
          <p>{d}</p>
        </div>
      </div>""" for name, d, ic in INDUSTRIES)
page("industries.html",
     "Industries We Serve — UMCO Chartered Accountants",
     "Sector-specific audit, tax, and advisory expertise across manufacturing, retail, technology, healthcare, education, financial services, and more.",
     f"""
<section class="page-hero">
  <div class="ph-bg" style="background-image:url('{IMG["hero_growth"]}')"></div>
  <div class="ph-veil"></div>
  <div class="wrap">
    <div class="crumb"><a href="index.html">Home</a><span>/</span><span>Industries</span></div>
    <h1>Advice that understands your <span class="serif-accent">sector.</span></h1>
    <p class="lede">Generic accounting advice costs money in industries with specific tax regimes, reporting rules, and risk profiles. Ours isn't generic.</p>
  </div>
</section>
<section class="industries section">
  <div class="wrap">
    <div class="indx-grid reveal-stagger">{ind_cards}</div>
  </div>
</section>
<section class="section">
  <div class="wrap split">
    <div class="split-body reveal">
      <div class="kicker">For international investors</div>
      <h2 style="font-size:clamp(26px,3.4vw,40px)">Entering Pakistan? <span class="serif-accent">Start here.</span></h2>
      <p>Foreign companies entering Pakistan face a maze of SECP registration, State Bank exchange controls, and federal-plus-provincial tax regimes. UMCO acts as your single local point of accountability — from entity formation to ongoing compliance — with reporting in the format your head office expects.</p>
      <ul class="tick-list">
        <li>{ICON["check"]} Entity structuring and SECP incorporation</li>
        <li>{ICON["check"]} State Bank approvals and profit repatriation</li>
        <li>{ICON["check"]} Group-policy-aligned IFRS reporting</li>
        <li>{ICON["check"]} One engagement partner for everything</li>
      </ul>
      <div style="margin-top:34px"><a href="services/corporate-advisory.html" class="btn btn-navy">Corporate Advisory {ICON["arrow"]}</a></div>
    </div>
    <div class="figure-panel reveal">
      <h3>Market entry, handled</h3>
      <div class="fig-rows">
        <div class="fig-row"><span>Typical incorporation timeline</span><b>2–4 wks</b></div>
        <div class="fig-row"><span>Registrations managed</span><b>All</b></div>
        <div class="fig-row"><span>Points of contact you need</span><b>1</b></div>
      </div>
    </div>
  </div>
</section>
{cta_band()}""",
     active="industries.html")

# ───────────────────────────── CASE STUDIES ─────────────────────────────
all_cases = "".join(case_card(i, c, with_img=True) for i, c in enumerate(CASES))
page("case-studies.html",
     "Case Studies — UMCO Chartered Accountants",
     "Representative client engagements across tax, audit, advisory, outsourcing, and digital transformation — with measurable outcomes.",
     f"""
<section class="page-hero">
  <div class="ph-bg" style="background-image:url('{IMG["hero_digital"]}')"></div>
  <div class="ph-veil"></div>
  <div class="wrap">
    <div class="crumb"><a href="index.html">Home</a><span>/</span><span>Case Studies</span></div>
    <h1>Results you can <span class="serif-accent">verify.</span></h1>
    <p class="lede">Representative engagements, anonymised to protect client confidentiality. References available on request during scoping.</p>
  </div>
</section>
<section class="section" style="background:var(--paper)">
  <div class="wrap">
    <div class="case-grid reveal-stagger">{all_cases}</div>
  </div>
</section>
{cta_band()}""",
     active="case-studies.html")

# ───────────────────────────── INSIGHTS ─────────────────────────────
all_insights = "".join(f"""
      <a class="insight-card" href="contact.html">
        <div class="insight-meta"><span>{cat}</span><time datetime="{date}">{date}</time></div>
        <h3>{t}</h3>
        <p>{d}</p>
        <span class="read-time" style="margin-top:14px">⏱ {4 + i % 4} min read</span>
        <span class="text-link">Request full briefing {ICON["arrow"]}</span>
      </a>""" for i, (cat, date, t, d) in enumerate(INSIGHTS))
page("insights.html",
     "Insights — UMCO Chartered Accountants",
     "Practical analysis of Pakistan tax, IFRS reporting, and regulatory changes — written for CFOs and business owners.",
     f"""
<section class="page-hero">
  <div class="wrap">
    <div class="crumb"><a href="index.html">Home</a><span>/</span><span>Insights</span></div>
    <h1>Analysis worth your <span class="serif-accent">time.</span></h1>
    <p class="lede">Short, practical briefings on the tax, reporting, and regulatory changes that affect businesses operating in Pakistan.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="insight-grid reveal-stagger">{all_insights}</div>
  </div>
</section>
{cta_band()}""",
     active="insights.html")

# ───────────────────────────── CAREERS ─────────────────────────────
page("careers.html",
     "Careers — UMCO Chartered Accountants",
     "Build a career in audit, tax, and advisory at Umair Manzoor & Co — real client exposure, partner mentorship, and ICAP/ACCA training support.",
     f"""
<section class="page-hero">
  <div class="wrap">
    <div class="crumb"><a href="index.html">Home</a><span>/</span><span>Careers</span></div>
    <h1>Do the work that makes a <span class="serif-accent">career.</span></h1>
    <p class="lede">At UMCO you work directly with partners on real client problems from day one — not three layers down on someone else's checklist.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <div class="kicker">Why join</div>
      <h2>What we <span class="serif-accent">offer.</span></h2>
    </div>
    <div class="process-grid reveal-stagger">
      <div class="process-cell"><i>—</i><h4>Real exposure</h4><p>Client-facing responsibility early, across audit, tax, and advisory — not a single rotation for years.</p></div>
      <div class="process-cell"><i>—</i><h4>Qualification support</h4><p>Structured study leave and mentorship for ICAP and ACCA candidates, with exam-aligned scheduling.</p></div>
      <div class="process-cell"><i>—</i><h4>Partner mentorship</h4><p>Your reviewer is a partner who knows your work, not an anonymous quality function.</p></div>
      <div class="process-cell"><i>—</i><h4>Modern tooling</h4><p>Cloud audit and accounting platforms — we automate the drudgery so you learn judgement, not data entry.</p></div>
    </div>
  </div>
</section>
<section class="section-tight" style="background:var(--paper)">
  <div class="wrap">
    <div class="section-head reveal">
      <div class="kicker">Open positions</div>
      <h2>Current <span class="serif-accent">openings.</span></h2>
      <p>We hire year-round for strong candidates. If none of these fit, write to us anyway.</p>
    </div>
    <div class="offer-list reveal-stagger" style="max-width:720px">
      <a class="offer-item" href="mailto:info@umairmanzoor.com?subject=Application%20—%20Audit%20Senior" style="text-decoration:none">{ICON["check"]}<div><h4>Audit Senior — Karachi</h4><p>3+ years in external audit; ICAP finalist or newly qualified preferred.</p></div></a>
      <a class="offer-item" href="mailto:info@umairmanzoor.com?subject=Application%20—%20Audit%20Associate" style="text-decoration:none">{ICON["check"]}<div><h4>Audit Associate — Karachi</h4><p>1–3 years in external audit; strong working-paper discipline and ICAP progression.</p></div></a>
      <a class="offer-item" href="mailto:info@umairmanzoor.com?subject=Application%20—%20Trainee%20(ICAP/ACCA)" style="text-decoration:none">{ICON["check"]}<div><h4>Trainees — ICAP / ACCA</h4><p>Training contracts with rotation across audit, tax, and advisory.</p></div></a>
    </div>
    <p class="reveal" style="margin-top:28px; font-size:14px; color:var(--ink-muted)">Apply with your CV at <a href="mailto:info@umairmanzoor.com" style="color:var(--gold-deep); font-weight:600">info@umairmanzoor.com</a>.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <div class="kicker">Your trajectory</div>
      <h2>How careers grow <span class="serif-accent">here.</span></h2>
    </div>
    <div class="timeline reveal-stagger">
      <div class="tl-item"><h4><span>Years 0–3</span>Trainee → Associate</h4><p>Rotations across audit, tax, and advisory while you complete ICAP or ACCA — with structured study leave and a partner mentor.</p></div>
      <div class="tl-item"><h4><span>Years 3–5</span>Senior</h4><p>You run fieldwork and client relationships directly, supervising trainees and presenting findings to management.</p></div>
      <div class="tl-item"><h4><span>Years 5–8</span>Manager</h4><p>Full engagement ownership — scoping, delivery, and review — plus a voice in how the practice develops.</p></div>
      <div class="tl-item"><h4><span>Years 8+</span>Director &amp; Partnership Track</h4><p>We promote from within. Every current practice leader started as a trainee somewhere — several of them here.</p></div>
    </div>
  </div>
</section>
{cta_band()}""")

# ───────────────────────────── CONTACT ─────────────────────────────
svc_opts = "".join(f'<option value="{s["slug"]}">{s["name"]}</option>' for s in SERVICES)

if CALENDLY_READY:
    schedule_block = f"""
<section class="section" style="padding-top:0;background:var(--paper)" id="schedule">
  <div class="wrap">
    <div class="section-head center reveal">
      <div class="kicker">Pick a time</div>
      <h2>Book a consultation, <span class="serif-accent">instantly.</span></h2>
      <p>Prefer to skip the form? Choose a slot that suits you and we'll meet by call or video — no back-and-forth.</p>
    </div>
    <div class="calendly-inline-widget reveal" data-url="{CALENDLY_URL}?hide_gdpr_banner=1&amp;primary_color=c6a35d" style="min-width:320px;height:680px"></div>
  </div>
</section>"""
else:
    schedule_block = f"""
<section class="section" style="padding-top:0" id="schedule">
  <div class="wrap">
    <div class="schedule-card reveal">
      <div class="sc-icon">{ICON["calendar"]}</div>
      <div class="sc-body">
        <div class="kicker">Book a consultation</div>
        <h2>Speak with a senior <span class="serif-accent">advisor.</span></h2>
        <p>Reach out and we'll confirm a time that works — by phone, WhatsApp, or email. A senior advisor responds within one business day.</p>
        <div class="sc-actions">
          <a href="#enquiry" class="btn btn-gold">Book online meeting {ICON["arrow"]}</a>
          <a href="tel:+922137120735" class="btn btn-ghost-dark">Call (92) 21 3712 0735</a>
          <a href="https://wa.me/923106569999" target="_blank" rel="noopener" class="btn btn-ghost-dark">WhatsApp us {ICON["arrow"]}</a>
          <a href="mailto:info@umairmanzoor.com" class="btn btn-ghost-dark">Email info@umairmanzoor.com</a>
        </div>
      </div>
    </div>
  </div>
</section>"""
page("contact.html",
     "Contact — Book a Consultation | UMCO Chartered Accountants",
     "Book a consultation with a senior UMCO advisor. Office in Shayan Iconic Tower, Shaheed-e-Millat Road, Karachi. Response within one business day.",
     f"""
<section class="page-hero">
  <div class="wrap">
    <div class="crumb"><a href="index.html">Home</a><span>/</span><span>Contact</span></div>
    <h1>Let's talk about your <span class="serif-accent">business.</span></h1>
    <p class="lede">Tell us what you're dealing with. A senior advisor — not a sales handler — responds within one business day.</p>
  </div>
</section>
<section class="section" id="enquiry">
  <div class="wrap detail-grid" style="grid-template-columns:1fr 1.35fr">
    <div class="reveal">
      <div class="kicker">Reach us directly</div>
      <div class="offer-list">
        <a class="offer-item" href="mailto:info@umairmanzoor.com" style="text-decoration:none">{ICON["check"]}<div><h4>Email</h4><p>info@umairmanzoor.com</p></div></a>
        <a class="offer-item" href="tel:+922137120735" style="text-decoration:none">{ICON["check"]}<div><h4>Phone</h4><p>(92) 21 3712 0735</p></div></a>
        <a class="offer-item" href="https://wa.me/923106569999" target="_blank" rel="noopener" style="text-decoration:none">{ICON["check"]}<div><h4>WhatsApp</h4><p>+92 310 6569999</p></div></a>
        <div class="offer-item">{ICON["check"]}<div><h4>Office</h4><p>Office 205, Shayan Iconic Tower, Plot 5, Block 3, D.M.C.H.S, Shaheed-e-Millat Road, Karachi</p></div></div>
      </div>
      <ul class="tick-list" style="margin-top:30px">
        <li>{ICON["check"]} Completely confidential</li>
        <li>{ICON["check"]} No obligation, no sales pitch</li>
        <li>{ICON["check"]} Response within one business day</li>
      </ul>
    </div>
    <div class="reveal">
      <form class="form-shell" onsubmit="umcoSubmit(event)">
        <div class="form-grid">
          <div class="field"><label for="fname">First name</label><input id="fname" name="fname" type="text" placeholder="Ahmed" required /></div>
          <div class="field"><label for="lname">Last name</label><input id="lname" name="lname" type="text" placeholder="Khan" required /></div>
          <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" placeholder="ahmed@company.com" required /></div>
          <div class="field"><label for="phone">Phone</label><input id="phone" name="phone" type="tel" placeholder="+92 300 000 0000" /></div>
          <div class="field full"><label for="company">Company / organisation</label><input id="company" name="company" type="text" placeholder="Your company name" /></div>
          <div class="field full"><label for="service">Service needed</label>
            <select id="service" name="service" required>
              <option value="" disabled selected>Select a service…</option>
              {svc_opts}
              <option value="other">Not sure — I need guidance</option>
            </select>
          </div>
          <div class="field full"><label for="msg">Tell us about your situation</label><textarea id="msg" name="msg" placeholder="Briefly describe your challenge or what you're looking to achieve…"></textarea></div>
          <button type="submit" class="btn btn-gold form-submit">Request Consultation</button>
        </div>
      </form>
    </div>
  </div>
</section>
{schedule_block}
<section class="section-tight" style="padding-top:0">
  <div class="wrap">
    <div class="section-head reveal" style="margin-bottom:0">
      <div class="kicker">Find us</div>
      <h2>Umair Manzoor &amp; Co. Chartered Accountants, <span class="serif-accent">Shaheed e Millat Road.</span></h2>
    </div>
    <div class="map-shell reveal">
      <iframe title="Umair Manzoor &amp; Co Chartered Accountants — office location" src="https://maps.google.com/maps?q=24.877978,67.0669268&z=17&hl=en&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
    </div>
  </div>
</section>""",
     active="contact.html")

print("\nAll pages generated.")
