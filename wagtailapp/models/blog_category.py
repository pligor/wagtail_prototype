from django.db import models
from wagtail.core.fields import RichTextField
from wagtail.search import index
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

#Snippets are managed by Wagtail admin interface
#Snippets do NOT exist as part of the page tree themselves
from wagtail.snippets.models import register_snippet

@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    #Note that we are using panels rather than content_panels here - since snippets generally
    # have no need for fields such as slug or publish date, the editing interface for them is
    # not split into separate ‘content’ / ‘promote’ / ‘settings’ tabs as standard, and so there
    # is no need to distinguish between ‘content panels’ and ‘promote panels’.
    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name
        # return super().__str__()

    class Meta:
        verbose_name_plural = "blog categories"
