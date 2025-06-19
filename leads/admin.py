from django.contrib import admin
from .models import *
from unfold.admin import ModelAdmin
from core.adminbase import BaseAdmin
from .resources import *

# Register your models here.
@admin.register(EventRegistrationForm)
class EventRegistrationFormAdmin(BaseAdmin):
    resource_class=EventsResource
    list_display = ('name', 'email', 'phone', 'event', 'nearest_office', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('name', 'email', 'phone', 'event')
    list_filter = ('date_added', 'is_deleted')

@admin.register(GetExpertAdviceForm)
class GetExpertAdviceFormAdmin(BaseAdmin):
    resource_class=GetExpertResource
    list_display = ('name', 'email', 'phone', 'preferred_course', 'preferred_country', 'nearest_office', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('name', 'email', 'phone', 'preferred_course')
    list_filter = ('date_added', 'is_deleted')

@admin.register(FreeConsultationForm)
class FreeConsultationFormAdmin(BaseAdmin):
    resource_class=FreeConsultationResource
    list_display = ('name', 'email', 'phone', 'preferred_country', 'preferred_course', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('name', 'email', 'phone', 'preferred_country')
    list_filter = ('date_added', 'is_deleted')

@admin.register(SpecializationEnquiryForm)
class SpecializationEnquiryFormAdmin(BaseAdmin):
    resource_class=SpecializationEnquiryResource
    list_display = ('name', 'email', 'phone', 'specialization', 'course', 'destination', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('name', 'email', 'phone', 'specialization', 'course')
    list_filter = ('date_added', 'is_deleted')

@admin.register(UniversityEnquiryForm)
class UniversityEnquiryFormAdmin(BaseAdmin):
    resource_class=UniversityEnquiryResource
    list_display = ('name', 'email', 'phone', 'university', 'destination', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('name', 'email', 'phone', 'university')
    list_filter = ('date_added', 'is_deleted')

@admin.register(EnrolForTrainingForm)
class EnrolForTrainingFormAdmin(BaseAdmin):
    resource_class=EnrolForTrainingResource
    list_display = ('name', 'email', 'phone', 'training_for', 'preferred_course', 'nearest_office', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('name', 'email', 'phone', 'training_for')
    list_filter = ('date_added', 'is_deleted')

@admin.register(TrainingContactForm)
class TrainingContactFormAdmin(BaseAdmin):
    resource_class=TrainingContactResource
    list_display = ('name', 'email', 'phone', 'preferred_centre', 'training_type', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('name', 'email', 'phone', 'preferred_centre')
    list_filter = ('date_added', 'is_deleted')

@admin.register(GetExpertCoachingForm)
class GetExpertCoachingFormAdmin(BaseAdmin):
    resource_class=GetExpertCoaching
    list_display = ('name', 'email', 'phone', 'preferred_country', 'preferred_time', 'mode_of_coaching', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('name', 'email', 'phone', 'preferred_country')
    list_filter = ('date_added', 'is_deleted')