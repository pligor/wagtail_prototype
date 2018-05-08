from django.db import models

from .models_module.blog_index_page import *
from .models_module.blog_page import *
from .models_module.blog_tag_index_page import *
from .models_module.blog_category import *

#     # HOW TO NAVIGATE THE HIERARCHY
#     # Given a page object 'somepage':
#     # MyModel.objects.descendant_of(somepage)
#     # child_of(page) / not_child_of(somepage)
#     # ancestor_of(somepage) / not_ancestor_of(somepage)
#     # parent_of(somepage) / not_parent_of(somepage)
#     # sibling_of(somepage) / not_sibling_of(somepage)
#     # # ... and ...
#     # somepage.get_children()
#     # somepage.get_ancestors()
#     # somepage.get_descendants()
#     # somepage.get_siblings()

# class BlogIndexPage(Page):  # this is the index page for our blog
#     intro = RichTextField(blank=True)  # this is a rich text field
#
#     content_panels = Page.content_panels + [
#         FieldPanel('intro', classname="full")
#     ]
#
#
#     def get_published_blogposts(self):
#         return self.get_children().live().order_by('-first_published_at')
#
#     # Overriding context and passing more variables in the context of the page
#     # def get_context(self, request):
#     #     # Update context to include only published posts, ordered by reverse-chron
#     #     context = super().get_context(request)
#     #     blogpages = self.get_children().live().order_by('-first_published_at')
#     #     context['blogpages'] = blogpages
#     #     return context
#     subpage_types = ['wagtailapp.BlogPage']
#
#
# class BlogPage(Page):
#     date = models.DateField("Date this blogpost was posted")
#     intro = models.CharField(max_length=250)
#     body = RichTextField(blank=False)
#
#     # We are making both intro and body to be searchable
#     search_fields = Page.search_fields + [
#         index.SearchField('intro'),
#         index.SearchField('body')
#     ]
#
#     content_panels = Page.content_panels + [
#         FieldPanel('date'),
#         FieldPanel('intro'),
#         FieldPanel('body', classname="full"),
#
#         # this is the reference from the parental key, So you are bringing the panel in here!
#         InlinePanel("gallery_images", label="Gallery Images")
#     ]
#
#     # Control where this page type may be used in the website
#     parent_page_types = ['wagtailapp.BlogIndexPage']  # enforce only blog index page to be the parent of this page
#     # subpage_types = []

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
