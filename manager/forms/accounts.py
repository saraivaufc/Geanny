from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password
from django.db.models import Q


from manager.models import User, Attendee, Organizer
from manager.management.permissions import group_permissions


class LoginForm(ModelForm):
	next = forms.CharField(widget=forms.HiddenInput)
	user_cache = None

	def is_valid(self):
		super(LoginForm, self).is_valid()
		try:
			user = User.objects.get(username=self.cleaned_data['username'])
 		except User.DoesNotExist:
			self._errors['no_user'] = _('User does not exist')
			print 'casa'
			return False
 		if not check_password(self.cleaned_data['password'], user.password):
			self._errors['invalid_password'] = _('Password is invalid')
			print 'papel'
			return False
		print 'tesoura'
		return True

	class Meta:
		model= User
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
	