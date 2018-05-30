#http://docs.wagtail.io/en/v2.0/topics/snippets.html

from django import template
from wagtailapp.advert_snippet import Advert

register = template.Library() #initiate register decorator

@register.inclusion_tag('wagtailapp/advert.html', #so this is considering the app
                        takes_context=True #USEFUL
                        )
def adverts(context):
    return {
        'adverts': Advert.objects.all(),
        'request': context['request']
    }