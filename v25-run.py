#!/usr/bin/env python3
"""
v2.5 Full Rebuild — Jacksonville Epoxy Flooring (904epoxyfloors.com)
Run from site root: python3 v25-run.py
"""
import os, re, shutil
from pathlib import Path

ROOT = Path(__file__).parent
HVAC_CSS = Path("/Users/costa.demetral/Documents/Rank and Rent $/My-RR-Sites/Huntsville-HVAC-Pros/docs/css/style.v2.5.css")

DOMAIN = "904epoxyfloors.com"
PHONE = "(904) 204-4753"
PHONE_LINK = "tel:+19042044753"
SITE_NAME = "Jacksonville Epoxy Flooring Pros"

# ── NAV ────────────────────────────────────────────────────────────────────
NAV = '''<nav class="nav" id="nav">
  <div class="nav__inner">
    <a href="/" class="nav__logo">JAX <span>Epoxy</span></a>
    <ul class="nav__links" id="navLinks">
      <li><a href="/services/">Services</a></li>
      <li><a href="/locations/">Areas</a></li>
      <li><a href="/blog/">Blog</a></li>
      <li><a href="/contact.html">Contact</a></li>
      <li><a href="tel:+19042044753" class="nav__cta">Call Now</a></li>
    </ul>
    <button class="nav__toggle" id="navToggle" aria-label="Open menu">
      <svg viewBox="0 0 24 24"><path d="M3 12h18M3 6h18M3 18h18" stroke="currentColor" stroke-width="2" stroke-linecap="round" fill="none"/></svg>
    </button>
  </div>
</nav>'''

# ── FOOTER ─────────────────────────────────────────────────────────────────
FOOTER = '''<footer class="footer">
  <div class="container">
    <div class="footer__grid">
      <div class="footer__col footer__col--brand">
        <div class="footer__brand-name">JAX <span>Epoxy</span></div>
        <p class="footer__brand-desc">Jacksonville&rsquo;s trusted epoxy flooring experts. Garage floors, metallic &amp; commercial coatings built for Florida&rsquo;s humidity. 15-year warranty on every job.</p>
        <div class="footer__contact-item"><a href="tel:+19042044753">(904) 204-4753</a></div>
        <div class="footer__contact-item"><a href="mailto:info@904epoxyfloors.com">info@904epoxyfloors.com</a></div>
      </div>
      <div class="footer__col">
        <h4 class="footer__heading">Services</h4>
        <ul class="footer__links">
          <li><a href="/services/garage-floor-epoxy.html">Garage Floor Epoxy</a></li>
          <li><a href="/services/metallic-epoxy.html">Metallic Epoxy</a></li>
          <li><a href="/services/polyaspartic-coating.html">Polyaspartic Coating</a></li>
          <li><a href="/services/commercial-epoxy.html">Commercial Epoxy</a></li>
          <li><a href="/services/">All Services</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h4 class="footer__heading">Service Areas</h4>
        <ul class="footer__links">
          <li><a href="/">Jacksonville</a></li>
          <li><a href="/locations/orange-park.html">Orange Park</a></li>
          <li><a href="/locations/fleming-island.html">Fleming Island</a></li>
          <li><a href="/locations/st-augustine.html">St. Augustine</a></li>
          <li><a href="/locations/ponte-vedra.html">Ponte Vedra</a></li>
          <li><a href="/locations/fernandina-beach.html">Fernandina Beach</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h4 class="footer__heading">Contact</h4>
        <div class="footer__contact-item"><a href="tel:+19042044753">(904) 204-4753</a></div>
        <div class="footer__contact-item">info@904epoxyfloors.com</div>
        <div class="footer__contact-item">Jacksonville &amp; Northeast Florida</div>
        <div class="footer__contact-item"><a href="/contact.html">Get Free Estimate &rarr;</a></div>
      </div>
    </div>
    <div class="footer__bottom">
      <span class="footer__copy">&copy; 2026 Jacksonville Epoxy Flooring Pros. All rights reserved. FL Licensed Contractor.</span>
      <div class="footer__legal">
        <a href="/privacy-policy.html">Privacy Policy</a>
        <a href="/sitemap.xml">Sitemap</a>
      </div>
    </div>
  </div>
</footer>
<div class="mobile-cta">
  <a href="tel:+19042044753" class="mobile-cta__btn mobile-cta__btn--call">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg>
    Call Now
  </a>
  <a href="/contact.html#contact" class="mobile-cta__btn mobile-cta__btn--estimate">Free Estimate</a>
</div>
<script>
document.documentElement.classList.add("js");
var nav=document.getElementById('nav');
if(nav)window.addEventListener('scroll',function(){nav.classList.toggle('scrolled',window.scrollY>60)},{passive:true});
var nt=document.getElementById('navToggle');
if(nt)nt.addEventListener('click',function(){document.getElementById('navLinks').classList.toggle('open');});
document.querySelectorAll('.faq__question').forEach(function(btn){
  btn.addEventListener('click',function(){
    var item=btn.closest('.faq__item');
    var isOpen=item.classList.contains('active');
    document.querySelectorAll('.faq__item').forEach(function(i){i.classList.remove('active');});
    if(!isOpen)item.classList.add('active');
  });
});
var revEls=document.querySelectorAll('.reveal');
if(revEls.length){
  var obs=new IntersectionObserver(function(entries){
    entries.forEach(function(e){if(e.isIntersecting){e.target.classList.add('visible');obs.unobserve(e.target);}});
  },{threshold:0.15});
  revEls.forEach(function(el){obs.observe(el);});
}
</script>'''

