from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .serializers import UserSerializer
from wagtailapp.models_module.blog_page import BlogPage
from .serializers import BlogPageSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BlogPageViewSet(viewsets.ModelViewSet):
    queryset = BlogPage.objects.all()[:0]  # this will not be used if get_queryset is defined

    def get_queryset(self):
        return BlogPage.objects.all()  # [:2]

    serializer_class = BlogPageSerializer
