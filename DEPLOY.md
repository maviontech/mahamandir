# Deployment Guide — Swarved Mahamandir

This document covers the one-time setup and every-deploy steps, including
seeding the CMS admin.

---

## 1 · One-time server setup

```bash
# clone
git clone git@github.com:maviontech/mahamandir.git /opt/mahamandir
cd /opt/mahamandir

# virtualenv
python3 -m venv venv
source venv/bin/activate

# dependencies
pip install -r requirements.txt
pip install gunicorn          # production WSGI server
```

---

## 2 · Environment variables

Create `/opt/mahamandir/.env` (and load it via systemd / docker / your
platform). **Never commit this file.**

```env
# Django core
DJANGO_SECRET_KEY=<generate with: python -c 'import secrets;print(secrets.token_urlsafe(64))'>
DJANGO_DEBUG=false
DJANGO_ALLOWED_HOSTS=swarved-mahamandir.org,www.swarved-mahamandir.org

# Initial admin credentials (consumed by `create_admin` once)
SMM_ADMIN_USERNAME=owner
SMM_ADMIN_EMAIL=owner@swarved-mahamandir.org
SMM_ADMIN_PASSWORD=<long-random-passphrase>
```

Then update `mahamandir/settings.py` to read these (recommended before
production — currently dev defaults are hard-coded).

---

## 3 · Every-deploy commands

Run these four commands on every production deploy — they are idempotent
and safe to re-run:

```bash
# 1. collect static files
python manage.py collectstatic --noinput

# 2. apply DB migrations
python manage.py migrate --noinput

# 3. seed CMS with the baseline authentic content
#    (only adds/updates — never deletes your hand-edited content)
python manage.py seed_cms

# 4. ensure the admin user exists (reads SMM_ADMIN_* from env)
python manage.py create_admin
```

### Alternative: generate a random admin password on first install

```bash
python manage.py create_admin \
    --username owner \
    --email owner@swarved-mahamandir.org \
    --generate-password
```

This prints the password **once** — save it in your password manager
immediately. Subsequent runs will not change the password unless you
pass `--password` or `SMM_ADMIN_PASSWORD` again.

---

## 4 · Rotating the admin password

```bash
python manage.py create_admin \
    --username owner \
    --password 'new-strong-passphrase'
```

Or, while logged in, go to `/manage/settings/` → change through the
Django shell → or add a self-service password-change view (TODO).

---

## 5 · Seed command details (`seed_cms`)

`seed_cms` is idempotent by design:

| Content type        | Behaviour                                              |
| ------------------- | ------------------------------------------------------ |
| `SiteSetting`       | get-or-create singleton, preserves existing values     |
| `HeroSlide`         | `update_or_create(order=…)` — re-running overwrites    |
| `Event`             | `update_or_create(title=…)` — re-running overwrites    |
| `Service`           | `update_or_create(slug=…)` — re-running overwrites     |
| `GalleryCategory`   | `update_or_create(slug=…)` — re-running overwrites     |
| `GalleryImage`      | **deleted + recreated** each run (so edits from admin  |
|                     | panel would be lost; run only on fresh installs)       |
| `Testimonial`       | **deleted + recreated** — fresh installs only          |
| `Stat` / `Offering` | **deleted + recreated** — fresh installs only          |

**In production, run `seed_cms` only on first install.** Once staff
start editing content via the admin panel, rely on migrations for
schema changes and let the DB be the source of truth.

---

## 6 · Media (uploaded images) — persistent storage

Image uploads from the admin panel go to `MEDIA_ROOT` (default:
`media/` in the project folder). In production:

- Mount `media/` on a persistent volume (NOT inside the Docker image)
- Or point `MEDIA_ROOT` at S3-compatible storage (`django-storages`)
- Back it up nightly

---

## 7 · First-deploy checklist

- [ ] `.env` created with strong `DJANGO_SECRET_KEY`, `SMM_ADMIN_*`
- [ ] `DJANGO_DEBUG=false`
- [ ] `DJANGO_ALLOWED_HOSTS` set to the real domain
- [ ] `pip install -r requirements.txt`
- [ ] `python manage.py migrate`
- [ ] `python manage.py seed_cms`
- [ ] `python manage.py create_admin`
- [ ] `python manage.py collectstatic --noinput`
- [ ] Gunicorn + Nginx (or Waitress/Apache) configured
- [ ] HTTPS via Let's Encrypt
- [ ] Media folder on persistent volume
- [ ] DB backup cron in place
- [ ] Log in at `https://your-domain/manage/login/` and change password
