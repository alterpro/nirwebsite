from django import template
from header.models import *

register = template.Library()

# header snippet
@register.inclusion_tag('../header/templates/menu.html', takes_context=True)
def menu(context, name):
    return {
        'menu_items': Menu.items,
        'request': context['request'],
    }
