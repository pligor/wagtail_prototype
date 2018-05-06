from django.db import models
from wagtail.core.models import Page, Orderable
# this is a Blog Page Model
from wagtail.core.models import Page, Orderable
from wagtail.search import index
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from modelcluster.fields import ParentalKey
from wagtail.core.fields import RichTextField

from ..models import BlogPage

#Inheriting from Orderable adds a sort_order field to the model, to keep track of the ordering of images in the gallery.
class BlogPageGalleryImage(Orderable):
    # A field to connect it to the page
    #The ParentalKey to BlogPage is what attaches the gallery images to a specific page. A ParentalKey works similarly
    #  to a ForeignKey, but also defines BlogPageGalleryImage as a “child” of the BlogPage model, so that it’s treated
    # as a fundamental part of the page in operations like submitting for moderation, and tracking revision history.
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')

    ### What fields are included
    # we are not saving the image here inside the table of the model but we are linking to the images of wagtail
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE,
        related_name='+'  # why just a plus sign ???
    )
    #Use this configuration if you want to keep the image after deletion of
    # the blogpost: blank=True, null=True, on_delete=models.SET_NULL

    caption = models.CharField(blank=False, max_length=250)

    # how is it going to be rendered
    panels = [
        ImageChooserPanel("image"),  # choose an image
        FieldPanel("caption"),  # type the string of the caption
    ]
