from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone

class Organization(models.Model):
    name = models.CharField(max_length=255, verbose_name=_(u"Name"), help_text=_(u'Please enter name.'))
    decription = models.TextField(verbose_name=_(u"Description"), help_text=_(u'Please enter description.'))
    image = models.ImageField(verbose_name=_(u"Image"),help_text=_(u'Please choose an image for the profile of organization.'),upload_to = 'documents/image/event/%Y/%m/%d', null=True, blank=True, default=None)        
    
    creation = models.DateTimeField(verbose_name=_(u'Creation'), default=timezone.now)
    exists = models.BooleanField(verbose_name=_(u"Exists"), default=True)

    def save(self, *args, **kwargs):
        if not self.code:
            i = RegistrationEvent.objects.all().order_by('-code')[0]
            self.code = i.code+1
        super(RegistrationEvent, self).save(*args, **kwargs) 
    


    def __unicode__(self):
        return self.name

    def delete(self):
        self.exists = False
        self.save()
        
    def restore(self):
        self.exists = True
        self.save()
    
    class Meta:
        ordering = ['name']
        verbose_name = _(u"Organization")
        verbose_name_plural = _(u"Organizations")