from .base import *

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

LOCAL_SETTINGS_LOADED = False

INSTALLED_APPS.extend([
    'rest_framework',
])

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
