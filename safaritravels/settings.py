"""
Django settings for safaritravels project.
Configured for deployment on Render.com with Supabase Postgres.
ALL secrets/credentials are read from environment variables — never hardcode
SECRET_KEY or database credentials here. Create a `.env` file locally
(see `.env.example`) and set the same variables in the Render dashboard.
"""

from pathlib import Path
from decouple import config, Csv
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# --- Core security settings -------------------------------------------------
SECRET_KEY = 'change-this-to-a-long-random-string'
DEBUG = True
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="127.0.0.1,localhost", cast=Csv())

RENDER_EXTERNAL_HOSTNAME = config("RENDER_EXTERNAL_HOSTNAME", default="")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

CSRF_TRUSTED_ORIGINS = config(
    "CSRF_TRUSTED_ORIGINS",
    default="",
    cast=Csv()
)
if RENDER_EXTERNAL_HOSTNAME:
    CSRF_TRUSTED_ORIGINS.append(f"https://{RENDER_EXTERNAL_HOSTNAME}")

# --- Applications ------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "tours",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "safaritravels.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "tours.context_processors.site_settings",
            ],
        },
    },
]

WSGI_APPLICATION = "safaritravels.wsgi.application"

# --- Database: Supabase Postgres via DATABASE_URL env var -------------------
# In Supabase: Project Settings > Database > Connection string (URI, use the
# "Session pooler" connection for Render). Put it in DATABASE_URL.
# _database_url = config("DATABASE_URL", default="")
# if _database_url:
#     DATABASES = {
#         "default": dj_database_url.parse(
#             _database_url,
#             conn_max_age=600,
#             ssl_require=config("DB_SSL_REQUIRE", default=True, cast=bool),
#         )
#     }
# else:
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.sqlite3",
#             "NAME": BASE_DIR / "db.sqlite3",
#         }
#     }



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres', 
        'USER': 'postgres.kigodcvtsssckcsgnmpl',  
        'PASSWORD': 'NyumbaChap@123', 
        'HOST': 'aws-0-eu-central-1.pooler.supabase.com',  
        'PORT': '5432',  
    }
}


# --- Password validation -----------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --- Internationalization -----------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Africa/Dar_es_Salaam"
USE_I18N = True
USE_TZ = True

# --- Static & media files ------------------------------------------------------
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"},
}

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --- Security hardening for production -----------------------------------------
if not DEBUG:
    SECURE_SSL_REDIRECT = config("SECURE_SSL_REDIRECT", default=True, cast=bool)
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# --- Site-wide company info (used across templates) ----------------------------
SITE_NAME = "Safari Travels"
SITE_PHONE_PRIMARY = "+255 760 608 544"
SITE_PHONE_SECONDARY = "+255 616 214 327"
SITE_WHATSAPP = "255760608544"
SITE_EMAIL = "info@safaritravels.co.tz"
SITE_LOCATION = "Bondeni Street, Arusha, Tanzania"
SITE_INSTAGRAM = "https://instagram.com/safaritravels"
SITE_FACEBOOK = "https://facebook.com/safaritravels"
SITE_THREADS = "https://threads.net/@safaritravels"
