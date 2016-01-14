from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.contrib import messages

from manager.forms.admin import ResourceForm
from manager.models import Event as EventModel
from manager.models import Resource as ResourceModel
from manager.utils.decorators import group_required

class Resource(object):
    
    @method_decorator(login_required)
    @method_decorator(group_required('organizer'))
    def see(self, request, resource_id):
        try:
            resource = ResourceModel.objects.get(id=resource_id, exists=True)
            return render(request, 'manager/admin/resource/see.html', {'resource': resource})
        except ResourceModel.DoesNotExist:
            messages.error(request, 'Resource no fount.')
            HttpResponseRedirect(reverse('admin'))
            

    @method_decorator(login_required)
    @method_decorator(group_required('organizer'))
    def add(self, request, event_id):
        try:
            event = EventModel.objects.get(id=event_id, exists=True)
        except EventModel.DoesNotExist:
            messages.error(request, 'Event no fount.')
            return HttpResponseRedirect(reverse('admin'))

        if request.method == "POST":
            request.POST = request.POST.copy()
            request.POST['event'] = event.id
            request.POST['activities'] = []

            form = ResourceForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, _('Successfully added resource.'))
                return HttpResponseRedirect(reverse('admin_event_see', kwargs={'event_id':event_id}))
            else:
                messages.error(request,_('Error adding resource.'))
        else:
            form = ResourceForm()
        return render(request, 'manager/admin/resource/form.html', {'form': form, 'event': event , 'type':'add'})
    

    @method_decorator(login_required)
    @method_decorator(group_required('organizer'))
    def edit(self, request, resource_id):
        try:
            resource = ResourceModel.objects.get(id=resource_id, exists=True)
        except ResourceModel.DoesNotExist:
            messages.error(request, 'Resource no fount.')
            return HttpResponseRedirect(reverse('admin'))

        if request.method == 'POST':
            request.POST = request.POST.copy()
            request.POST['event'] = resource.get_event().id
            form = ResourceForm(request.POST, request.FILES, instance=resource)
            if form.is_valid():
                resource = form.save()
                messages.success(request, _("Successfully edited resource"))
                return HttpResponseRedirect(reverse('admin_resource_see',kwargs={'resource_id':resource_id} ))
            else:
                messages.error(request, _("Error when editing resource"))
        else:
            form = ResourceForm(instance=resource)
        return render(request, 'manager/admin/resource/form.html', {'form': form,'resource':resource, 'type':'edit'})
        

    @method_decorator(login_required)
    @method_decorator(group_required('organizer'))
    def remove(self, request, resource_id):
        try:
            resource = ResourceModel.objects.get(id=resource_id, exists=True)
        except ResourceModel.DoesNotExist:
            messages.error(request, 'Resource no fount.')
            return HttpResponseRedirect(reverse('admin'))
        try:
            resource.delete()
            messages.success(request, _('Successfully removed resource.'))
        except Exception, e:
            raise(e)
            messages.error(request, _('Error removing resource.'))
        return HttpResponseRedirect(reverse('admin_event_see', kwargs={'event_id':resource.get_event().id}))