from django.contrib import admin
from .models import User,EventUser,Organizer

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','username', 'email', 'phone', 'user_type')


admin.site.register(User,UserAdmin)
admin.site.register(EventUser)
admin.site.register(Organizer)