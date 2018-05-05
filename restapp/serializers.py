from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


# class UserSerializer(serializers.HyperlinkedModelSerializer):
class UserSerializer(serializers.ModelSerializer):
    email_name = serializers.SerializerMethodField()

    def get_email_name(self, obj):
        return obj.email.split('@')[0]

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff', 'email_name')
