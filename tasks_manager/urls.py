"""work_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import page, create_project, list_projects, get_only_one_record, project_detail
from .views import update_project, update_multi_projects, del_project, project_task_rel, raw_query
from .create_developer import create_developer
from .create_dev_django_forms import create_developer_django_forms
from .create_supervisor import create_supervisor
from .create_project import create_project
from .create_supervisor_and_user import create_supervisor_and_user
from .connection import connection

from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Project, Task
from django.urls import reverse_lazy
from .my_update_view import MyUpdateView
from .update_view_custom import UpdateViewCustom
from .views import logout

app_name = 'tasks_manager' #you need to define the namespace also here
urlpatterns = [
    url(r'^$', page, name="home"),
    url(r'^conn$', connection, name="conn"),
    url(r'^logout$', logout, name="logout"),
    url(r'^create_project', create_project, name="create_project"),
    url(r'^list_projects$', list_projects, name="list_projects"),
    url(r'^get_only_one_record$', get_only_one_record, name="get_only_one_record"),

    # exoume integer gia parametro
    url(r'^project-detail-(?P<param>\d+)$', project_detail, name="project_detail"),
    url(r'^update_project/(?P<my_pk>\d+)$', update_project, name="update_project"),

    url(r'update_multi_projects$', update_multi_projects, name='update_multi_projects'),
    url(r'del_project$', del_project, name='del_project'),
    url(r'project_task_rel$', project_task_rel, name='project_task_rel'),
    url(r'raw_query$', raw_query, name='raw_query'),

    url(r'^create_developer$', create_developer, name="create_developer"),
    url(r'^create_developer_django_forms$', create_developer_django_forms, name="create_developer_django_forms"),
    url(r'^create_supervisor$', create_supervisor, name="create_supervisor"),
    url(r'^create_supervisor_and_user$', create_supervisor_and_user, name="create_supervisor_and_user"),

    url(r'^create_project$', create_project, name="create_project"),
    url(r'^create_project_cbv$',
        CreateView.as_view(model=Project,  # CLASS BASED, AUTOMAGICALLY CREATE A VIEW
                           template_name="tasks_manager/create_project_cbv.html",
                           success_url=reverse_lazy('home'),
                           fields='__all__',
                           # https://itbinnacle.wordpress.com/2015/12/27/django-using-modelformmixin-base-class-of-createuserview-without-the-fields-attribute-is-prohibited/
                           ),
        name="create_project_cbv"),

    url(r'^project/list$', ListView.as_view(
        model=Project,
        template_name="tasks_manager/list_project.html",
    ), name="project_listing"),

    # TODO EXTENDING CBVs is an ANTIPATTERN

    # NOTE THAT WE ARE FORCED TO USE the PARAMETER to be "pk" otherwise the DetailView is not
    # going to automagically work
    url(r'^task_detail_(?P<pk>\d+)$', DetailView.as_view(
        model=Task,
        template_name='tasks_manager/task_detail.html',
    ), name='detail_task'),

    # NOTE THAT WE ARE FORCED TO USE the PARAMETER to be "pk" otherwise the UpdateView is not
    # going to automagically work
    # Extending UpdateView just for fun to show the alternative and slightly more advanced
    # url(r'^update_task_(?P<pk>\d+)$', UpdateView.as_view(
    #     model=Task,
    #     template_name='tasks_manager/update_task.html',
    #     success_url=reverse_lazy('home'),  # no arguments args=[]
    #     fields='__all__',
    # ), name='update_task'),
    url(r'^update_task_(?P<pk>\d+)$', MyUpdateView.as_view(), name='update_task'),

    # NOTE THAT WE ARE FORCED TO USE the PARAMETER to be "pk" otherwise the DeleteView is not
    # going to automagically work
    url(r'^delete_task_(?P<pk>\d+)$', DeleteView.as_view(
        model=Task,
        template_name='tasks_manager/delete_task.html',
        success_url=reverse_lazy('home'),  # no arguments args=[]
    ), name='delete_task'),

    url(r'^project_update_(?P<pk>\d+)$', UpdateViewCustom.as_view(
        model=Project,
        url_name='project_update',
        success_url='project_update',
        fields='__all__',
    ), name='project_update'),
]

"""
 [0-9] is equivalent to [0123456789]
•
 [a-z] matches all the letters, [abcdefghijklmnopqrstuvwxyz]
•
 [A-Z] matches all uppercase letters
•
 [a-zA-Z] matches all the letters
The following are the shortcuts:
•
 \d is equivalent to [0-9]
•
 \w is equivalent to [a-zA-Z0-9_]
•
 [0-9] is equivalent to [0123456789]
"""
