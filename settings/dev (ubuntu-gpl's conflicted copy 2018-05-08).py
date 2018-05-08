from .base import *
# try:
from .settings_wagtail import *

# except Exception as ee:
#     pass

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

LOCAL_SETTINGS_LOADED = False

INSTALLED_APPS = [
                     'rest_framework',
                 ] + INSTALLED_APPS
INSTALLED_APPS = MyWagtailConfig.INSTALLED_APPS + INSTALLED_APPS
INSTALLED_APPS = ['wagtailapp'] + INSTALLED_APPS

MIDDLEWARE.extend(MyWagtailConfig.MIDDLEWARE)

try:
    STATIC_ROOT
except NameError:
    raise Exception("static root is necessary to be configured for wagtail")

try:
    MEDIA_ROOT
except NameError:
    raise Exception("media root is necessary to be configured for wagtail")

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # these permissions are followed one layer at a time as you see the order here
        'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],

    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",  # http header is required here, HTTP_AUTHORIZATION
        "rest_framework.authentication.SessionAuthentication",  # default one, useful to devs
    ]
}

try:
    from .local_settings import *
except:
    pass
