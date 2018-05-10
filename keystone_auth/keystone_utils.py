from django.conf import settings
import requests
from .models import KeystoneUser

def get_user_with_token(token):
    response = requests.get(settings.KEYSTONE_AUTH_TOKEN, headers={
        'Authorization': "token {}".format(token)
    })

    if response.status_code > 201:
        return None

    user_details = response.json()['results'][0]
    user = KeystoneUser()
    user.keystone_token = user_details['key']
    user.id = user_details['userid']
    user.uuid = user_details['uuid']
    user.username = user_details['username']
    return user

def fill_user(user):
    try:
        headers = {
            'Authorization': 'token {}'.format(settings.KEYSTONE_API_SYSTEM_TOKEN)
        }
        # TODO Why this call has the api system token? and then filters by user id while we could just
        # pass user's token and be fine
        params = {
            'userid': user.id
        }

        url = settings.KEYSTONE_URL + '/api/roles/'

        resp = requests.get(url, headers=headers, params=params)

        resp_data = resp.json()
        roles = resp_data.get('results', [])
        if len(roles) > 0:
            user.first_name = roles[0]['user']['first_name']
            user.last_name = roles[0]['user']['last_name']
    except Exception as ee:
        # logger.error('%s %s %s', __file__, e.__class__, e)
        roles = []

    user.roles = roles

    return user