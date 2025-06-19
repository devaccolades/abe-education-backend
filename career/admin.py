from django.contrib import admin

from .models import *
from unfold.admin import ModelAdmin
from core.adminbase import BaseAdmin
from .resources import JobApplicationFormResource

# Register your models here.
@admin.register(Careers)
class CareersAdmin(ModelAdmin):
    list_display = ('ordering_priority', 'job_title', 'type', 'location1', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('ordering_priority', 'job_title', 'type', 'location1')
    list_filter = ('date_added', 'is_deleted')


@admin.register(JobApplicationForm)
class JobApplicationAdmin(BaseAdmin):
    resource_class=JobApplicationFormResource
    list_display = ('name', 'position', 'email', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('name', 'position', 'email')
    list_filter = ('date_added', 'is_deleted')

@admin.register(Perks)
class Perks(ModelAdmin):
    list_display = ('title', 'date_added', 'date_updated')
    search_fields = ('title' ,)
    list_filter = ('date_added', 'is_deleted')