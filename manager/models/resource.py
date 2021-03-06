from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone

class Resource(models.Model):
    RESOURCE_TYPE = (
        ('LECTURE', _('Lecture')),
        ('COURSE', _('Course')), 
        ('INSTRUCTOR', _('Instructor')),
        ('MATERIAL', _('Material')),
        ('ROOM', _('Room')),
    )
    PRIORITY = (
        ('LOW', _('Low')),
        ('NORMAL', _('Normal')),
        ('HIGH', _('High')), 
    )

    event = models.ForeignKey('Event', verbose_name=_("Event"))
    activities = models.ManyToManyField('Activity', verbose_name=_("Activities"), null=True, blank=True)
    
    name = models.CharField(max_length=255, verbose_name=_(u"Name"), help_text=_(u'Please enter the name of the resource.'))
    description = models.TextField(verbose_name=_(u"Description"), help_text=_(u'Please enter a description of the resource.'))
    type = models.CharField(max_length=255, verbose_name=_(u'Type'), choices=RESOURCE_TYPE, help_text=_(u'Please enter the type of resource.'))
    priority = models.CharField(max_length=255, verbose_name=_(u'Priority'), choices=PRIORITY, help_text=_(u'Please enter the priority of resource.'))
    value = models.FloatField(verbose_name=_(u'Value'),default=1, help_text=_(u'Please choose the quantity of resource.'))
    quantity = models.FloatField(verbose_name=_(u'Quantity'),default=1, help_text=_(u'Please choose the quantity of resource.'))
    image = models.ImageField(verbose_name=_(u"Image"),help_text=_(u'Please choose an image for the profile of your activity.'),upload_to = 'documents/image/resource/%Y/%m/%d', null=True, blank=True, default=None)    
    
    active = models.BooleanField(verbose_name=_(u'Active'), default=False, help_text=_(u'Please check this box if you want to publish your resource.')) 
    creation = models.DateTimeField(verbose_name=_(u'Creation'), default=timezone.now)
    exists = models.BooleanField(verbose_name=_(u"Exists"), default=True)
        
    def get_event(self):
        return self.event
    def get_activities(self):
        return self.activities.objects.filter(exists=True)
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def get_type(self):
        return self.type
    def get_priority(self):
        return self.priority
    def get_value(self):
        return self.value
    def get_quantity(self):
        return self.get_quantity
    def get_image(self):
        return self.image  

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
        verbose_name = _(u"Resource")
        verbose_name_plural = _(u"Resources")
