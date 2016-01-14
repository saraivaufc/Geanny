from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone

class Payment(models.Model):
    user = models.ForeignKey('Person', verbose_name=_(u'Person'))
    value = models.FloatField(verbose_name=_(u'Value'),default=0.0)
    is_maturity = models.BooleanField(verbose_name=_(u'Maturity'), default=False)
    maturity_date = models.DateTimeField(verbose_name=_(u'Maturity Date'))
    
    is_paid = models.BooleanField(verbose_name=_(u'Paid'), default=False)
    paid_value = models.FloatField(verbose_name=_(u'Value'),default=0.0)
    paid_date = models.DateTimeField(verbose_name=_(u'Paid Date'), null=True, blank=True)
    
    monthly_interest =  models.FloatField(verbose_name=_(u'Monthly Interest'),default=0.0)

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
        ordering = ['user']
        verbose_name = _(u"Address")
        verbose_name_plural = _(u"Addreses")