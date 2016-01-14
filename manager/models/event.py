from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone

class Event(models.Model):
    EVENT_TYPE = (
        ('PRESENTIAL', _('Presential')),
        ('ONLINE', _('Online'))   
    )
    name = models.CharField(max_length=255, verbose_name=_(u"Name"), help_text=_(u'Please enter the name of the activity.'))
    description = models.TextField(verbose_name=_(u"Description"), help_text=_(u'Please enter a description of the activity.'))
    type = models.CharField(max_length=100, verbose_name=_(u'Type'), choices=EVENT_TYPE, help_text=_(u'Please enter the type of your event.'))
    address = models.ForeignKey('Address', verbose_name=_(u'Address'), null=True, blank=True)
    start_date =  models.DateField(verbose_name=_(u'Start Date'), help_text=_(u'Please enter the starting date of the event.'))
    end_date =  models.DateField(verbose_name=_(u'End Date'), help_text=_(u'Please enter the end date of the event.'))
    capacity = models.IntegerField(verbose_name=_(u'Capacity'), help_text=_(u'Please ability of people to your event supports.'))
    value = models.FloatField(verbose_name=_(u'Value'),default=0.0, help_text=_(u'Please choose the registration fee.'))
    image = models.ImageField(verbose_name=_(u"Image"),help_text=_(u'Please choose an image for the profile of your event.'),upload_to = 'documents/image/event/%Y/%m/%d', null=True, blank=True, default=None)        
    
    active = models.BooleanField(verbose_name=_(u'Active'), default=False, help_text=_(u'Please check this box if you want to publish your event.'))
    creation = models.DateTimeField(verbose_name=_(u'Creation'), default=timezone.now)
    exists = models.BooleanField(verbose_name=_(u"Exists"), default=True)
    
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def get_type(self):
        return self.type
    def get_address(self):
        return self.address
    def get_start_date(self):
        return self.start_date
    def get_end_date(self):
        return self.end_date
    def get_capacity(self):
        return self.capacity
    def get_value(self):
        return self.value
    def get_image(self):
        return self.image
    def get_activities(self):
        from manager.models import Activity
        return Activity.objects.filter(event=self.id, exists=True)



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
        verbose_name = _(u"Event")
        verbose_name_plural = _(u"Events")