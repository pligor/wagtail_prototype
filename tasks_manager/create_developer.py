from django.shortcuts import render
from django.http import HttpResponse
from .models import Supervisor, Developer


def create_developer(request):
    error = False

    if request.method == "POST":
        if all([key in request.POST.keys() for key in ['login', 'name', 'password', 'supervisor']]):
            supervisor = Supervisor.objects.get(id=request.POST.get('supervisor', ''))
            new_dev = Developer(
                name=request.POST.get('name', ''),
                login=request.POST.get('login', ''),
                password=request.POST.get('password', ''),
                its_supervisor=supervisor
            )

            new_dev.save()

            return HttpResponse("developer was added")
        else:
            return HttpResponse("error occured: {}".format(", ".join(request.POST.keys())))

    elif request.method == "GET":
        supervisors = Supervisor.objects.all()
        return render(request, 'tasks_manager/create_developer.html', context={
            'supervisors': supervisors
        })

    else:
        raise Exception("wrong method, only GET or POST are allowed")
