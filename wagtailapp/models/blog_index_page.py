from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from django.db import models


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    from .ad_blog_rel import AdvertBlogPageIndexRelationship
    from .advert_snippet import AdvertSnippet
    its_ads = models.ManyToManyField(AdvertSnippet, through=AdvertBlogPageIndexRelationship)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('its_ads')
    ]

    def get_published_rev_order(self):
        return self.get_children().live().order_by('-first_published_at')

    # def get_context(self, request):
    #     """Creating variables for the view"""
    #     # Update context to include only published posts, ordered by reverse-chron
    #     context = super().get_context(request)
    #     blogpages = self.get_children().live().order_by('-first_published_at')
    #     context['blogpages'] = blogpages
    #     return context

