# http://docs.wagtail.io/en/v2.0/topics/snippets.html

from django import template
from wagtailapp.models_module.advert_snippet import Advert

register = template.Library()  # initiate register decorator


@register.inclusion_tag('wagtailapp/simple_adverts.html',  # so this is considering the app / name of html
                        takes_context=True  # USEFUL
                        )
def adverts(context):
    return {
        'adverts': Advert.objects.all(),
        'request': context['request']
    }


@register.inclusion_tag('wagtailapp/simple_advert.html')
def simple_advert(advert):
    return {
        'advert': advert,
    }
