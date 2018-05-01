from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import authenticate, login


class Form_connection(forms.Form):
    username = forms.CharField(label='Login')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    next_url = forms.CharField(widget=forms.HiddenInput)

    def clean(self):
        # after this call self.cleaned_data should be populated
        super(Form_connection, self).clean()

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        # print([username, password])

        if username and password and not authenticate(username=username, password=password):
            # print("INVALID USER!!")
            raise forms.ValidationError("Wrong login or pass")
        else:
            return self.cleaned_data


def connection(request):
    if request.method == 'POST':
        form = Form_connection(request.POST)

        # print("NEXT_URL POST")
        # print(form.data['next_url'])

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # authenticate actually gets you user object!
            user = authenticate(username=username, password=password)

            if user:
                # the login now means that your user is logged in and any authorizations will pass
                login(request, user)

                next_url = form.cleaned_data["next_url"]
                return redirect(to=next_url)
            else:
                return render(request, 'tasks_manager/connection.html')
        else:
            return render(request, 'tasks_manager/connection.html', context={
                'form': form
            })
    elif request.method == 'GET':
        form = Form_connection(
            {
                'next_url': request.GET.get('next')
            }
        )

        # print("NEXT_URL GET")
        # print(form.data['next_url'])

        # if form.next_url is None:
        return render(request, 'tasks_manager/connection.html', context={
            'form': form
        })
        # else:
        #     return redirect(to=form.next_url)
    else:
        raise Exception("invalid method")