# ── JS inline ──────────────────────────────────────────────────────────────
JS = '''<script>
document.documentElement.classList.add("js");
var nav=document.getElementById('nav');
if(nav)window.addEventListener('scroll',function(){nav.classList.toggle('scrolled',window.scrollY>60)},{passive:true});
var nt=document.getElementById('navToggle');
if(nt)nt.addEventListener('click',function(){document.getElementById('navLinks').classList.toggle('open');});
document.querySelectorAll('.faq__question').forEach(function(btn){
  btn.addEventListener('click',function(){
    var item=btn.closest('.faq__item');
    var isOpen=item.classList.contains('active');
    document.querySelectorAll('.faq__item').forEach(function(i){i.classList.remove('active');});
    if(!isOpen)item.classList.add('active');
  });
});
var revEls=document.querySelectorAll('.reveal');
if(revEls.length){
  var obs=new IntersectionObserver(function(entries){
    entries.forEach(function(e){if(e.isIntersecting){e.target.classList.add('visible');obs.unobserve(e.target);}});
  },{threshold:0.15});
  revEls.forEach(function(el){obs.observe(el);});
}
</script>'''

CLARITY = '''<script type="text/javascript">
(function(c,l,a,r,i,t,y){
c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
})(window,document,"clarity","script","vqc7u895rm");
</script>'''

TRUST_BAR = '''<div class="trust-bar">
  <div class="container">
    <div class="trust-bar__inner">
      <div class="trust-bar__item">
        <div class="trust-bar__icon"><svg viewBox="0 0 24 24" fill="none" stroke="var(--color-accent)" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
        FL Licensed &amp; Insured
      </div>
      <div class="trust-bar__item">
        <div class="trust-bar__icon"><svg viewBox="0 0 24 24" fill="none" stroke="var(--color-accent)" stroke-width="2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg></div>
        4.9 Google Rating
      </div>
      <div class="trust-bar__item">
        <div class="trust-bar__icon"><svg viewBox="0 0 24 24" fill="none" stroke="var(--color-accent)" stroke-width="2"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg></div>
        15-Year Warranty
      </div>
      <div class="trust-bar__item">
        <div class="trust-bar__icon"><svg viewBox="0 0 24 24" fill="none" stroke="var(--color-accent)" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div>
        Free Estimates
      </div>
    </div>
  </div>
</div>'''

INNER_HERO_BUTTONS = '''      <div class="hero__buttons">
        <a href="tel:+19042044753" class="btn btn--primary">
          <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg>
          Call (904) 204-4753
        </a>
        <a href="/contact.html#contact" class="btn btn--ghost">Get Free Estimate</a>
      </div>'''

