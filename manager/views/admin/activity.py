from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.contrib import messages

from manager.forms import ActivityForm
from manager.models import Event as EventModel
from manager.models import Activity as ActivityModel
from manager.utils.decorators import group_required

class Activity(object):
    
    @method_decorator(login_required)
    @method_decorator(group_required('organizer'))
    def see(self, request, activity_id):
        try:
            activity = ActivityModel.objects.get(id=activity_id, exists=True)
            return render(request, 'manager/admin/activity/see.html', {'activity': activity})
        except ActivityModel.DoesNotExist:
            messages.error(request, 'Activity no fount.')
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
            form = ActivityForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, _('Successfully added activity.'))
                return HttpResponseRedirect(reverse('admin_event_see', kwargs={'event_id':event_id}))
            else:
                messages.error(request,_('Error adding activity.'))
        else:
            form = ActivityForm()
        return render(request, 'manager/admin/activity/form.html', {'form': form, 'event': event , 'type':'add'})
    

    @method_decorator(login_required)
    @method_decorator(group_required('organizer'))
    def edit(self, request, activity_id):
        try:
            activity = ActivityModel.objects.get(id=activity_id, exists=True)
        except ActivityModel.DoesNotExist:
            messages.error(request, 'Activity no fount.')
            return HttpResponseRedirect(reverse('admin'))

        if request.method == 'POST':
            request.POST = request.POST.copy()
            request.POST['event'] = activity.get_event().id
            form = ActivityForm(request.POST, request.FILES, instance=activity)
            if form.is_valid():
                activity = form.save()
                messages.success(request, _("Successfully edited activity"))
                return HttpResponseRedirect(reverse('admin_activity_see',kwargs={'activity_id':activity_id} ))
            else:
                messages.error(request, _("Error when editing activity"))
        else:
            form = ActivityForm(instance=activity)
        return render(request, 'manager/admin/activity/form.html', {'form': form,'activity':activity, 'type':'edit'})
        

    @method_decorator(login_required)
    @method_decorator(group_required('organizer'))
    def remove(self, request, activity_id):
        try:
            activity = ActivityModel.objects.get(id=activity_id, exists=True)
        except ActivityModel.DoesNotExist:
            messages.error(request, 'Activity no fount.')
            return HttpResponseRedirect(reverse('admin'))
        try:
            activity.delete()
            messages.success(request, _('Successfully removed activity.'))
        except Exception, e:
            raise(e)
            messages.error(request, _('Error removing activity.'))
        return HttpResponseRedirect(reverse('admin_event_see', kwargs={'event_id':activity.get_event().id}))