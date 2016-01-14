from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.contrib import messages

from manager.forms.admin import EventForm
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
            form = EventForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, _('Successfully added event'))
                return HttpResponseRedirect(reverse('admin'))
            else:
                messages.error(request,_('Error adding event.'))
        else:
            form = EventForm()
        return render(request, 'manager/admin/event/form.html', {'form': form, 'type':'add'})
    

    @method_decorator(login_required)
    @method_decorator(group_required('organizer'))
    def edit(self, request, event_id):
        try:
            event = EventModel.objects.get(id=event_id, exists=True)
        except EventModel.DoesNotExist:
            messages.error(request, 'Event no fount.')
            return HttpResponseRedirect(reverse('admin'))

        if request.method == 'POST':
            form = EventForm(request.POST, request.FILES, instance=event)
            if form.is_valid():
                event = form.save()
                messages.success(request, _("Successfully edited event"))
                return self.see(request, event.id)
            else:
                messages.error(request, _("Error when editing event"))
        else:
            form = EventForm(instance=event)
        return render(request, 'manager/admin/event/form.html', {'form': form,'event':event, 'type':'edit'})
        

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