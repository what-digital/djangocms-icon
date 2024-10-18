from django import forms
from parler.forms import TranslatableModelForm

from .fields import IconField
from .models import Icon


class IconForm(TranslatableModelForm):
    icon = IconField(required=True)

    class Meta:
        model = Icon
        fields = ('label', 'icon', 'template', 'attributes',)
