"""
Django settings for fruitfultreecountmanagement project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
import cv2

print(cv2.COLOR_RGB2BGR)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR: Path = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "your_secret_key_here"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost"]
SITE_ID = 1


# Application definition

INSTALLED_APPS: list[str] = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    # Extensions - installed with pip3 / requirements.txt
    "django_extensions",
    "crispy_forms",
    "leaflet",
    "django_filters",
    "django_property_filter",

    # 3rd part apps
    "rest_framework",
    "rest_framework_gis",
    # local apps
    "home.apps.HomeConfig",
    "farms.apps.FarmsConfig",
    "changedet.apps.ChangedetConfig",
    # these are required for user authentication
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "django.contrib.sites",
    "allauth.socialaccount.providers.google",
]

MIDDLEWARE: list[str] = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "fruitfultreecountmanagement.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
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

WSGI_APPLICATION = "fruitfultreecountmanagement.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# postgre(postGis) database
# you should connect your database here
DATABASES: dict[str, dict[str, str]] = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "fruitful_tree_count_management",
        "USER": "your database user name",
        "PASSWORD": "your database password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS: list[dict[str, str]] = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

REST_FRAMEWORK: dict[str, list[str]] = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly"
    ],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

STATICFILES_DIRS: tuple[str] = (os.path.join(BASE_DIR, "static"),)


MEDIA_URL = "media/"

MEDIA_ROOT: str = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Gdal Library
# GDAL_LIBRARY_PATH = r'C://OSGeo4W/bin/gdal306.dll'
GDAL_LIBRARY_PATH = r"C:\OSGeo4W\bin\gdal306.dll"
GEOS_LIBRARY_PATH = r"C:\OSGeo4W\bin\geos_c.dll"


# leaflet-django
LEAFLET_CONFIG = {
    "SRID": 3857,  # See http://spatialreference.org
    "SPATIAL_EXTENT": (-180.0, -90.0, 180.0, 90.0),
    "DEFAULT_CENTER": (34.988515, 37.980672),
    "DEFAULT_ZOOM": 6,
    "MIN_ZOOM": 3,
    "MAX_ZOOM": 30,
    "DEFAULT_PRECISION": 6,
    "ATTRIBUTION_PREFIX": "Powered by django-leaflet",
    "TILES": [
        (
            "Hybrid",
            "http://{s}.google.com/vt?lyrs=s,h&x={x}&y={y}&z={z}",
            {
                "attribution": "&copy; google Hybrid",
                "subdomains": ["mt0", "mt1", "mt2", "mt3"],
            },
        ),
    ],
    "PLUGINS": {
        "draw": {
            "css": "leaflet/draw/leaflet.draw.css",
            "js": [
                "leaflet/draw/leaflet.draw.js",
                "https://unpkg.com/leaflet.featuregroup.subgroup@1.0.2/dist/leaflet.featuregroup.subgroup.js",
                "https://cdn.rawgit.com/hayeswise/Leaflet.PointInPolygon/v1.0.0/wise-leaflet-pip.js",
            ],
            "auto-include": True,
        },
    }
    # "MINIMAP": True,
    # 'RESET_VIEW': False,
    # 'FORCE_IMAGE_PATH': True,
}

# Google maps API key
GOOGLE_MAPS_API_KEY = "paste Google map API key here"

# this is required for user authentication
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]

# Google Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': 'Client id should be here',
            'secret': 'secret should be here',
            'key': ''
        },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
