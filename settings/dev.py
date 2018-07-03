from .base import *
# try:
from .settings_wagtail import *

# except Exception as ee:
#     pass

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

LOCAL_SETTINGS_LOADED = False

# try to put it at the beginning of the installed apps
INSTALLED_APPS = ['rest_framework'] + INSTALLED_APPS
INSTALLED_APPS = MyWagtailConfig.INSTALLED_APPS + INSTALLED_APPS
INSTALLED_APPS = ['wagtailapp'] + INSTALLED_APPS
INSTALLED_APPS = ['keystone_auth'] + INSTALLED_APPS
INSTALLED_APPS = ['emailing'] + INSTALLED_APPS
INSTALLED_APPS = ['article'] + INSTALLED_APPS

# print(INSTALLED_APPS)
MY_AUTH = False

# try to put it at the end of the middleware
MIDDLEWARE.extend(MyWagtailConfig.MIDDLEWARE)
if MY_AUTH:
    MIDDLEWARE.extend(['keystone_auth.keystone_middleware.keystone_middleware'])

try:
    STATIC_ROOT
except NameError:
    raise Exception("static root is necessary to be configured for wagtail")

try:
    MEDIA_ROOT
except NameError:
    raise Exception("media root is necessary to be configured for wagtail")

# STATICFILES_DIRS = MyWagtailConfig.STATICFILES_DIRS(BASE_DIR=BASE_DIR) + STATICFILES_DIRS
# print(STATICFILES_DIRS)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # these permissions are followed one layer at a time as you see the order here
        'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],

    "DEFAULT_AUTHENTICATION_CLASSES": [
        'keystone_auth.keystone_rest_auth.KeystoneRestAuthentication',
        "rest_framework.authentication.TokenAuthentication",  # http header is required here, HTTP_AUTHORIZATION
        "rest_framework.authentication.SessionAuthentication",  # default one, useful to devs
    ]
}

# Once a user has authenticated, Django stores which backend was used to authenticate the user in
# the user’s session, and re-uses the same backend for the duration of that session whenever access
# to the currently authenticated user is needed. This effectively means that authentication sources
# are cached on a per-session basis, so if you change AUTHENTICATION_BACKENDS, you’ll need to clear
# out session data if you need to force users to re-authenticate using different methods. A simple
# way to do that is simply to execute Session.objects.all().delete().


if MY_AUTH:
    AUTHENTICATION_BACKENDS = [
        'keystone_auth.keystone_auth_backend.KeystoneAuthBackend',
    ]  # + AUTHENTICATION_BACKENDS

KEYSTONE_URL = 'http://localhost:9001'
KEYSTONE_LOGIN = KEYSTONE_URL + "/api/api-token-auth/"
KEYSTONE_AUTH_TOKEN = KEYSTONE_URL + "/api/tokens/"
KEYSTONE_API_SYSTEM_TOKEN = "	28e2ddd97954f56bd47872e7433851bcb94507b7"
KEYSTONE_TOKEN_KEY = "keystone_token"

# LOGIN_URL_PATH_EXEMPT_FROM_AUTH = '/tasks_mngr/conn' #avoid hardcoded urls
LOGIN_URL_PATH_EXEMPT_FROM_AUTH = 'tasks_manager:conn'
WAGTAIL_FRONTEND_LOGIN_URL = '/tasks_mngr/conn'

# LOGIN_REDIRECT_URL = 'tasks_manager:conn'

# https://keen.io/invite/03d6b4105dba11e8908f0242ac110003 <-- admin access
# This is your actual Project ID and Write Key
KEEN_PROJECT_ID = "5b040ac3c9e77c000139857b"
KEEN_WRITE_KEY = "19BD95AED53AFB8FB11DC4621B42DCD7C81A60EDB9AF37FF2A2F24A315DD4F861C4A4EA92C4C8D8C5CEB18F49C30FD64C04532CB6862391CB8B6B4D90E6DC3E6C64D4AD987194ABC8427EC3D8A036EAD3ABA7F7A84E3A4AD5624E7C764213BEB"

TEMPLATES[0]['OPTIONS']['libraries'] = {
    'demo_tags': 'wagtailapp.templatetags.demo_tags'
}

try:
    from .local_settings import *
except:
    pass