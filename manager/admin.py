from django.contrib import admin

from .models import User, Attendee, Organizer, RegisterKey, OrganizerKey

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	pass
@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
	pass
@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
	pass
@admin.register(OrganizerKey)
class OrganizerKeyAdmin(admin.ModelAdmin):
	pass

