from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password
from django.db.models import Q


from manager.models import User, Attendee, Organizer
from manager.management.permissions import group_permissions


class LoginForm(forms.Form):
	username = forms.CharField(label=_('Username'), help_text=_("Please enter you username."),
		widget=forms.TextInput(), 
		error_messages={'required': _('Please enter you username.')} )
	password = forms.CharField(label=_('Password'), help_text=_('Please enter you password.'),
		widget=forms.PasswordInput(),
		error_messages={'required': _('Please enter you password.')})

	class Meta:
		fields = ("username","password")

class RegisterForm(ModelForm):
	GROUPS = [
		('attendee',_('Attendee')),
		('organizer',_('Organizer')),
	]
	group = forms.ChoiceField(label=_("Group"), choices=GROUPS)
	class Meta:
		model= User
		fields = ("first_name", "last_name","email", "username","password", "group")

class AttendeeRegisterForm(RegisterForm):
	class Meta(RegisterForm.Meta):
		model = Attendee

class OrganizerRegisterForm(RegisterForm):
	class Meta(RegisterForm.Meta):
		model = Organizer
	