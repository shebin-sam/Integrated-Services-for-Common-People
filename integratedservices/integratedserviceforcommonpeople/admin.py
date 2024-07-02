from django.contrib import admin

# Register your models here.
from .models import Contact, Service

admin.site.register(Contact)
admin.site.register(Service)