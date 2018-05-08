from wagtail.core.fields import RichTextField
from wagtail.search import index
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from .blog_page import BlogPage


class BlogTagIndexPage(Page):
    """This is a page model but does not have any extra
    fields available because it is not necessary"""

    def get_context(self, request):
        # Update template context
        context = super().get_context(request)
        context['tagged_blogpages'] = BlogPage.get_by_tag(tag=request.GET.get('tag'))
        return context
