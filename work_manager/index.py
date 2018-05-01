from django.http import HttpResponse

def home(request):
    return HttpResponse("okey dokey, hello people!")