from rest_framework import serializers
from .models import *
# from destination.serializer import DestinationsSerializer


class SEOSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEO  
        fields = ['id', 'page', 'path', 'meta_title','meta_description']
        


class BlogSerializer(serializers.ModelSerializer):
    date_added = serializers.SerializerMethodField()
    class Meta:
        model = Blogs
        fields = ['id', 'title', 'type', 'meta_title', 'meta_description', 'image', 'image_alt', 'descriptions', 'slug', 'date_added']

    def get_date_added(self, obj):
        return obj.date_added.strftime("%d/%m/%Y")

class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = ['id', 'name', 'location','review_text','profile_picture','type','thumbnail','video', 'ratings','youtube_link']

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq  
        fields = ['id', 'question', 'answer']

class BranchDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchDetails
        fields = ['id', 'place', 'address', 'email', 'phone1', 'phone2', 'phone3', 'whatsapp1', 'whatsapp2', 'direction_url']

class HomeCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeCards
        fields = '__all__'

class FooterDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterDescription
        fields = ['id', 'description']

class BankDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankDetails
        fields = ['id', 'bank_name', 'bank_logo', 'bank_logo_alt']

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'title', 'image', 'image_alt', 'date_added']

class BankPropertyDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankPropertyDocuments
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class StudyLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyLevel
        fields = ['id', 'level_name']

class EventSerializer(serializers.ModelSerializer):
    study_destination = CountrySerializer(many=True, read_only=True)
    study_level = StudyLevelSerializer(many=True, read_only=True)

    class Meta:
        model = Events
        fields = ['id', 'title', 'description', 'start_date', 'end_date', 'start_time', 'end_time', 'location', 'services', 'study_destination', 'study_level', 'about_event', 'image', 'image_alt', 'card_image', 'card_image_alt', 'meta_title', 'meta_description', 'slug', ]

class EventFaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventFaq  
        fields = ['id', 'question', 'answer']

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'

class PopupFeaturedSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopupFeatured
        fields = '__all__'