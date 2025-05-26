from django.contrib import admin
from .models import *
from unfold.admin import ModelAdmin


# Register your models here.
@admin.register(EventRegistrationForm)
class EventRegistrationFormAdmin(ModelAdmin):
    list_display = ('name', 'email', 'phone', 'event', 'nearest_office', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('name', 'email', 'phone', 'event')
    list_filter = ('date_added', 'is_deleted')

@admin.register(GetExpertAdviceForm)
class GetExpertAdviceFormAdmin(ModelAdmin):
    list_display = ('name', 'email', 'phone', 'preferred_course', 'preferred_intake', 'nearest_office', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('name', 'email', 'phone', 'preferred_course')
    list_filter = ('date_added', 'is_deleted')

@admin.register(FreeConsultationForm)
class FreeConsultationFormAdmin(ModelAdmin):
    list_display = ('name', 'email', 'phone', 'preferred_country', 'preferred_course', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('name', 'email', 'phone', 'preferred_country')
    list_filter = ('date_added', 'is_deleted')

@admin.register(SpecializationEnquiryForm)
class SpecializationEnquiryFormAdmin(ModelAdmin):
    list_display = ('name', 'email', 'phone', 'specialization', 'course', 'destination', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('name', 'email', 'phone', 'specialization', 'course')
    list_filter = ('date_added', 'is_deleted')

@admin.register(UniversityEnquiryForm)
class UniversityEnquiryFormAdmin(ModelAdmin):
    list_display = ('name', 'email', 'phone', 'university', 'destination', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('name', 'email', 'phone', 'university')
    list_filter = ('date_added', 'is_deleted')

@admin.register(EnrolForTrainingForm)
class EnrolForTrainingFormAdmin(ModelAdmin):
    list_display = ('name', 'email', 'phone', 'training_for', 'preferred_course', 'nearest_office', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('name', 'email', 'phone', 'training_for')
    list_filter = ('date_added', 'is_deleted')

@admin.register(TrainingContactForm)
class TrainingContactFormAdmin(ModelAdmin):
    list_display = ('name', 'email', 'phone', 'preferred_centre', 'training_type', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('name', 'email', 'phone', 'preferred_centre')
    list_filter = ('date_added', 'is_deleted')