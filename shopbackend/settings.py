from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-change-me")
DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "hfs-backend-production.up.railway.app",
]


# -------------------
# Applications
# -------------------
INSTALLED_APPS = [
    "corsheaders",

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    

    "products",
]

# -------------------
# Middleware
# -------------------
MIDDLEWARE = [
     "corsheaders.middleware.CorsMiddleware",

    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

   

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# -------------------
# URLs / WSGI
# -------------------
ROOT_URLCONF = "shopbackend.urls"
WSGI_APPLICATION = "shopbackend.wsgi.application"

# -------------------
# Templates
# -------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# -------------------
# Database (Railway compatible)
# -------------------
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# -------------------
# Static / Media
# -------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

if not DEBUG:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# If the app is behind a proxy (Railway), ensure Django knows requests are https
# so `request.build_absolute_uri()` and DRF absolute URLs use https.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True

# -------------------
# CORS
# -------------------
CORS_ALLOWED_ORIGINS = [
    "https://nbb-two.vercel.app",
]

FRONTEND_URL = os.getenv("FRONTEND_URL")
if FRONTEND_URL:
    CORS_ALLOWED_ORIGINS.append(FRONTEND_URL)

CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
    "https://*.vercel.app",
    "https://hfs-backend-production.up.railway.app",
]
# -------------------
# DRF
# -------------------
REST_FRAMEWORK = {}

# -------------------
# Other
# -------------------
LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "UTC"

USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_PASSWORD_VALIDATORS = []

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOW_CREDENTIALS = True