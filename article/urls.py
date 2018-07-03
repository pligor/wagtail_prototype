from rest_framework import routers
from article.viewsets import ArticleViewSet

router = routers.DefaultRouter()

router.register(r'article', ArticleViewSet)

from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^frontpage//{0,1}$', TemplateView.as_view(template_name='article/index.html')),
]