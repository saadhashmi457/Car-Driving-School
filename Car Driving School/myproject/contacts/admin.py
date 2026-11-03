from django.contrib import admin
from contacts.models import contactsmodel

# Register your models here.

class contactsadmin(admin.ModelAdmin):
    list_display=("Name","Email","Message")
    
    
admin.site.register(contactsmodel,contactsadmin)
