from django.contrib import admin
from .models import Region, CarbonRecord, Report

admin.site.register(Region)
admin.site.register(CarbonRecord)
admin.site.register(Report)