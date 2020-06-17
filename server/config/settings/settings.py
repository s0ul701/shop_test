from datetime import timedelta
import os

import dj_database_url

#########################################################################################
# Allowed hosts configs
#########################################################################################

ALLOWED_HOSTS = ['0.0.0.0', 'localhost']

#########################################################################################
# WSGI application and root URL configs
#########################################################################################

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

#########################################################################################
# Secret key and dubug configs
#########################################################################################

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

#########################################################################################
# Middleware configs
#########################################################################################

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#########################################################################################
# Templates configs
#########################################################################################

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#########################################################################################
# Database configs
#########################################################################################

DATABASES = {'default': dj_database_url.config()}

#########################################################################################
# Password validators configs
#########################################################################################

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

#########################################################################################
# Timezone and language configs
#########################################################################################

USE_I18N = True
USE_L10N = True
USE_TZ = True

#########################################################################################
# Base dir and static/media files configs
#########################################################################################

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(f'{BASE_DIR}/../', 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(f'{BASE_DIR}/../', "media")

#########################################################################################
# REST framework configs
#########################################################################################

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

#########################################################################################
# JWT-tokens configs
#########################################################################################

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(weeks=40),
    'REFRESH_TOKEN_LIFETIME': timedelta(weeks=80),
    'AUTH_HEADER_TYPES': ('Token',),
}
