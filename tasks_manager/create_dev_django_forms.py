from django.shortcuts import render
from django.http import HttpResponse
from .models import Developer, Supervisor

from django import forms


class Form_inscription(forms.Form):
    """this generates forms similar to models style"""

    name = forms.CharField(label='ONOMA', max_length=30, error_messages={
        # TODO pws ta kanoume na fainontai auta giati me thn javascript kaleitai kati topika
        'required': 'Prepei na patisei to onoma!',
        'invalid': 'Lathos!'
    }
                           )
    login = forms.CharField(label='Login', max_length=30)

    # it is still a charfield but it is wrapped to be a password input
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    password_bis = forms.CharField(label='Password (again)', widget=forms.PasswordInput)

    supervisor = forms.ModelChoiceField(label='Supervisor', queryset=Supervisor.objects.all())

    def clean(self):
        """Extending clean method"""
        super(Form_inscription, self).clean()

        password = self.cleaned_data.get('password')
        password_bis = self.cleaned_data.get('password_bis')

        if password and password_bis and password != password_bis:
            raise forms.ValidationError("Passwords are NOT identical")
        else:
            return self.cleaned_data


def create_developer_django_forms(request):
    if request.method == 'POST':
        form = Form_inscription(request.POST)

        if form.is_valid():
            new_dev = Developer(
                name=form.cleaned_data['name'],
                login=form.cleaned_data['login'],
                password=form.cleaned_data['password'],
                its_supervisor=form.cleaned_data['supervisor']
            )

            new_dev.save()

            return HttpResponse("Developer was added")
        else:
            return render(request, 'tasks_manager/create_developer_django_forms.html', context={
                'form': form,  # this is to display the errors appropriately
            })

    else:
        form = Form_inscription()

        return render(request, 'tasks_manager/create_developer_django_forms.html', context={
            'form': form
        })
