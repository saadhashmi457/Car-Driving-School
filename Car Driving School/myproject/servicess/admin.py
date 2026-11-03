from django.contrib import admin
from servicess.models import servicemodel

# Register your models here.

class serviceadmin(admin.ModelAdmin):
    list_display=("Title","Detail")
    
admin.site.register(servicemodel,serviceadmin)
