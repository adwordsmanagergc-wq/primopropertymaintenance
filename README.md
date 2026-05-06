# Primo Property Maintenance – Website

Simple static website for **Primo Property Maintenance**, a property maintenance business based in Glen Iris, VIC. Built as plain HTML/CSS/JS so it can be hosted anywhere (Netlify, Vercel, GitHub Pages, cPanel, S3, etc.) with no build step.

## Pages

- `index.html` – home page
- `services.html` – services overview
- `about.html` – about the business
- `contact.html` – contact details and quote form (placeholder action)
- `areas.html` – service areas index
- `areas/<suburb>.html` – SEO-optimised landing page per suburb

### Suburb landing pages (9)

Glen Iris, Malvern, Malvern East, Camberwell, Hawthorn East, Ashburton, Toorak, Armadale, Kooyong.

Each page has unique title, meta description, H1, body copy and `LocalBusiness` schema with the suburb in `areaServed`.

## Contact details used

- **Address:** 26 Martin Road, Glen Iris VIC 3146
- **Phone:** 0403 186 353
- **Hours (assumed):** Mon–Sat, 7:00am–6:00pm

Update these in each HTML file (and in `index.html`'s JSON-LD) if any are wrong.

## Images

All images are placeholders rendered as styled `<div class="placeholder-img">` blocks. Drop real photos into `images/` and replace each placeholder with an `<img>` tag. See `images/README.md` for suggested filenames.

## Contact form

The form on `contact.html` currently shows a placeholder alert on submit. To make it work, point `action` at a form handler such as Formspree, Netlify Forms, or a custom backend.

## SEO files

- `sitemap.xml` – list of public URLs
- `robots.txt` – allows all bots, points to the sitemap

Update the canonical domain references throughout if hosting at a different URL.

## Local preview

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

## Regenerating suburb pages

`build_suburbs.py` is a one-time generator. Edit the `SUBURBS` list and run:

```bash
python3 build_suburbs.py
```
