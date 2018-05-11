from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task, Developer
from django.conf import settings


def raw_query(request):
    # notice that the convention for naming the tables is: appname_tablename
    projects = list(Project.objects.raw("SELECT * FROM tasks_manager_project;"))
    return render(request, 'tasks_manager/projects.html', context={
        'projects': projects
    })


def project_task_rel(request):
    project = Project.objects.filter(title__contains="Project")[0]
    tasks = Task.objects.filter(project=project)  # THE OPPOSITE OF filter is "exclude", page 64/84 pdf
    return HttpResponse("project {} has {:d} tasks".format(project, len(tasks)))


def del_project(request):
    project = Project.objects.all()[0]
    title_lost_project = project.title
    project.delete()
    return HttpResponse("we just lost the project with title: {}".format(title_lost_project))


def update_multi_projects(request):
    projects = Project.objects.filter(client_name="parents")
    projects.update(client_name="goneis")
    return HttpResponse("check admin to see if projects have been updated")


def update_project(request, my_pk):
    project = Project.objects.get(id=my_pk)
    project.title = "Grant " + project.title
    project.save()
    return HttpResponse("This is new title of project with id {}: {}".format(project.id, project))


def project_detail(request, param):
    project = Project.objects.get(id=param)
    return HttpResponse("This is the project of id {}: {}".format(project.id, project))


def get_only_one_record(request):
    # project = Project.objects.get(id=3)
    project = Project.objects.filter(client_name='parents').order_by("-id")[:1].get()
    return HttpResponse("This is the project of id {}: {}".format(project.id, project))


def list_projects(request):
    # all_projects = Project.objects.all()
    from django.db import models

    # projects = Project.objects.filter(client_name='goneis').filter(title__contains='degree')
    projects = Project.objects.filter(models.Q(client_name='goneis') | models.Q(client_name='myself'))
    # The __contains means that we apply the contains on the title
    return render(request, 'tasks_manager/projects.html', context={
        'projects': projects
    })


def create_project(request):
    new_project = Project(title="Tasks Manager with Django",
                          description="Django project to getting start with Django easily",
                          client_name='myself')
    new_project.save()

    # create first task and link with project
    new_task = Task(
        title="This is my first task",
        description="do a git init",
        importance=1,
        project=new_project,
        app_user=Developer.objects.filter(name='Developer')[:1].get()
    )

    return HttpResponse("we have created a new Project with id {} and task {}".format(new_project.id,
                                                                                      new_task.title))


# Create your views here.
def page(request):
    my_var = "<THIS> Is my string"
    capitals = ['Paris', 'London', 'Washington']
    return render(request, 'tasks_manager/index.html', {
        "str_var": my_var,
        "years": 55,
        "capitals": capitals,
        "dog_no": 1,
        "my_paragraphs": """Eimai edw
        kai esy ekei
        kai oi alloi parapera
        den mporo na to pistepso
        oti kanw tis pio pikres skepseis"""
    })


def logout(request):
    from django.contrib.auth import logout
    logout(request)
    response = HttpResponse("You are logged out!")
    response.set_cookie(key=settings.KEYSTONE_TOKEN_KEY, value=None)
    return response


def show_cookie(request):
    return HttpResponse("This is the cookie: {}".format(
        request.COOKIES.get(settings.KEYSTONE_TOKEN_KEY, "(empty cookie)")
    ))
