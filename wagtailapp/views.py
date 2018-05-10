from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import BlogPage


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
