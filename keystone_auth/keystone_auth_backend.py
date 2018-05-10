import requests
from django.conf import settings
from .models import KeystoneUser
from .keystone_utils import get_user_with_token, fill_user

class KeystoneAuthBackend(object):
    def authenticate(self, request, username=None, password=None):
        print("inside authenticate")
        print(username, password)

        #token, uuid, userid
        result = self._logging_in(username=username, password=password)

        if result is None:
            return None

        token = result['token']
        user = get_user_with_token(token)
        if user is None:
            raise Exception("server error")

        assert isinstance(user, KeystoneUser)

        user.token = token

        user_filled = fill_user(user=user)

        print(user_filled)
        print(user_filled.roles)

        return user

    def _logging_in(self, username, password):
        try:
            response = requests.post(settings.KEYSTONE_LOGIN, json={
                "username": username,
                "password": password,
            }, headers={
                "Content-Type": "application/json"
            })
        except Exception as ee:
            print("exception")
            return None

        if response.status_code == 200:
            return response.json()
        else:
            print("wrong response code")
            return None


    def authenticate_wrong_DEPRECATED(self, request, username=None, password=None):
        print("inside authenticate")
        print(username, password)

        token = request.COOKIES.get(settings.KEYSTONE_TOKEN_KEY)

        if token is None:
            print("FIRST USER IS NONE")
            result = self._logging_in(username=username, password=password)

            if result is None:
                return None
            else:
                token = result["token"]
        else:
            print("TOKEN IS HERE")

        user = self._get_user_with_token(token)
        assert isinstance(user, KeystoneUser)

        user.token = token

        if user is None:
            raise Exception("server error")

        assert user is not None
        user_filled = self._fill_user(user=user)

        print(user_filled)
        print(user_filled.roles)

        return user
