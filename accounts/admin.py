from django.contrib import admin
from .models import User,EventUser,Organizer

admin.site.register(User)
admin.site.register(EventUser)
admin.site.register(Organizer)