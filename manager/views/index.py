from django.shortcuts import render
from django.http import HttpResponse

class Index(object):
	
	def home(self, request):
		# return render(request, 'manager/index/home.html', {})
		return render(request, 'manager/screens/screen-event.html', {})
		
	def contact(self, request):
		return HttpResponse("contact")

	def about(self, request):
		return HttpResponse("about")