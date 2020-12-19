"""
Django settings for Groundtek project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

LOGIN_REDIRECT_URL = reverse_lazy('visits:dashboard')

LOGIN_URL = reverse_lazy('visits:login')
LOGOUT_URL = reverse_lazy('visits:logout')


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ugeopolimer@gmail.com'
EMAIL_HOST_PASSWORD = '21023040'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = 'Groundek'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'au4mn%^3j3h$hil%vs+r-6_k7r9xu&ma0ql3*v0m@jl0kx6^ui'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','groundtek.tech','e-novitskiy.site','uretekbelarus.by']

# Application definition

SITE_ID=1

INSTALLED_APPS = [
    'visits',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'phonenumber_field',
    'django.contrib.sites',
    'standart',
    'rosetta',
    'parler',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Groundtek.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'material-kit-master/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'visits.context_processors.visit',
                'visits.context_processors.menu',
            ],
        },
    },
]

WSGI_APPLICATION = 'Groundtek.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/


PARLER_LANGUAGES = {
    SITE_ID: (
        {'code': 'en'},
        {'code': 'pl'},
        {'code': 'ru'},
    ),
    'default': {
        'fallback': 'en',
        'hide_untranslated': False,
    }
}


LANGUAGES = (
    ('en', _('English')),
    ('ru', _('Russian')),
    ('pl', _('Polish')),

)


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/material-kit-master/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'material-kit-master'),)
MEDIA_URL = ''
MEDIA_ROOT = os.path.join(BASE_DIR, '')

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)


VISITS_SESSION_ID = 'visits'