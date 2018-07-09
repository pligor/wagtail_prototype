"""
Django settings for work_manager project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
# DJANGO v1.11
from __future__ import unicode_literals
import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g=^3d%w6hgggjxmy*x7v1leil8uu@p3g6&b)8h)^7a5p8^gmlb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    # 'south', see page 43/62 of the pdf file
    'tasks_manager',  # necessary to define our apps here

    'django.contrib.admin',  # this is to enable the administrator

    'django.contrib.auth',  # this is to enable or disable the authentication module

    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Middleware are classes and methods, including the methods that are performed
# during the request process.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # include this to all the forms: {% csrf_token %}
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# here is where we start checking for urls
ROOT_URLCONF = 'work_manager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'work_manager.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-uk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_CHARSET = 'utf-8'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# 1. collect from here
STATICFILES_DIRS = [
    # this is to include our own custom folder to the static directories
    os.path.join(BASE_DIR, "tasks_manager", "static")
]

# 2. collect to this folder
# this is to express the destination for the command: python3 manage.py collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# 3. display with this link
STATIC_URL = '/static/'

# print('STATICFILES_DIRS')
# print(STATICFILES_DIRS)

LOGIN_URL = "tasks_manager:conn"  # this is the name of the login page

# A module is meant to be under the Python path if you can run Python and import that module.
# One of the ways to put a module under the Python path is to modify the sys.path variable
# before importing a module that is in an unusual location. The value of sys.path is a list of
# directories starting with an empty string for the current directory, followed by the directories in
# the virtual environment, and finally the globally shared directories of the Python installation.
EXTERNAL_LIBS_PATH = os.path.join(BASE_DIR, "externals", "libs")
EXTERNAL_APPS_PATH = os.path.join(BASE_DIR, "externals", "apps")
sys.path = ["", EXTERNAL_APPS_PATH, EXTERNAL_LIBS_PATH] + sys.path
# Note that we also add an empty string as the first path to search,
# which means that the current directory of any module
# should always be checked first before checking other Python paths.

MEDIA_ROOT = os.path.join(BASE_DIR, "work_manager", "media")
MEDIA_URL = '/media/'

LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]

FILE_UPLOAD_TEMP_DIR = os.path.join(BASE_DIR, "tmp")

AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']

#Use environment variable: export DJANGO_SETTINGS_MODULE=....