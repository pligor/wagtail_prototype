from django.http import HttpResponse
from django.conf import settings
import json

def home(request):
    return HttpResponse("These are the installed apps: {}".format(
        json.dumps(settings.INSTALLED_APPS, indent=True)
    ))
