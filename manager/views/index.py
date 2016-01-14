from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required

from manager.models import Event
from manager.utils.decorators import group_required

class Index(object):
	
	def home(self, request):
		# return render(request, 'manager/index/home.html', {})
		return render(request, 'manager/screens/screen-event.html', {})
		
	def content(self, request):
		if request.user.groups.filter(name='organizer').exists():
			return HttpResponseRedirect(reverse('admin'))
		elif request.user.groups.filter(name='attendee').exists():
			events = Event.objects.filter(exists=True, active=True)
			return render(request, 'manager/index/home.html', {'events': events})
		else:
			return HttpResponseRedirect(reverse('login'))
			
	
	@method_decorator(login_required)
	@method_decorator(group_required('organizer'))
	def admin(self, request):
		events = Event.objects.filter(exists=True)
		return render(request, 'manager/index/admin.html', {'events': events})	

	def contact(self, request):
		return HttpResponse("contact")

	def about(self, request):
		return HttpResponse("about")