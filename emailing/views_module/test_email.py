from django.http import HttpResponse

def test_email(request):
    return HttpResponse('testing email here')