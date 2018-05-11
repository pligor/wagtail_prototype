from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .serializers import UserSerializer
from wagtailapp.models_module.blog_page import BlogPage
from .serializers import BlogPageSerializer
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse


def redirect_to_my_auth(request):
    return redirect_to_login(request.GET.get('next'), login_url="tasks_manager:conn")


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BlogPageViewSet(viewsets.ModelViewSet):
    queryset = BlogPage.objects.all()[:0]  # this will not be used if get_queryset is defined

    def get_queryset(self):
        return BlogPage.objects.all()  # [:2]

    serializer_class = BlogPageSerializer
