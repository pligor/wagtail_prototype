from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet
#http://docs.wagtail.io/en/v2.0/topics/snippets.html

#this seems to work automagically, no need to define it anywhere that we are using this particular file to register the
#snippet
@register_snippet
class Advert(models.Model):
    """
    Snippets do NOT use multiple tabs of fields
    Snippets do NOT provide the “save as draft” or “submit for moderation” features
    """

    url = models.URLField(null=True, blank=True)
    text = models.CharField(max_length=255)

    panels = [
        FieldPanel('url'),
        FieldPanel('text')
    ]

    def __str__(self):
        # return super().__str__()
        return self.text