CTA_SECTION = '''<section class="cta-section">
  <div class="container">
    <div class="cta__urgency"><span class="cta__urgency-dot"></span>Free Estimates Available</div>
    <h2 class="cta__title">Ready to Transform Your Floor?</h2>
    <p class="cta__desc">Free on-site estimates. Written quote before any work starts. Coatings built for Florida&rsquo;s climate &amp; humidity.</p>
    <div class="cta__buttons">
      <a href="tel:+19042044753" class="btn btn--white">Call (904) 204-4753</a>
      <a href="/contact.html#contact" class="btn btn--outline">Request Free Estimate</a>
    </div>
  </div>
</section>'''

HEAD_COMMON = '''  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="sitemap" type="application/xml" href="/sitemap.xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;900&display=swap" rel="stylesheet">'''


# ── HELPERS ─────────────────────────────────────────────────────────────────
def strip_emojis(html):
    html = html.replace('\U0001f4de', '').replace('\U0001f5d3', '')
    html = html.replace('\U0001f4f1', '').replace('\u2705', '')
    html = html.replace('\u2b50', '').replace('\U0001f3e0', '')
    html = html.replace('\U0001f527', '').replace('\U0001f4e6', '')
    html = re.sub(r'[\U0001F300-\U0001F9FF]', '', html)
    html = re.sub(r'&#128222;', '', html)  # phone emoji HTML entity
    return html


def fix_css_link(html, depth=0):
    rel = '../' * depth
    new = f'<link rel="stylesheet" href="{rel}css/style.v2.5.css">'
    html = re.sub(r'<link[^>]+styles\.v1\.css[^>]*>', new, html)
    html = re.sub(r'<link[^>]+style\.v2\.5\.css[^>]*>', new, html)  # fix double
    html = re.sub(r'<link[^>]+programmatic-pages\.css[^>]*>\s*', '', html)
    html = re.sub(r'<link[^>]+Outfit[^>]+>\s*', '', html)
    html = re.sub(r'<script[^>]+phosphor-icons[^>]+></script>\s*', '', html)
    return html


def fix_og(html):
    html = html.replace('og-image.webp', 'og-image.jpg')
    if 'og:image:width' not in html and 'og-image.jpg' in html:
        html = html.replace(
            '<meta property="og:image"',
            '<meta property="og:image:width" content="1200">\n  <meta property="og:image:height" content="630">\n  <meta property="og:image"'
        )
    return html


def ensure_atc(html):
    if 'apple-touch-icon' not in html:
        html = html.replace('</head>', '  <link rel="apple-touch-icon" href="/apple-touch-icon.png">\n</head>', 1)
    return html


def fix_contact_links(html):
    html = html.replace('href="/#contact"', 'href="/contact.html#contact"')
    html = re.sub(r'href="(?:\.\./)*#contact"', 'href="/contact.html#contact"', html)
    return html


def replace_nav(html):
    """Replace old header/nav block with v2.5 nav"""
    html = re.sub(
        r'<header[^>]*>.*?</header>\s*(?:<div class="mobile-menu">.*?</div>\s*)?',
        NAV + '\n',
        html, count=1, flags=re.DOTALL
    )
    return html


def replace_footer(html):
    """Replace old footer + scripts with v2.5 footer"""
    m = re.search(r'<footer[^>]*>', html)
    if not m:
        # Add footer before </body>
        html = html.replace('</body>', FOOTER + '\n</body>')
        return html
    foot_start = m.start()
    # Find end of footer
    foot_end_m = re.search(r'</footer>', html[foot_start:])
    if not foot_end_m:
        return html
    foot_end = foot_start + foot_end_m.end()
    
    pre = html[:foot_start]
    post = html[foot_end:]
    
    # Clean post: remove old mobile-cta, old scripts, old styles
    post = re.sub(r'<style[^>]*>[\s\S]*?\.mobile-cta[\s\S]*?</style>', '', post)
    post = re.sub(r'<div class="mobile-cta"[^>]*>[\s\S]*?</div>', '', post)
    post = re.sub(r'<div[^>]+floating-cta[\s\S]*?</div>\s*<script>[\s\S]*?</script>', '', post)
    post = re.sub(r'<script src=["\'][^"\']*main\.js["\'][^>]*></script>', '', post)
    post = re.sub(r'<script[^>]*>[\s\S]*?function\s+gtag[\s\S]*?</script>', '', post)
    post = re.sub(r'\s*</body>\s*</html>\s*$', '', post)
    
    return pre + '\n' + FOOTER + '\n</body>\n</html>\n'


