from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
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

