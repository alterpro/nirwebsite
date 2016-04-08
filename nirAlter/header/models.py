from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailcore.models import Orderable
from modelcluster.fields import ParentalKey, ClusterableModel

# from .managers import MenuItemManager

@register_snippet
class Menu(ClusterableModel):
    site = models.OneToOneField('wagtailcore.Site', related_name="main_menu")

    # objects = MenuItemManager()
    title = models.CharField(max_length=255, null=False, blank=False)
    brand_text = models.CharField(max_length=20, null=True, blank=True)
    brand_image_width = models.IntegerField(blank=True, null=True)
    brand_image_height = models.IntegerField(blank=True, null=True)
    brand_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    @property
    def items(self):
        return self.objects.all()

    def __unicode__(self):
        return 'For %s' % (self.site.site_name or self.site)

    panels = (
        FieldPanel('site'),
        FieldPanel('brand_text'),
        ImageChooserPanel('brand_image'),
        FieldPanel('brand_image_width'),
        FieldPanel('brand_image_height'),
        InlinePanel('menu_items', label="Menu Items", help_text='Set the menu items for the current menu.'),
    )

    class Meta:
        verbose_name = _("menu")
        verbose_name_plural = _("menu")


class MenuItem(models.Model):
    allow_subnav = False

    link_page = models.ForeignKey(
        'wagtailcore.Page',
        verbose_name=_('Link to an internal page'),
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    link_url = models.CharField(
        max_length=255,
        verbose_name=_('Link to a custom URL'),
        blank=True,
        null=True,
    )
    link_text = models.CharField(
        max_length=255,
        blank=True,
        help_text=_("Must be set if you wish to link to a custom URL."),
    )
    url_append = models.CharField(
        verbose_name=_("Hash or querystring to append to URL"),
        max_length=255,
        blank=True,
    )

    # objects = MenuItemManager()

    class Meta:
        abstract = True
        verbose_name = _("menu item")
        verbose_name_plural = _("menu items")

    def relative_url(self, current_site):
        try:
            url = self.link_page.relative_url(current_site)
        except AttributeError:
            url = self.link_url
        return url + self.url_append

    @property
    def menu_text(self):
        if self.link_page:
            return self.link_text or self.link_page.title
        return self.link_text

    @property
    def menu_url(self):
        if (self.link_page):
            return self.link_page.url
        else:
            return self.link_url

    def clean(self, *args, **kwargs):
        super(MenuItem, self).clean(*args, **kwargs)

        if self.link_url and not self.link_text:
            raise ValidationError({
                'link_text': [
                    _("This must be set if you're linking to a custom URL."),
                ]
            })

        if not self.link_url and not self.link_page:
            raise ValidationError({
                'link_url': [
                    _("This must be set if you're not linking to a page."),
                ]
            })

        if self.link_url and self.link_page:
            raise ValidationError(_(
                "You cannot link to both a page and URL. Please review your "
                "link and clear any unwanted values."
            ))

    def __unicode__(self):
        return self.menu_text

    panels = (
        PageChooserPanel('link_page'),
        FieldPanel('url_append'),
        FieldPanel('link_text'),
        FieldPanel('link_url'),
    )


class HeaderMenuItem(Orderable, MenuItem):
    menu = ParentalKey('Menu', related_name='menu_items', null=True)

    allow_subnav = models.BooleanField(
        default=True,
        verbose_name=_(
            "Allow sub-navigation for this page"
        ),
    )
    panels = MenuItem.panels + (
        FieldPanel('allow_subnav'),
    )
