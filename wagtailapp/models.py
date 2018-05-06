from django.db import models

# this is a Blog Page Model
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.search import index
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from modelcluster.fields import ParentalKey

# from .models.my_home_page import *
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

class HomePage(Page): #this was already defined ??? and now we are making it better
    """By default, it will look for a template filename formed from the app and model name,
    separating capital letters with underscores (e.g. HomePage within the ‘home’ app becomes home/home_page.html)"""
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]

class BlogIndexPage(Page): #this is the index page for our blog
    intro = RichTextField(blank=True) #this is a rich text field

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]


# class BlogPage(Page):  # this is like a Django Model
#
#     # Database fields
#     body = RichTextField()  # for a WYSIWYG editor
#     date = models.DateField("Post date")
#     feed_image = models.ForeignKey(
#         "wagtailimages.Image",
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name='+'
#     )
#     # Use django-taggit module supported by wagtail for tags
#
#     # Search index configuration. Just creating some index in the database for faster querying
#     search_fields = Page.search_fields + [
#         # these two are supported. You are either filtering or you are searching.
#         # OR actually you can even create two indices for both filtering and searching to a field
#         # but that's all for now
#         # http://docs.wagtail.io/en/v2.0.1/topics/search/indexing.html#wagtailsearch-indexing-fields
#         index.SearchField('body'),
#         index.FilterField('date')
#     ]
#
#     # defining how the page’s fields will be arranged in the page editor interface: all ...._panels like
#     # content panels: for content such as main body text
#     promote_panels = [  # for metadata, such as tags, thumbnail image and SEO title
#         # Here we are structuring fields in the interface
#
#         MultiFieldPanel(Page.promote_panels, "Common page configuration"),
#         # Here we are taking the default promote panels of the page and we are grouping them together
#
#         # For only four specific model types which are linked via a foreign key we can have a chooser like
#         # so:
#         # PageChooserPanel
#         # ImageChooserPanel
#         # DocumentChooserPanel
#         # SnippetChooserPanel
#         ImageChooserPanel('feed_image')  # for the feed_image foreign link here
#
#         # For all the rest the FieldPanel will create a dropdown
#     ]
#
#     # Control where this page type may be used in the website
#     # parent_page_types = ['wagtailapp.BlogIndex']  # So here Blogs can be created only under BlogIndex type (which we haven't created yet!)
#     subpage_types = []  # No subpage types.
#     # Therefore you define a hierarchy
#     #Setting parent_page_types to an empty list is a good way of preventing a particular page type from being
#     # created in the editor interface
#
#
# class BlogRelatedLink(Orderable):
#     page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name="related_links")
#     name = models.CharField(max_length=255)
#     url = models.URLField()
#
#     panels = [
#         FieldPanel('name'),
#         FieldPanel('url'),
#     ]
