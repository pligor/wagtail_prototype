"""work_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import reverse_lazy
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls
from .views import some_blogs, redirect_to_my_auth

from django.views.generic import TemplateView

urlpatterns = [
    url(r'^cms/login', redirect_to_my_auth, name="wagtailadmin_login"),  # admin interface for wagtail
    url(r'^cms/', include(wagtailadmin_urls)),  # admin interface for wagtail
    url(r'^documents/', include(wagtaildocs_urls)),  # document files to be served (document management)
    url(r'^some_blogs/', some_blogs, name='some_blogs'),  # here are all the pages
    url(r'', include(wagtail_urls)),  # here are all the pages
]

"""
 [0-9] is equivalent to [0123456789]
•
 [a-z] matches all the letters, [abcdefghijklmnopqrstuvwxyz]
•
 [A-Z] matches all uppercase letters
•
 [a-zA-Z] matches all the letters
The following are the shortcuts:
•
 \d is equivalent to [0-9]
•
 \w is equivalent to [a-zA-Z0-9_]
•
 [0-9] is equivalent to [0123456789]
"""
