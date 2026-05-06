#!/usr/bin/env python3
"""One-time generator for suburb landing pages."""
import os, pathlib

OUT = pathlib.Path(__file__).parent / "areas"
OUT.mkdir(exist_ok=True)

SUBURBS = [
    {"slug":"glen-iris","name":"Glen Iris","postcode":"3146","blurb":"Glen Iris is our home turf. We've worked on weatherboard cottages, double-brick family homes and modern renovations all across the suburb.","landmarks":"From High Street to Gardiners Creek and the Glen Iris shopping strip"},
    {"slug":"malvern","name":"Malvern","postcode":"3144","blurb":"Malvern's mix of heritage Victorians, Edwardians and beautifully renovated homes deserves careful, detailed maintenance work.","landmarks":"Around Glenferrie Road, Malvern Gardens and the Stonnington area"},
    {"slug":"malvern-east","name":"Malvern East","postcode":"3145","blurb":"From Central Park to Waverley Road, Malvern East homes get a lot of weather – we keep exteriors looking sharp year-round.","landmarks":"Near Central Park, Darling Station and Waverley Road"},
    {"slug":"camberwell","name":"Camberwell","postcode":"3124","blurb":"Camberwell's leafy streets and period homes are a great fit for our quality painting and pressure cleaning services.","landmarks":"Around Camberwell Junction, Burke Road and Riversdale Road"},
    {"slug":"hawthorn-east","name":"Hawthorn East","postcode":"3123","blurb":"We service homes throughout Hawthorn East, from Auburn Road through to the boundary with Camberwell.","landmarks":"Near Auburn Village, Anderson Park and Camberwell Road"},
    {"slug":"ashburton","name":"Ashburton","postcode":"3147","blurb":"Ashburton's family homes benefit from regular exterior cleaning and painting – we're just up the road in Glen Iris.","landmarks":"Around High Street Ashburton, Y-Water Centre and Markham Reserve"},
    {"slug":"toorak","name":"Toorak","postcode":"3142","blurb":"Discreet, premium exterior maintenance for Toorak homes – with the care these properties deserve.","landmarks":"From Toorak Village to Heyington Place and Orrong Road"},
    {"slug":"armadale","name":"Armadale","postcode":"3143","blurb":"From High Street's period terraces to Armadale's family homes, our team brings tidy, careful workmanship.","landmarks":"Around High Street Armadale, Kings Arcade and Dandenong Road"},
    {"slug":"kooyong","name":"Kooyong","postcode":"3144","blurb":"A small, tightly-held suburb that we know well – careful exterior care for Kooyong homes.","landmarks":"Near Kooyong Park, Kooyong Station and Glenferrie Road"},
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Property Maintenance {name} VIC {postcode} | Painting & Pressure Cleaning | Primo</title>
<meta name="description" content="Local property maintenance in {name} VIC {postcode}. House painting, high-pressure cleaning, deck restoration & exterior care from Glen Iris-based Primo Property Maintenance. Call 0403 186 353.">
<meta name="keywords" content="property maintenance {name}, house painter {name}, pressure cleaning {name} {postcode}, exterior cleaning {name} VIC">
<link rel="canonical" href="https://primopropertymaintenance.com.au/areas/{slug}.html">
<meta property="og:title" content="Property Maintenance {name} VIC | Primo">
<meta property="og:description" content="Painting, pressure cleaning, deck restoration and exterior maintenance in {name} {postcode}.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://primopropertymaintenance.com.au/areas/{slug}.html">
<link rel="stylesheet" href="../css/styles.css">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Primo Property Maintenance",
  "image": "https://primopropertymaintenance.com.au/images/area-{slug}.jpg",
  "url": "https://primopropertymaintenance.com.au/areas/{slug}.html",
  "telephone": "+61403186353",
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "26 Martin Road",
    "addressLocality": "Glen Iris",
    "addressRegion": "VIC",
    "postalCode": "3146",
    "addressCountry": "AU"
  }},
  "areaServed": {{
    "@type": "Place",
    "name": "{name}, VIC {postcode}, Australia"
  }},
  "priceRange": "$$"
}}
</script>
</head>
<body>

<header class="site-header">
  <div class="header-inner">
    <a href="../index.html" class="logo">Primo<span> Property Maintenance</span></a>
    <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">☰</button>
    <nav class="nav" aria-label="Main">
      <a href="../index.html">Home</a>
      <a href="../services.html">Services</a>
      <a href="../areas.html" class="active">Service Areas</a>
      <a href="../about.html">About</a>
      <a href="../contact.html">Contact</a>
      <a href="tel:0403186353" class="btn-cta">Call 0403 186 353</a>
    </nav>
  </div>
</header>

<div class="breadcrumbs">
  <div class="container"><a href="../index.html">Home</a> &rsaquo; <a href="../areas.html">Service Areas</a> &rsaquo; {name}</div>
</div>

