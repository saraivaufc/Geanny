from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, login as login_user
from django.contrib.auth import logout as auth_logout


from manager.forms.accounts import LoginForm, RegisterForm, AttendeeRegisterForm, OrganizerRegisterForm
from manager.management.permissions import group_permissions
from manager.views.index import Index
from manager.models import RegisterKey, OrganizerKey


class Accounts(object):
    def __init__(self):
        self.index = Index()
    def login(self, request):
        try:
            if request.method == 'GET': next = request.GET['next']
            else:
                next = None
        except:
            next = None

        if request.user.is_authenticated():
            if next:
                return HttpResponseRedirect(next)
            else:
                return HttpResponseRedirect(reverse('home'))

        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                try:
                    login_user(request, user)
                    return HttpResponseRedirect(reverse('home'))
                except Exception, e:
                    messages.error(request, _("Username or password incorrect."))
            else:
                messages.error(request, _("Form no valid")) 
        else:
            form = LoginForm()
        return render(request, 'manager/accounts/login.html', {'form': form})

    def logout(self, request):
        try:
            auth_logout(request)
        except Exception, e:
            print e
        return HttpResponseRedirect(reverse('login'))

    def register(self, request):
        if request.method == 'POST':
            group = request.POST['group']
            if group in group_permissions:
                key = None
                if group == 'attendee':
                    form = AttendeeRegisterForm(request.POST, request.FILES)
                elif group == 'organizer':
                    form = OrganizerRegisterForm(request.POST, request.FILES)
                    if form.is_valid():
                        try:
                            key = OrganizerKey.objects.get(key=form.cleaned_data['key'], exists=True, in_use=False)
                        except OrganizerKey.DoesNotExist:
                            messages.error(request, _("Key no found"))
                            return render(request, 'manager/accounts/register.html', {'form': form})
                else:
                    messages.error(request, _("Group not found."))      

                if form.is_valid():
                    user = form.save(commit=False)
                    try:
                        user.set_password(user.password)
                        user.save(group=group)
                        if key:
                            key.add_user(user)
                        messages.success(request, _("User created success."))
                        return HttpResponseRedirect(reverse('login'))
                    except Exception, e:
                        print e
                        messages.error(request, _("Created user error."))
                else:
                    messages.error(request, _("Form no valid"))
            else:
                messages.error(request, _("Group not found."))
        else:
            form = RegisterForm()
        return render(request, 'manager/accounts/register.html', {'form': form})