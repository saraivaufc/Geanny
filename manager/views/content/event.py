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
    def see(self, request, event_id):
        try:
            event = EventModel.objects.get(id=event_id, exists=True)
            return render(request, 'manager/content/event/see.html', {'event': event})
        except EventModel.DoesNotExist:
            messages.error(request, 'Event no fount.')
            HttpResponseRedirect(reverse('content'))