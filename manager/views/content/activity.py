from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.contrib import messages

from manager.forms.admin import ActivityForm
from manager.models import Activity as ActivityModel
from manager.utils.decorators import group_required

class Activity(object):
    def see(self, request, activity_id):
        try:
            activity = ActivityModel.objects.get(id=activity_id, exists=True)
            return render(request, 'manager/content/activity/see.html', {'activity': activity})
        except ActivityModel.DoesNotExist:
            messages.error(request, 'Activity no fount.')
            HttpResponseRedirect(reverse('admin'))