<section class="hero" style="padding: 50px 0 40px;">
  <div class="container">
    <h1>Property Maintenance in {name} VIC {postcode}</h1>
    <p class="lede">House painting, pressure cleaning, deck restoration and exterior care for {name} homes – delivered by your local Glen Iris team.</p>
    <div class="hero-actions">
      <a href="tel:0403186353" class="btn btn-primary">Call 0403 186 353</a>
      <a href="../contact.html" class="btn btn-outline">Free Quote</a>
    </div>
  </div>
</section>

<section>
  <div class="container two-col">
    <div>
      <h2>Your local property maintenance team in {name}</h2>
      <p>{blurb}</p>
      <p>{landmarks}, we look after exterior painting, pressure cleaning, deck restoration, paver sealing and general property maintenance for residential and commercial clients.</p>
      <p>Because we're based just a few minutes away in Glen Iris, we can be on-site quickly to quote and start work – and we know the streets, weather and styles of homes in {name} like the back of our hand.</p>
      <ul class="why-list">
        <li>Fully insured local team</li>
        <li>Free, no-obligation quotes in {name}</li>
        <li>Quality materials and proper preparation</li>
        <li>Tidy site, careful workmanship</li>
      </ul>
    </div>
    <div class="placeholder-img large">[ {name} Project Photo ]</div>
  </div>
</section>

<section class="alt">
  <div class="container">
    <h2 class="section-title">Services we offer in {name}</h2>
    <p class="section-sub">All of our services are available throughout {name} {postcode}.</p>
    <div class="grid">
      <article class="card"><div class="placeholder-img">[ Painting ]</div><div class="card-body"><h3>House Painting in {name}</h3><p>Interior and exterior repaints with thorough prep and quality finishes.</p><a href="../services.html#painting">Service details →</a></div></article>
      <article class="card"><div class="placeholder-img">[ Pressure Cleaning ]</div><div class="card-body"><h3>Pressure Cleaning {name}</h3><p>Driveways, paths, patios and walls cleaned back to looking great.</p><a href="../services.html#pressure-cleaning">Service details →</a></div></article>
      <article class="card"><div class="placeholder-img">[ House Wash ]</div><div class="card-body"><h3>House Wash Downs {name}</h3><p>Soft and pressure washing for brick, render and weatherboard homes.</p><a href="../services.html#house-washing">Service details →</a></div></article>
      <article class="card"><div class="placeholder-img">[ Decks ]</div><div class="card-body"><h3>Deck Restoration {name}</h3><p>Sand, clean and re-coat decks for years of additional life.</p><a href="../services.html#deck-restoration">Service details →</a></div></article>
      <article class="card"><div class="placeholder-img">[ Pavers ]</div><div class="card-body"><h3>Paver Cleaning &amp; Sealing</h3><p>Deep clean and seal pavers and pool surrounds in {name}.</p><a href="../services.html#paver-cleaning">Service details →</a></div></article>
      <article class="card"><div class="placeholder-img">[ Pool ]</div><div class="card-body"><h3>Pool Cleaning {name}</h3><p>One-off and routine residential pool cleaning.</p><a href="../services.html#pool-cleaning">Service details →</a></div></article>
    </div>
  </div>
</section>

<section class="cta-strip">
  <h2>Ready to get a quote in {name}?</h2>
  <p>Pick up the phone or send a quick enquiry – we'll come out and take a look.</p>
  <a href="tel:0403186353" class="btn btn-primary">Call 0403 186 353</a>
</section>

<section>
  <div class="container">
    <h2 class="section-title">Other suburbs we service</h2>
    <div class="areas-grid">
{nearby_pills}
    </div>
  </div>
</section>

<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <h4>Primo Property Maintenance</h4>
        <p>26 Martin Road<br>Glen Iris VIC 3146</p>
        <p><a href="tel:0403186353">0403 186 353</a></p>
      </div>
      <div>
        <h4>Quick Links</h4>
        <ul>
          <li><a href="../index.html">Home</a></li>
          <li><a href="../services.html">Services</a></li>
          <li><a href="../areas.html">Service Areas</a></li>
          <li><a href="../about.html">About</a></li>
          <li><a href="../contact.html">Contact</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      &copy; <span data-year></span> Primo Property Maintenance. All rights reserved.
    </div>
  </div>
</footer>

<script src="../js/main.js"></script>
</body>
</html>
"""

for s in SUBURBS:
    nearby = [o for o in SUBURBS if o["slug"] != s["slug"]]
    pills = "\n".join(
        f'      <a class="area-pill" href="{o["slug"]}.html">{o["name"]}</a>' for o in nearby
    )
    html = TEMPLATE.format(
        slug=s["slug"], name=s["name"], postcode=s["postcode"],
        blurb=s["blurb"], landmarks=s["landmarks"], nearby_pills=pills,
    )
    (OUT / f'{s["slug"]}.html').write_text(html, encoding="utf-8")
    print("wrote", s["slug"])
print("done")
