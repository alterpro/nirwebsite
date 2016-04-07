from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsnippets.models import register_snippet
from blog.models import LinkFields


@register_snippet
class Header(models.Model):
    url = models.URLField(null=True, blank=True)
    text = models.CharField(max_length=255)

    panels = [
        FieldPanel('url'),
        FieldPanel('text'),
    ]

    def __str__(self):              # __unicode__ on Python 2
        return self.text

class MenuItem(LinkFields):
    @property
    def url(self):
        return self.link

    def __unicode__(self):
        if self.link_external:
            title = self.link_external
        elif self.link_page:
            title = self.link_page.title
        elif self.link_document:
            title = self.link_document.title
        return title

    class Meta:
        verbose_name = "Menu item"
        description = "Items appearing in the menu"