def fix_hero_inner(html):
    """Ensure inner page hero has .hero--inner and .hero__title"""
    # If page-hero class found, convert
    if 'class="page-hero' in html or 'class="location-hero' in html:
        def rebuild_hero(m):
            content = m.group(1)
            h_m = re.search(r'<h[12][^>]*>(.*?)</h[12]>', content, re.DOTALL)
            p_m = re.search(r'<p[^>]*>(.*?)</p>', content, re.DOTALL)
            h1 = h_m.group(1).strip() if h_m else 'Service'
            desc = p_m.group(1).strip() if p_m else ''
            return (f'<section class="hero hero--inner">\n  <div class="container">\n'
                    f'    <div class="hero__content">\n'
                    f'      <div class="hero__badge">904 Epoxy Floors &mdash; Jacksonville, FL</div>\n'
                    f'      <h1 class="hero__title">{h1}</h1>\n'
                    + (f'      <p class="hero__desc">{desc}</p>\n' if desc else '')
                    + INNER_HERO_BUTTONS + '\n'
                    f'    </div>\n  </div>\n</section>')
        html = re.sub(
            r'<section class="(?:page-hero|location-hero)[^"]*">(.*?)</section>',
            rebuild_hero, html, count=1, flags=re.DOTALL
        )
    # Also ensure hero--inner has .hero__title on existing h1
    if 'hero--inner' in html and 'hero__title' not in html:
        html = re.sub(
            r'(<section class="hero hero--inner"[^>]*>.*?<h1)(\s+[^>]*>|>)',
            r'\1 class="hero__title"\2',
            html, count=1, flags=re.DOTALL
        )
    return html


def fix_btn_classes(html):
    """Normalize button class names to v2.5"""
    html = re.sub(r'class="btn btn-primary"', 'class="btn btn--primary"', html)
    html = re.sub(r'class="btn btn-secondary"', 'class="btn btn--outline"', html)
    html = re.sub(r'class="btn btn--ghost\b', 'class="btn btn--outline', html)
    html = re.sub(r'class="btn btn--ghost-light\b', 'class="btn btn--outline', html)
    return html


def process_page(path, depth=0):
    """Apply all v2.5 patches to a page"""
    html = path.read_text(encoding='utf-8')
    html = fix_css_link(html, depth)
    html = fix_og(html)
    html = ensure_atc(html)
    html = strip_emojis(html)
    html = fix_contact_links(html)
    html = replace_nav(html)
    html = replace_footer(html)
    html = fix_hero_inner(html)
    html = fix_btn_classes(html)
    path.write_text(html, encoding='utf-8')
    print(f'  ✅ {path.relative_to(ROOT)}')


