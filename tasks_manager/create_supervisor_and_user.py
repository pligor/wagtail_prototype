from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Supervisor
from django.urls import reverse
from django import forms
from django.contrib.auth.models import User


class Form_supervisor(forms.Form):
    name = forms.CharField(label="name", max_length=30)
    login = forms.CharField(label="Login")
    email = forms.EmailField(label="Email")
    specialization = forms.CharField(label="Specialization")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_bis = forms.CharField(label="Password (again)", widget=forms.PasswordInput)

    def clean(self):
        """Extending clean method"""
        super(Form_supervisor, self).clean()

        password = self.cleaned_data.get('password')
        password_bis = self.cleaned_data.get('password_bis')

        if password and password_bis and password != password_bis:
            raise forms.ValidationError("Passwords are NOT identical")
        else:
            return self.cleaned_data


def create_supervisor_and_user(request):
    if request.method == 'POST':
        form = Form_supervisor(request.POST)

        if form.is_valid():
            new_user = User(
                username=form.cleaned_data['name'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['name'],
                last_name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
            )
            new_user.save()

            new_supervisor = Supervisor(
                user_auth = new_user,
                email=form.cleaned_data['email'],
                specialization = form.cleaned_data['specialization'],
            )

            new_supervisor.save()

            return redirect(to='home')  # just get us to home
        else:  # this means that we have errors to render
            return render(request, 'tasks_manager/create_supervisor_and_user.html', context={
                'form': form
            })

    elif request.method == 'GET':
        form = Form_supervisor()
        return render(request, 'tasks_manager/create_supervisor_and_user.html', context={
            'form': form
        })
    else:
        raise Exception("method is not expected {}".format(request.method))
