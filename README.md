# Safari Travels — Django Website

Full-stack Tanzania tourism website: Django backend, PostgreSQL (Supabase), deployed on Render.

## Stack
- Django 5.1, WhiteNoise for static files, gunicorn for production serving
- Postgres via Supabase (falls back to SQLite locally if `DATABASE_URL` is unset)
- All secrets read from environment variables — **nothing is hardcoded in `settings.py`**

## Local setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env      # then fill in real values
python manage.py migrate
python manage.py seed_data      # loads real Safari Travels content (packages, destinations, day trips)
python manage.py createsuperuser
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` for the site and `/admin/` for the content dashboard.

## Content model (edit everything from /admin/)
- **Destinations** — the 9 popular destinations (Serengeti, Kilimanjaro, Zanzibar, etc.)
- **Packages** — multi-day tours, each with an editable day-by-day itinerary (shows as the journey timeline on the package page)
- **Day Trips** — single-day excursions
- **Testimonials** — guest reviews shown on the homepage
- **Contact Messages** — every submission from the contact form lands here, mark `handled` once followed up

Images: either paste an image URL into the `image` field, or upload a file directly via `image_upload` in admin — the site prefers the uploaded file if both are set.

## Supabase setup
1. Create a project at supabase.com
2. Project Settings → Database → Connection string (URI) → copy the **Session pooler** URI (works better with Render's free tier than the direct connection)
3. Put that URI in `DATABASE_URL` in your `.env` (local) and in Render's environment variables (production)

## Deploying to Render
1. Push this project to a GitHub repo
2. On Render: New → Web Service → connect the repo (it will detect `render.yaml`)
3. Set these environment variables in the Render dashboard:
   - `SECRET_KEY` — Render can auto-generate this
   - `DATABASE_URL` — your Supabase connection string
   - `DEBUG` — `False`
   - `ALLOWED_HOSTS` — `.onrender.com` (or your custom domain once attached)
4. Deploy. `build.sh` runs migrations and `collectstatic` automatically on every deploy.
5. After first deploy, run once from the Render shell: `python manage.py seed_data` and `python manage.py createsuperuser`

## Security notes
- `.env` is git-ignored — never commit real credentials
- Rotate the Supabase database password if it was ever shared in plaintext anywhere (chat, docs, etc.)
- `DEBUG=False` and HTTPS redirect are enforced automatically outside local dev

## Company info already wired in
Company name, phone numbers, WhatsApp link, email, address and social links are all set in `safaritravels/settings.py` (`SITE_*` variables) and pulled into every template via a context processor — update them in one place if anything changes.