# ── NEIGHBORHOOD PAGE REBUILD ───────────────────────────────────────────────
def rebuild_neighborhood(path):
    html = path.read_text(encoding='utf-8')

    slug = path.stem
    neigh = slug.replace('garage-epoxy-in-', '').replace('-', ' ').title()

    title_m = re.search(r'<title>([^<]+)</title>', html)
    desc_m = re.search(r'<meta name="description" content="([^"]+)"', html)
    canonical_m = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    h1_m = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)

    title = title_m.group(1) if title_m else f'Garage Floor Epoxy in {neigh} | 904 Epoxy Floors'
    desc = desc_m.group(1) if desc_m else f'Professional epoxy flooring in {neigh}, Jacksonville FL. Free estimates. 15-year warranty.'
    canonical = canonical_m.group(1) if canonical_m else f'https://{DOMAIN}/neighborhoods/{path.name}'
    h1_text = re.sub(r'<[^>]+>', '', h1_m.group(1)).strip() if h1_m else f'Garage Floor Epoxy in {neigh}'

    # Extract schemas
    schemas = re.findall(r'(<script type="application/ld\+json">.*?</script>)', html, re.DOTALL)
    schemas_html = '\n'.join(schemas)

    # Extract geo tags
    geo_m = re.search(r'<meta name="geo\.position" content="([^"]+)"', html)
    geo = f'<meta name="geo.position" content="{geo_m.group(1)}">' if geo_m else ''

    # Extract main article content
    main_content = ''
    # Try main-content div first
    mc_m = re.search(r'<div class="main-content">(.*?)(?:<aside|</div>\s*</div>\s*</article)', html, re.DOTALL)
    if mc_m:
        main_content = mc_m.group(1)
    else:
        # Try article
        art_m = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)
        if art_m:
            main_content = art_m.group(1)
            # Remove content-wrapper and main-content wrappers
            main_content = re.sub(r'<div class="content-wrapper"[^>]*>\s*<div class="main-content">\s*', '', main_content)
        else:
            # Try programmatic-page main
            main_m = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
            if main_m:
                main_content = main_m.group(1)

    # Remove h1 (goes in hero), sidebar, old breadcrumb
    main_content = re.sub(r'<h1[^>]*>.*?</h1>', '', main_content, flags=re.DOTALL)
    main_content = re.sub(r'<aside[^>]*>.*?</aside>', '', main_content, flags=re.DOTALL)
    main_content = re.sub(r'<div class="sidebar">.*?</div>', '', main_content, flags=re.DOTALL)
    main_content = re.sub(r'<nav class="breadcrumb"[^>]*>.*?</nav>', '', main_content, flags=re.DOTALL)
    main_content = strip_emojis(main_content)
    main_content = fix_contact_links(main_content)
    main_content = fix_btn_classes(main_content)
    # Fix relative image paths for neighborhoods (root-relative)
    main_content = main_content.strip()

    # Extract nearby areas
    nearby_links = re.findall(r'<a href="(/neighborhoods/[^"]+)"[^>]*class="nearby-link"[^>]*>([^<]+)</a>', html)
    nearby_html = ''
    if nearby_links:
        links_html = ''.join(
            f'<a href="{href}" style="background:var(--color-white);border:1px solid #e2e8f0;padding:10px 20px;border-radius:8px;font-weight:600;color:var(--color-text);transition:all .2s;">{name}</a>'
            for href, name in nearby_links
        )
        nearby_html = f'''
<section class="why" style="background:var(--color-surface);">
  <div class="container">
    <div class="why__header" style="text-align:center;max-width:680px;margin:0 auto 2rem;">
      <span class="section-label">Nearby Areas</span>
      <h2 class="section-title" style="color:var(--color-text);">Other Jacksonville Neighborhoods We Serve</h2>
    </div>
    <div style="display:flex;flex-wrap:wrap;gap:12px;justify-content:center;">
      {links_html}
    </div>
  </div>
</section>'''

    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:image" content="https://{DOMAIN}/images/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:locale" content="en_US">
  <meta property="og:site_name" content="{SITE_NAME}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://{DOMAIN}/images/og-image.jpg">
  <meta name="geo.region" content="US-FL">
  <meta name="geo.placename" content="{neigh}">
  {geo}
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#1a1a2e">
  {HEAD_COMMON}
  <link rel="stylesheet" href="/css/style.v2.5.css">
  {schemas_html}
  {CLARITY}
</head>
<body>

{NAV}

<section class="hero hero--inner">
  <div class="container">
    <div class="hero__content">
      <div class="hero__badge">
        <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        Jacksonville, FL
      </div>
      <h1 class="hero__title">{h1_text}</h1>
      <p class="hero__desc">Florida-grade prep. Moisture-vapor barrier. 15-year warranty. Free estimates.</p>
{INNER_HERO_BUTTONS}
    </div>
  </div>
</section>

{TRUST_BAR}

<section class="why" style="background:var(--color-white);">
  <div class="container">
    <div style="max-width:860px;margin:0 auto;">
{main_content if main_content else f"<p>Professional garage floor epoxy services in {neigh}, Jacksonville. FL licensed, 15-year warranty. Call <a href='tel:+19042044753'>(904) 204-4753</a>.</p>"}
    </div>
  </div>
</section>

{nearby_html}

{CTA_SECTION.replace("Ready to Transform Your Floor?", f"Ready to Transform Your {neigh} Garage?")}

