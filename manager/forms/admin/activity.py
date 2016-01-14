from django.forms import ModelForm, HiddenInput
from django.utils.translation import ugettext_lazy as _

from manager.models import Activity

class ActivityForm(ModelForm):
    class Meta:
    	model= Activity
        fields = (
                "event",
                "name",
        		"description", 
        		"type", 
        		"start_hour", 
        		"end_hour", 
        		"value",
        		"capacity", 
        		"image",
        		"active")
        widgets = {
            'event': HiddenInput(attrs={'class':'hidden'}),
        }