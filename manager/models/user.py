from django.db import models

# -*- coding: UTF-8 -*-

from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User as UserAuth
from django.contrib.auth.models import Group

class Person(UserAuth):
	profile_image = models.ImageField(verbose_name=_(u"Profile Image"), help_text=_(u"Please enter you profile image."), upload_to = 'documents/image/profile_image/%Y/%m/%d', null=True, blank=True, default=None)
	phone = models.CharField(verbose_name=_('Phone'), max_length=200, blank=True, null=True)
	address = models.CharField(verbose_name=_('Address'), max_length=200, blank=True, null=True)
	exists = models.BooleanField(default = True)
	
	def get_username(self):
		return self.username

	def get_first_name(self):
		return self.first_name

	def get_last_name(self):
		return self.last_name

	def get_email(self):
		return self.email

	def get_profile_image(self):
		return self.profile_image

	def get_phone(self):
		return self.phone

	def get_address(self):
		return self.address

	def is_member(self, group):
		return self.groups.filter(name=group).exists()
		
	def save(self,group=None, *args, **kwargs):
		super(Person, self).save(*args, **kwargs)
		if not group:
			group = 'attendee'
		print "Add person in",group
		group = Group.objects.get(name=group)
		self.groups.add(group)


	class Meta:
		ordering = ['-date_joined', ]
		verbose_name = _(u'Person')
		verbose_name_plural = _(u'Persons')
		
class Attendee(Person):

	def __unicode__(self):
		return self.get_email()

	class Meta(Person.Meta):
		verbose_name = _('Attendee')
		verbose_name_plural = _('Attendees')

class Organizer(Person):

	def __unicode__(self):
		return self.get_email()

	class Meta(Person.Meta):
		verbose_name = _('Organizer')
		verbose_name_plural = _('Organizes')
		