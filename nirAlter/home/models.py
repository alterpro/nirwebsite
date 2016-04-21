from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel



class HomePage(Page):
    top_title = models.CharField(max_length=100, blank=True)
    top_sub_title = models.CharField(max_length=250, blank=True)
    body = RichTextField(blank=True)
    top_background_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    top_background_image_height = models.IntegerField(blank=True, null=True)


    content_panels = Page.content_panels + [
        FieldPanel('top_title'),
        FieldPanel('top_sub_title'),
        FieldPanel('body', classname="full"),
        ImageChooserPanel('top_background_image'),
        FieldPanel('top_background_image_height'),
    ]
