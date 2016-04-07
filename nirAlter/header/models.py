from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailcore.models import Orderable
from blog.models import LinkFields
from modelcluster.fields import ParentalKey, ClusterableModel

class MenuManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(title=name)

@register_snippet
class Menu(ClusterableModel):
    objects = MenuManager()
    title = models.CharField(max_length=255, null=False, blank=False)

    @property
    def items(self):
        return self.objects.all()

    def __unicode__(self):
        return self.title

Menu.panels = [
    FieldPanel('title', classname='full title'),
    InlinePanel('menu_items', label="Menu Items", help_text='Set the menu items for the current menu.')
]

class MenuItem(Orderable, LinkFields):
    parent = ParentalKey(Menu, related_name='menu_items', null=True)
    link_title = models.CharField(max_length=255)
