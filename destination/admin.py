from django.contrib import admin
from .models import *
from unfold.admin import ModelAdmin

# Register your models here.

@admin.register(Destinations)
class DestinationsAdmin(ModelAdmin):
    list_display = ('destination', 'flag_alt', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('destination',)
    list_filter = ('date_added', 'is_deleted')


@admin.register(DestinationBanner)
class DestinationBannerAdmin(ModelAdmin):
    list_display = ('title', 'image_alt', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('title',)
    list_filter = ('date_added', 'is_deleted')


@admin.register(DestinationWhyChoose)
class DestinationWhyChooseAdmin(ModelAdmin):
    list_display = ('description', 'title_feature1', 'title_feature2', 'title_feature3', 'title_feature4', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('description', 'title_feature1', 'title_feature2')
    list_filter = ('date_added', 'is_deleted')


@admin.register(University)
class UniversityAdmin(ModelAdmin):
    list_display = ('university_name', 'location', 'students', 'ranking', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('university_name', 'location')
    list_filter = ('date_added', 'is_deleted')


@admin.register(LifeAsStudent)
class LifeAsStudentAdmin(ModelAdmin):
    list_display = ('title', 'image_alt', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('title',)
    list_filter = ('date_added', 'is_deleted')


@admin.register(DestinationFaq)
class DestinationFaqAdmin(ModelAdmin):
    list_display = ('question', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('question',)
    list_filter = ('date_added', 'is_deleted')


@admin.register(VisaBanner)
class VisaBannerAdmin(ModelAdmin):
    list_display = ('destination', 'description', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('description',)
    list_filter = ('date_added', 'is_deleted')


@admin.register(VisaDocuments)
class VisaDocumentsAdmin(ModelAdmin):
    list_display = ('document_1', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('destination',)
    list_filter = ('date_added', 'is_deleted')


@admin.register(VisaCards)
class VisaCardsAdmin(ModelAdmin):
    list_display = ('title', 'description', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('title', 'description')
    list_filter = ('date_added', 'is_deleted')


@admin.register(VisaYourObligations)
class VisaYourObligationsAdmin(ModelAdmin):
    list_display = ('description', 'image_alt', 'content_1', 'content_3', 'content_5', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('description', 'content_1', 'content_3', 'content_5')
    list_filter = ('date_added', 'is_deleted')


@admin.register(ScholarshipBanner)
class ScholarshipBannerAdmin(ModelAdmin):
    list_display = ('description', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('description',)
    list_filter = ('date_added', 'is_deleted')


@admin.register(ScholarshipCards)
class ScholarshipCardsAdmin(ModelAdmin):
    list_display = ('title', 'image_alt', 'description', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('title', 'description')
    list_filter = ('date_added', 'is_deleted')


@admin.register(Scholarships)
class ScholarshipsAdmin(ModelAdmin):
    list_display = ('title', 'university_name', 'funding_type', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('title', 'university_name')
    list_filter = ('date_added', 'is_deleted')


@admin.register(CostOfStudy)
class CostOfStudyAdmin(ModelAdmin):
    list_display = ('page_title', 'tuition_bachelor', 'tuition_postgrad', 'tuition_doctoral', 'visa_fee', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('page_title', 'tuition_bachelor', 'tuition_postgrad')
    list_filter = ('date_added', 'is_deleted')