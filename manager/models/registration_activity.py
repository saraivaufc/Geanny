from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone

class RegistrationActivity(models.Model):
    activity = models.ForeignKey('Activity', verbose_name=_("Activity"))
    attendee = models.ForeignKey('attendee', verbose_name=_(u'Attendee'))
    accredited = models.BooleanField(default=False, verbose_name=_(u'Accredited'))
    registration_date = models.DateTimeField(verbose_name=_(u'Registration Date'), default=timezone.now)
    payments = models.ManyToManyField('Payment',verbose_name=_(u'Payments'), default=None)
    
    creation = models.DateTimeField(verbose_name=_(u'Creation'), default=timezone.now)
    exists = models.BooleanField(verbose_name=_(u"Exists"), default=True)


    def __unicode__(self):
        return self.name

    def delete(self):
        self.exists = False
        self.save()
        
    def restore(self):
        self.exists = True
        self.save()
    
    class Meta:
        ordering = ['creation']
        verbose_name = _(u"Address")
        verbose_name_plural = _(u"Addreses")