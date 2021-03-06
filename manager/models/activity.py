from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone

class Activity(models.Model):
    ACTIVITY_TYPE = (
        ('LECTURE', _('Lecture')),
        ('COURSE', _('Course')), 
    )
    event = models.ForeignKey('Event', verbose_name=_("Event"))
    name = models.CharField(max_length=255, verbose_name=_(u"Name"), help_text=_(u'Please enter the name of the activity.'))
    description = models.TextField(verbose_name=_(u"Description"), help_text=_(u'Please enter a description of the activity.'))
    type = models.CharField(verbose_name=_(u'Type'), choices=ACTIVITY_TYPE, help_text=_(u'Please enter the type of your event.'), max_length=255)
    start_hour =  models.TimeField(verbose_name=_(u'Start Hour'), help_text=_(u'Please enter the starting hour of the activity.'))
    end_hour =  models.TimeField(verbose_name=_(u'End Hour'), help_text=_(u'Please enter the end date of the activity.'))
    value = models.FloatField(verbose_name=_(u'Value'),default=0.0, help_text=_(u'Please choose the registration fee.'))
    image = models.ImageField(verbose_name=_(u"Image"),help_text=_(u'Please choose an image for the profile of your activity.'),upload_to = 'documents/image/activity/%Y/%m/%d', null=True, blank=True, default=None)    
    capacity = models.IntegerField(verbose_name=_(u'Capacity'), help_text=_(u'Please ability of people to your activity supports.'))
    active = models.BooleanField(verbose_name=_(u'Active'), default=False, help_text=_(u'Please check this box if you want to publish your activity.'))
    
    active = models.BooleanField(verbose_name=_(u'Active'), default=False, help_text=_(u'Please check this box if you want to publish your activity.'))
    creation = models.DateTimeField(verbose_name=_(u'Creation'), default=timezone.now)
    exists = models.BooleanField(verbose_name=_(u"Exists"), default=True)
    
    def get_event(self):
        return self.event
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def get_type(self):
        return self.type
    def get_start_hour(self):
        return self.start_hour
    def get_end_hour(self):
        return self.end_hour
    def get_value(self):
        return self.value
    def get_image(self):
        return self.image
    def get_capacity(self):
        return self.capacity    


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
        verbose_name = _(u"Activity")
        verbose_name_plural = _(u"Activitis")