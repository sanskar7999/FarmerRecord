from django.contrib import admin
from .models import Farm
# Register your models here.
@admin.register(Farm)
class farmAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name' , 'email' , 'phone' ,'tractor_brand' , 'model', 'tractor_implements'  )