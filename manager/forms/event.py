from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from manager.models import Event

class EventForm(ModelForm):
    class Meta:
    	model= Event
        fields = ("name","description", "type", "start_date", "end_date", "capacity", "value", "image", "active")