# Swarved Mahamandir Dham — Official Website

A modern, serene Django website for the Swarved Mahamandir — one of the
largest meditation centres in the world.

## Quick start

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/Scripts/activate   # (Git Bash on Windows)

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply migrations
python manage.py migrate

# 4. Run the dev server
python manage.py runserver

# 5. Open in browser
#    http://127.0.0.1:8000/
```

## Project structure

```
mahamandir/
├── manage.py
├── requirements.txt
├── mahamandir/          Django project
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                Main app
│   ├── views.py
│   ├── urls.py
│   ├── models.py        ContactMessage, Subscriber
│   ├── data.py          Static content (events, services, gallery, etc.)
│   └── context_processors.py
├── templates/
│   ├── base.html
│   ├── includes/
│   │   ├── header.html
│   │   └── footer.html
│   └── core/
│       ├── home.html
│       ├── about.html
│       ├── mahamandir.html
│       ├── services.html
│       ├── gallery.html
│       ├── gallery_category.html
│       ├── events.html
│       ├── donate.html
│       └── contact.html
└── static/
    ├── css/style.css    Complete design system
    ├── js/main.js       Reveal, lightbox, nav, veil
    └── img/             All images stored locally
```

## Design philosophy

- **Serene entry**: a soft golden veil with a breathing Om greets visitors
  on first load, fading away after a contemplative pause.
- **Warm palette**: saffron, gold, pink sandstone, ivory — the colours of
  the Mahamandir itself.
- **Typography**: Cinzel (display), Cormorant Garamond (serif/italic), Inter (body).
- **Motion**: gentle fades and lifts — nothing jarring; reduced-motion is respected.
- **Ambient aura**: soft blurred orbs drift in the background.

## Pages

- **/** — Home: hero, invocation, about intro, stats, offerings, services, quote, events, testimonials, donate CTA
- **/about/** — Origin, founder, Vihangam Yoga philosophy
- **/mahamandir/** — The temple: architecture, features, photo mosaic, visit hours
- **/services/** — All eight seva initiatives in long form
- **/gallery/** — Category covers + featured mosaic
- **/gallery/<slug>/** — Per-category gallery with lightbox
- **/events/** — Timeline of upcoming events
- **/donate/** — 4 giving tiers + full donation form
- **/contact/** — Contact form (saves to DB) + map + details
- **/admin/** — Django admin for managing contact messages
```
```
