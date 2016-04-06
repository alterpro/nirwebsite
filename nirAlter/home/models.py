from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class HomePage(Page):
    top_title = models.CharField(max_length=100, blank=True)
    top_sub_title = models.CharField(max_length=250, blank=True)
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('top_title'),
        FieldPanel('top_sub_title'),
        FieldPanel('body', classname="full"),
    ]
