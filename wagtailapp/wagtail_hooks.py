#The name of this file should NOT be changed

from wagtail.core import hooks
from .models.blog_page import BlogPage

@hooks.register("after_create_page")
def do_after_create_page(request, page):
    if isinstance(page, BlogPage):
        page.specific.author = request.user.username
        # page.save()
        page.save_revision().publish()
    else:
        print("current page is not a blog page")
