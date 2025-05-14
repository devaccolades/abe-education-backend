from rest_framework import serializers
from .models import *

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
        fields = ['id', 'title', 'subtitle', 'description', 'image', 'image_alt']

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