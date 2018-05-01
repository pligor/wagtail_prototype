from .base import *

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

LOCAL_SETTINGS_LOADED = False

try:
    from .local_settings import *
except:
    pass
