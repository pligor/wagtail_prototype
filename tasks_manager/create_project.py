from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project

from django import forms

class Form_project_create(forms.Form):
    """this generates forms similar to models style"""

    title = forms.CharField(label='Title', max_length=30)
    description = forms.CharField(widget=forms.Textarea(attrs={  # widget
        'rows': 5,
        'cols': 100,
    }))

    client_name = forms.CharField(label='Client', max_length=50, initial="Mr Big (default value kai kala)")


from django.contrib.auth.decorators import login_required


#need to check the token with keystone
# @login_required()
def create_project(request):
    from django.conf import settings
    print('Are the local settings loaded? {}'.format(settings.LOCAL_SETTINGS_LOADED))

    if request.method == 'POST':
        form = Form_project_create(request.POST)

        if form.is_valid():
            Project(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                client_name=form.cleaned_data['client_name'],
            ).save()

            return HttpResponse("Project was added")
        else:
            return render(request, 'tasks_manager/create_project.html', context={
                'form': form,  # this is to display the errors appropriately
            })

    else:
        form = Form_project_create(initial={
            'title': 'Zwara'
        })

        return render(request, 'tasks_manager/create_project.html', context={
            'form': form
        })
