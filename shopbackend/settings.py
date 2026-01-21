from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-change-me")
DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    # Добавь сюда свой боевой домен
    # "your-backend-domain.com",
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

    "cloudinary_storage",
    "cloudinary",

    "products",
]

# -------------------
# Middleware
# -------------------
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",

    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
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
# Database
# -------------------
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# -------------------

# -------------------
# Static
# -------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# -------------------
# Cloudinary (MEDIA)
# -------------------
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
MEDIA_URL = "/media/"
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.getenv("CLOUDINARY_CLOUD_NAME", "your_cloud_name"),
    "API_KEY": os.getenv("CLOUDINARY_API_KEY", "your_api_key"),
    "API_SECRET": os.getenv("CLOUDINARY_API_SECRET", "your_api_secret"),
}

# -------------------
# CORS / CSRF
# -------------------
"""
CORS-настройки для production:
- Разрешены только ваши рабочие домены
"""

# -------------------
# CORS / CSRF
# -------------------
CORS_ALLOW_ALL_ORIGINS = True  # Для продакшна лучше False и явно указать домены ниже
CORS_ALLOWED_ORIGINS = [
    # "https://your-frontend-domain.com",
]
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = [
    # "https://your-frontend-domain.com",
]

# -------------------
# Other
# -------------------
LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_PASSWORD_VALIDATORS = []



# ======================
# Cloudinary storage
# ======================



