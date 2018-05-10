from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import authenticate, login
from django.conf import settings

class Form_connection(forms.Form):
    def initialize(self, request):
        self.request = request

    username = forms.CharField(label='Login')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    next_url = forms.CharField(widget=forms.HiddenInput, required=False)

    def clean(self):
        # after this call self.cleaned_data should be populated
        super(Form_connection, self).clean()

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        # print([username, password])

        if username and password and not authenticate(
                username=username, password=password, request=self.request):
            raise forms.ValidationError("Wrong login or pass")
        else:
            return self.cleaned_data

def connection(request):
    if request.method == 'POST':
        form = Form_connection(request.POST)
        form.initialize(request)

        # print("NEXT_URL POST")
        # print(form.data['next_url'])

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # authenticate actually gets you user object!
            # user = authenticate(username=username, password=password)
            user = authenticate(username=username, password=password, request=request)

            if user:
                # the login now means that your user is logged in and any authorizations will pass
                # login(request, user) #TODO what does this function do exactly

                next_url = form.cleaned_data["next_url"] or request.GET.get("next", "")

                if len(next_url) == 0:
                    response = redirect(to='home')
                else:
                    response = redirect(to=next_url)

                print("we are saving the token: {}".format(user.keystone_token))
                response.set_cookie(key=settings.KEYSTONE_TOKEN_KEY, value=user.keystone_token)

                return response
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
        form.initialize(request)

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
