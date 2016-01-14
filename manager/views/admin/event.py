from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.contrib import messages

from manager.forms import EventForm, AddressForm
from manager.models import Event as EventModel
from manager.utils.decorators import group_required

class Event(object):
    
    @method_decorator(login_required)
    @method_decorator(group_required('organizer'))
    def see_all(self, request):
        events = EventModel.objects.filter(exists=True)
        return render(request, 'manager/admin/event/see_all.html', {'events': events})

    @method_decorator(login_required)
    @method_decorator(group_required('organizer'))
    def see(self, request, event_id):
        try:
            event = EventModel.objects.get(id=event_id, exists=True)
            return render(request, 'manager/admin/event/see.html', {'event': event})
        except EventModel.DoesNotExist:
            messages.error(request, 'Event no fount.')
            HttpResponseRedirect(reverse('admin'))
            

    @method_decorator(login_required)
    @method_decorator(group_required('organizer'))
    def add(self, request):
        if request.method == "POST":
            form_address = AddressForm(request.POST, request.FILES, prefix='address')
            form_event = EventForm(request.POST, request.FILES, prefix='event')
            if form_address.is_valid() and form_event.is_valid():
                address = form_address.save()
                event = form_event.save(commit=False)
                event.address = address
                event.save()
                messages.success(request, _('Successfully added event'))
                return HttpResponseRedirect(reverse('admin'))
            else:
                messages.error(request,_('Error adding event.'))
        else:
            form_address = AddressForm(prefix='address')
            form_event = EventForm(prefix='event')
        return render(request, 'manager/admin/event/form.html', {'form_event': form_event, 'form_address': form_address, 'type':'add'})
    

    @method_decorator(login_required)
    @method_decorator(group_required('organizer'))
    def edit(self, request, event_id):
        try:
            event = EventModel.objects.get(id=event_id, exists=True)
        except EventModel.DoesNotExist:
            messages.error(request, 'Event no fount.')
            return HttpResponseRedirect(reverse('admin'))

        if request.method == 'POST':
            form_event = EventForm(request.POST, request.FILES, prefix='event', instance=event)
            form_address = AddressForm(request.POST, request.FILES, prefix='address', instance=event.get_address())
            if form_address.is_valid() and form_event.is_valid():
                address = form_address.save()
                event = form_event.save(commit=False)
                event.address = address
                event.save()
                messages.success(request, _('Successfully edited event'))
                return self.see(request, event.id)
                
            else:
                messages.error(request, _("Error when editing event"))
        else:
            form_address = AddressForm(prefix='address', instance=event.get_address())
            form_event = EventForm(prefix='event', instance=event)
        return render(request, 'manager/admin/event/form.html', {'form_event': form_event, 'form_address': form_address, 'event':event, 'type':'edit'})
        

    @method_decorator(login_required)
    @method_decorator(group_required('organizer'))
    def remove(self, request, event_id):
        try:
            event = EventModel.objects.get(id=event_id, exists=True)
        except EventModel.DoesNotExist:
            messages.error(request, 'Event no fount.')
            return HttpResponseRedirect(reverse('admin'))
        try:
            event.delete()
            messages.success(request, _('Successfully removed event.'))
        except:
            messages.error(request, _('Error removing event.'))
        return HttpResponseRedirect(reverse('admin'))