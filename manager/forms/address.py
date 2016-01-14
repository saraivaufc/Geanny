from django.forms import ModelForm, HiddenInput
from django.utils.translation import ugettext_lazy as _

from manager.models import Address

class AddressForm(ModelForm):
    class Meta:
    	model= Address
        fields = (
                "cep",
                "street",
        		"district", 
        		"city", 
        		"state",
                )