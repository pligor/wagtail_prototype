from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from wagtailapp.models.blog_page import BlogPage


# class UserSerializer(serializers.HyperlinkedModelSerializer):
class UserSerializer(serializers.ModelSerializer):
    email_name = serializers.SerializerMethodField()

    def get_email_name(self, obj):
        return obj.email.split('@')[0]

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff', 'email_name')


class BlogPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPage
        fields = ("id", "title", "slug", "date", "intro", "body", "author")
