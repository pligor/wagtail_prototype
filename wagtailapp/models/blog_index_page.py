from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from django.db import models
from wagtail.core.models import Orderable
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from django.conf import settings

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    # TODO mainly we only need to change the template for vue.js
    template = 'wagtailapp/blog_index_inline.html' if settings.IS_SINGLE_PAGE_APP else 'wagtailapp/blog_index_page.html'

    # from .ad_blog_rel import AdvertBlogPageIndexRelationship
    # from .advert_snippet import AdvertSnippet
    # its_ads = models.ManyToManyField(AdvertSnippet, through=AdvertBlogPageIndexRelationship)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        InlinePanel('advert_placements', label="Its Advertisements")
    ]

    def get_advertisements(self):
        return (advert_placement.its_advert for advert_placement in self.advert_placements.all())

    def get_published_rev_order(self):
        return self.get_children().live().order_by('-first_published_at')

    # def get_context(self, request):
    #     """Creating variables for the view"""
    #     # Update context to include only published posts, ordered by reverse-chron
    #     context = super().get_context(request)
    #     blogpages = self.get_children().live().order_by('-first_published_at')
    #     context['blogpages'] = blogpages
    #     return context


class BlogAdvertPlacement(Orderable, models.Model):
    """WE ARE FORCED TO CREATE THIS CLASS because we do not want to relate the snippet itself directly with the blog index page"""

    # 1. define the parent
    blog_index_page = ParentalKey(
        "wagtailapp.BlogIndexPage",
        on_delete=models.CASCADE,
        related_name="advert_placements",  # gives access to advert placements
    )

    # 2. It contains one advert which links to
    its_advert = models.ForeignKey(
        to='wagtailapp.AdvertSnippet',
        related_name = "+"
    )

    class Meta:
        verbose_name = "advert placement"
        verbose_name_plural = "advert placements"

    from wagtail.snippets.edit_handlers import SnippetChooserPanel
    panels = [
        SnippetChooserPanel('its_advert')
    ]

    def __str__(self):
        #return super().__str__()
        return self.blog_index_page.title + " >deixnei> " + self.its_advert.text



