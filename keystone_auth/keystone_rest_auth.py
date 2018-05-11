from rest_framework.authentication import BaseAuthentication
from django.conf import settings
from .keystone_utils import get_user_with_token, fill_user
from .models import KeystoneUser


class KeystoneRestAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get(settings.KEYSTONE_TOKEN_KEY)
        if not token:
            return None

        user = get_user_with_token(token=token)
        if user is None:
            return None

        assert isinstance(user, KeystoneUser)
        user.keystone_token = token
        user_filled = fill_user(user=user)

        return [user_filled, None]
