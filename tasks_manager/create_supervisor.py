from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Supervisor, Developer
from django.urls import reverse
from django import forms


# TODO : MODEL FORMS ARE AN ANTIPATTERN BECAUSE OF RESTRICTED FLEXIBILITY

class Form_supervisor(forms.ModelForm):
    """YES we really have a class and we are defining properties in this class in order to define"""

    class Meta:
        model = Supervisor
        exclude = ['date_created', 'last_connection']


def create_supervisor(request):
    if request.method == 'POST':
        form = Form_supervisor(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect(to='home')  # just get us to home
        else:  # this means that we have errors to render
            return render(request, 'tasks_manager/create_supervisor.html', context={
                'form': form
            })

    elif request.method == 'GET':
        form = Form_supervisor()

        return render(request, 'tasks_manager/create_supervisor.html', context={
            'form': form
        })
    else:
        raise Exception("method is not expected {}".format(request.method))
