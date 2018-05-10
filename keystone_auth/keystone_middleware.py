from django.conf import settings
from .keystone_utils import get_user_with_token, fill_user
from django.shortcuts import redirect
from .models import KeystoneUser

def keystone_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        def _go_to_login(path):
            return redirect(to=settings.LOGIN_URL_PATH_EXEMPT_FROM_AUTH + "?next=" + path)

        # Code to be executed for each request before
        # the view (and later middleware) are called.
        path_with_slash = request.path if request.path[-1] == "/" else request.path + "/"

        if path_with_slash == settings.LOGIN_URL_PATH_EXEMPT_FROM_AUTH:
            print("this is the login path")
            pass
        else:
            #tasks_mngr/create_project
            print(path_with_slash)
            if path_with_slash == "/tasks_mngr/create_project/": #TODO remove this "if" later
                token = request.COOKIES.get(settings.KEYSTONE_TOKEN_KEY)
                #cookie_value = None
                if token is None:
                    #cookie is not available, try to login
                    return _go_to_login(path_with_slash)
                else:
                    print("try to use the cookie to login via keystone: {}".format(
                        token if token else "(not defined yet)"))

                    user = get_user_with_token(token)
                    if user is None:
                        return _go_to_login(path_with_slash)

                    assert isinstance(user, KeystoneUser)
                    user.token = token
                    user_filled = fill_user(user=user)

                    request.user = user_filled
                    #
                    # print(user_filled)
                    # print(user_filled.roles)
                    # print("USER")
                    # print(request.user)

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware