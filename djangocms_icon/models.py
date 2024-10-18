from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from cms.models import CMSPlugin
from djangocms_attributes_field.fields import AttributesField
from djangocms_icon.translatable_utils import TranslatablePluginModel
from parler.models import TranslatedFields

from .fields import Icon


# Add additional choices through the ``settings.py``.
def get_templates():
    choices = [
        ('default', _('Default')),
    ]
    choices += getattr(
        settings,
        'DJANGOCMS_ICON_TEMPLATES',
        [],
    )
    return choices


class AbstractIcon(TranslatablePluginModel):
    icon = Icon()

    template = models.CharField(
        verbose_name=_('Template'),
        choices=get_templates(),
        default=get_templates()[0][0],
        max_length=255,
    )
    label = models.CharField(
        verbose_name=_('Label'),
        blank=True,
        max_length=255,
    )
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        return self.label or ''


class Icon(AbstractIcon):
    translations = TranslatedFields(
        icon_new=Icon(),
        template_new=models.CharField(
            verbose_name=_('Template'),
            choices=get_templates(),
            default=get_templates()[0][0],
            max_length=255,
        ),
        label_new=models.CharField(
            verbose_name=_('Label'),
            blank=True,
            max_length=255,
        ),
    )

    class Meta:
        abstract = False
