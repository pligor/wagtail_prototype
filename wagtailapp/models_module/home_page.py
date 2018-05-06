from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel


class HomePage(Page): #this was already defined ??? and now we are making it better
    """By default, it will look for a template filename formed from the app and model name,
    separating capital letters with underscores (e.g. HomePage within the ‘home’ app becomes home/home_page.html)"""
    home_body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('home_body', classname="full")
    ]

    #     You can apply custom behavior to this process by overriding Page class methods such as route() and serve()
    # in your own models