{FOOTER}
</body>
</html>'''

    path.write_text(page, encoding='utf-8')
    print(f'  ✅ {path.relative_to(ROOT)}')


# ── CSS BUILD ───────────────────────────────────────────────────────────────
def build_css():
    css = HVAC_CSS.read_text()
    # Amber palette
    css = css.replace('--color-accent: #0ea5e9', '--color-accent: #f59e0b')
    css = css.replace('--color-accent-dark: #0284c7', '--color-accent-dark: #d97706')
    css = css.replace('--color-accent-glow: rgba(14, 165, 233, 0.3)', '--color-accent-glow: rgba(245, 158, 11, 0.3)')
    css = css.replace('#0ea5e9', '#f59e0b')
    css = css.replace('#0284c7', '#d97706')
    css = css.replace('rgba(14, 165, 233,', 'rgba(245, 158, 11,')
    css = css.replace('rgba(14,165,233,', 'rgba(245,158,11,')
    css = css.replace('14, 165, 233', '245, 158, 11')
    # Hero title gradient
    css = css.replace(
        'background: linear-gradient(135deg, var(--color-accent), #38bdf8);',
        'background: linear-gradient(135deg, var(--color-accent), #fbbf24);'
    )
    # Process card hover border (has hardcoded color)
    css = css.replace('rgba(14, 165, 233, 0.3)', 'rgba(245, 158, 11, 0.3)')
    # Related card icon bg
    css = css.replace('rgba(14, 165, 233, 0.1)', 'rgba(245, 158, 11, 0.1)')
    css = css.replace('rgba(14, 165, 233, 0.12)', 'rgba(245, 158, 11, 0.12)')
    css = css.replace('rgba(14, 165, 233, 0.15)', 'rgba(245, 158, 11, 0.15)')

    # Process card hover border color
    css = css.replace('border-color: rgba(14, 165, 233, 0.3)', 'border-color: rgba(245, 158, 11, 0.3)')

    # Update header comment
    css = '/* style.v2.5.css — Jacksonville Epoxy Flooring | amber palette */\n' + css

    out = ROOT / 'css' / 'style.v2.5.css'
    out.parent.mkdir(exist_ok=True)
    out.write_text(css)
    print(f'  ✅ css/style.v2.5.css written ({len(css):,} chars)')


# ── MAIN ────────────────────────────────────────────────────────────────────
def main():
    print('\n=== v2.5 Full Rebuild — Jacksonville Epoxy ===\n')

    print('1. Building CSS...')
    build_css()

    print('\n2. Processing index.html (pre-built)...')
    idx = ROOT / 'index.html'
    if idx.exists():
        # index.html is written separately as a proper file
        html = idx.read_text()
        # Just ensure CSS link is correct (it's written fresh with correct link)
        print('  ✅ index.html (written separately)')

    print('\n3. Patching service pages...')
    for f in sorted((ROOT / 'services').glob('*.html')):
        if f.name == 'index.html':
            continue
        process_page(f, depth=1)

    print('\n4. Patching location pages...')
    for f in sorted((ROOT / 'locations').glob('*.html')):
        if f.name == 'index.html':
            continue
        process_page(f, depth=1)

    print('\n5. Rebuilding neighborhood pages...')
    for f in sorted((ROOT / 'neighborhoods').glob('*.html')):
        rebuild_neighborhood(f)

    print('\n6. Patching blog pages...')
    blog_dir = ROOT / 'blog'
    if blog_dir.exists():
        for f in sorted(blog_dir.glob('*.html')):
            process_page(f, depth=1)
        # blog index
        bi = blog_dir / 'index.html'
        if bi.exists():
            process_page(bi, depth=1)

    print('\n7. Patching root pages...')
    for fname in ['privacy-policy.html', '404.html', 'thank-you.html']:
        fp = ROOT / fname
        if fp.exists():
            process_page(fp, depth=0)

    print('\n✅ All pages processed!')
    print('\nNow run the checklist to verify:')
    print(f'  python3 /Users/costa.demetral/Documents/Rank\\ and\\ Rent\\ \\$/tools/v25-retrofit-checklist.py --site . --domain {DOMAIN}')


if __name__ == '__main__':
    main()
