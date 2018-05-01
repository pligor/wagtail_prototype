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
from django.contrib import admin
from .index import home

admin.autodiscover()

urlpatterns = [
    url(r'^$', home),
    url(r'^index/$', home),
    url(r'^admin/', admin.site.urls),
    url(r'^tasks_mngr/', include('tasks_manager.urls')),
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
