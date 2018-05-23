from django.contrib import admin

# Register your models here.
from IcecastTracker333app.models import Channel, Server, Route

admin.site.register(Channel)
admin.site.register(Server)
admin.site.register(Route)