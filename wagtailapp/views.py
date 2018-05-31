from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models.blog_page import BlogPage
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse

#https://stackoverflow.com/a/49871282/720484
def redirect_to_my_auth(request):
    return redirect_to_login(reverse('wagtailadmin_home'), login_url="tasks_manager:conn")

# Create your views here.
def some_blogs(request):
    attrs = ["id",
        "title",
        "slug",
        "date",
        "intro",
        "body",
        "author",]

    blogs = BlogPage.objects.all()[:2]
    for blog in blogs:
        # print("\n".join(blog.__dict__.keys()))
        for attr in attrs:
            print(getattr(blog, attr))
        print()

    response = HttpResponse("you are in the blogs")
    return response

# id
# title
# slug
# date
# intro
# body
# author
