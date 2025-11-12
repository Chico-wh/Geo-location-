"""
Django settings for core project (Render-ready).

Configuração pronta para PostgreSQL + Redis + Channels + WhiteNoise.
"""

from pathlib import Path
import os
import dj_database_url

# BASE DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = os.environ.get("SECRET_KEY", "dummy-secret")
DEBUG = int(os.environ.get("DEBUG", 0))
ALLOWED_HOSTS = ["*"]  # Ajuste para produção

# APPLICATIONS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Terceiros
    'rest_framework',
    'rest_framework_simplejwt',
    'channels',
    'corsheaders',

    # Apps do projeto
    'transporte',
    'authentication',
]

# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # arquivos estáticos
    'corsheaders.middleware.CorsMiddleware',       # CORS
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# REST FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    )
}

# TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

CSRF_TRUSTED_ORIGINS = [
    "https://geo-location-0s3j.onrender.com",
]
# JWT SETTINGS
from datetime import timedelta

SIMPLE_JWT = {
     'ACCESS_TOKEN_LIFETIME': timedelta(hours=3650),   # curto, 1 hora
    'REFRESH_TOKEN_LIFETIME': timedelta(days=3650), # longo, 30 dias
    'ROTATE_REFRESH_TOKENS': False,                # gera novo refresh token a cada uso
    'BLACKLIST_AFTER_ROTATION': False,
}
# URLS
ROOT_URLCONF = 'core.urls'

# WSGI / ASGI
WSGI_APPLICATION = 'core.wsgi.application'
ASGI_APPLICATION = 'core.asgi.application'

# DATABASE (PostgreSQL via Render)
DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL")
    )
}

# CACHE + CHANNELS (Redis)
REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379")
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {"hosts": [REDIS_URL]},
    },
}
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
    }
}

# AUTH PASSWORD VALIDATORS
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# INTERNATIONALIZATION
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# STATIC FILES
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# CORS
CORS_ALLOW_ALL_ORIGINS = True

# DEFAULT PK FIELD
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
