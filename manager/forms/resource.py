from django.forms import ModelForm, HiddenInput
from django.utils.translation import ugettext_lazy as _

from manager.models import Resource

class ResourceForm(ModelForm):
    class Meta:
        model= Resource
        fields = (
                "event",
                "activities",
                "name",
                "description", 
                "type",
                "priority",
                "value",
                "quantity",
                "image",
                "active",
                )
        widgets = {
            'event': HiddenInput(attrs={'class':'hidden'}),
            'activities': HiddenInput(attrs={'class':'hidden'}),
        }
