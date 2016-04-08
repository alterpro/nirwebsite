from django.template import loader, Library
from header.models import *

register = Library()


@register.simple_tag(takes_context=True)
def header_menu(context, template='header_menu.html'):
    request = context['request']
    site = request.site
    try:
        menu = site.main_menu
    except Menu.DoesNotExist:
        menu = Menu.objects.create(site=site)

    context.update({
        'menu': menu
    })

    return loader.get_template(template).render(context)
