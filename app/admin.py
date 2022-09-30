from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Meteric)
class MetericAdmin(admin.ModelAdmin):
    list_display=['id','metering_code','timestamp_utc']