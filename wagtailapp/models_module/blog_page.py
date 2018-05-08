from django.db import models
from django import forms

from wagtail.core.fields import RichTextField
from wagtail.search import index
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from .blog_category import BlogCategory

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        "wagtailapp.BlogPage",
        on_delete=models.CASCADE,
        related_name="tagged_items",
    )


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=False)
    categories = ParentalManyToManyField(to=BlogCategory, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),

            #This is NOT an Inline Panel because it is looking up to a parent(s)
            # (since it is many to many)
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple)
            # Widget is not necessary, but we choose our own for UX reasons

        ], heading="Setup your blog info here"),

        FieldPanel('intro'),
        FieldPanel('body', classname="full"),

        #This is because we are looking down, to children images
        InlinePanel(relation_name='gallery_images', label="Gallery Images"),
    ]

    parent_page_types = ['wagtailapp.BlogIndexPage']

    @staticmethod
    def get_by_tag(tag):
        return BlogPage.objects.filter(tags__name=tag)


class BlogPageGalleryImage(Orderable):
    # A ParentalKey works similarly to a ForeignKey, but also defines BlogPageGalleryImage
    # as a “child” of the BlogPage model, so that it’s treated as a fundamental part of the
    # page in operations like submitting for moderation, and tracking revision history.
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
