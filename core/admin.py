from django.contrib import admin
from .models import *
from unfold.admin import ModelAdmin



@admin.register(Blogs)
class BlogsAdmin(ModelAdmin):
    list_display = ('ordering_priority', 'title', 'slug', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('ordering_priority', 'title', 'slug', 'description')
    list_filter = ('date_added', 'is_deleted')
    prepopulated_fields = {'slug': ('title',)}

# @admin.register(Testimonials)
# class TestimonialAdmin(ModelAdmin):
#     search_fields = ('name', 'location', 'review_text')
#     list_filter = ('date_added', 'is_deleted')

@admin.register(Faq)
class FaqAdmin(ModelAdmin):
    search_fields = ('question',)
    list_filter = ('date_added', 'is_deleted')

@admin.register(SEO)
class SEOAdmin(ModelAdmin):
    list_display = ('page', 'path', 'meta_title', 'meta_description', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('page', 'path', 'meta_title')
    list_filter = ('date_added', 'is_deleted')

@admin.register(BranchDetails)
class BranchDetailsAdmin(ModelAdmin):
    list_display = ('place', 'address', 'email', 'phone1', 'whatsapp1', 'direction_url', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('place', 'address', 'email', 'phone1', 'whatsapp1')
    list_filter = ('date_added', 'is_deleted')

@admin.register(HomeCards)
class HomeCardsAdmin(ModelAdmin):
    list_display = ('title', 'subtitle', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('title', 'description', 'image_alt')
    list_filter = ('date_added', 'is_deleted')


@admin.register(FooterDescription)
class FooterDescriptionAdmin(ModelAdmin):
    list_display = ('description', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('description',)
    list_filter = ('date_added', 'is_deleted')


@admin.register(BankDetails)
class BankDetailsAdmin(ModelAdmin):
    list_display = ('bank_name', 'bank_logo_alt', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('bank_name',)
    list_filter = ('bank_name', 'date_added', 'is_deleted')
   

@admin.register(Gallery)
class GalleryAdmin(ModelAdmin):
    list_display = ( 'title', 'image_alt', 'image', 'date_added', 'is_deleted')
    search_fields = ('image_alt',)
    list_filter = ('date_added', 'is_deleted')

@admin.register(BankPropertyDocuments)
class BankPropertyDocumentsAdmin(ModelAdmin):
    list_display = ('list_content', 'date_added', 'date_updated')
    search_fields = ('list_content',)
    list_filter = ('date_added', 'is_deleted')

@admin.register(Country)
class CountryAdmin(ModelAdmin):
    list_display = ('country', 'flag_image', 'flag_alt',  'date_added', 'date_updated', 'is_deleted')
    search_fields = ('country', 'flag_alt')
    list_filter = ('date_added', 'is_deleted')

@admin.register(StudyLevel)
class StudyLevelAdmin(ModelAdmin):
    list_display = ('level_name', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('level_name',)
    list_filter = ('date_added', 'is_deleted')

@admin.register(Events)
class EventsAdmin(ModelAdmin):
    list_display = ('ordering_priority', 'title', 'start_date', 'end_date', 'location', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('ordering_priority', 'title', 'description', 'location')
    list_filter = ('date_added', 'is_deleted')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(EventFaq)
class EventFaqAdmin(ModelAdmin):
    search_fields = ('question',)
    list_filter = ('date_added', 'is_deleted')

@admin.register(Specialization)
class SpecializationAdmin(ModelAdmin):
    list_display = ('specialization_area', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('specialization_area',)
    list_filter = ('date_added', 'is_deleted')
   
@admin.register(PopupFeatured)
class PopupFeaturedAdmin(ModelAdmin):
    list_display = ('title', 'image', 'image_alt', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('title',)
    list_filter = ('date_added', 'is_deleted')