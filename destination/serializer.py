from rest_framework import serializers
from .models import *
# from core.serializer import SpecializationSerializer



class DestinationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destinations
        fields = [
            'id', 'destination', 'flag_image', 'flag_alt', 'home_image', 'home_image_alt',
            'home_description', 'meta_title', 'meta_description', 'specialization_image',
            'specialization_image_alt', 'ug_description', 'pg_description',
            'diploma_description', 'slug', 'date_added', 
        ]


class DestinationBannerSerializer(serializers.ModelSerializer):
    destination_name = serializers.CharField(source='destination.destination', read_only=True)

    class Meta:
        model = DestinationBanner
        fields = [
            'id', 'destination', 'destination_name', 'title', 'description', 'image',
            'image_alt', 'why_choose', 'title_feature1', 'text_feature1',
            'title_feature2', 'text_feature2', 'title_feature3', 'text_feature3',
            'title_feature4', 'text_feature4', 'date_added',
        ]


class UniversitySerializer(serializers.ModelSerializer):
    destination_name = serializers.CharField(source='destination.destination', read_only=True)

    class Meta:
        model = University
        fields = [
            'id', 'destination', 'destination_name', 'university_name', 'image',
            'image_alt', 'location', 'students', 'ranking', 'date_added', 
        ]


class LifeAsStudentSerializer(serializers.ModelSerializer):
    destination_name = serializers.CharField(source='destination.destination', read_only=True)

    class Meta:
        model = LifeAsStudent
        fields = [
            'id', 'destination', 'destination_name', 'main_description',
            'card_title_1', 'card_content_1', 'card_image_1', 'image_alt_1',
            'card_title_2', 'card_content_2', 'card_image_2', 'image_alt_2',
            'card_title_3', 'card_content_3', 'card_image_3', 'image_alt_3',
            'post_study_description', 'post_title_1', 'post_description_1',
            'post_title_2', 'post_description_2', 'date_added',
        ]


class DestinationFaqSerializer(serializers.ModelSerializer):
    destination_name = serializers.CharField(source='destination.destination', read_only=True)

    class Meta:
        model = DestinationFaq
        fields = [
            'id', 'destination', 'destination_name', 'question', 'answer',
            'date_added',
        ]


class VisaBannerSerializer(serializers.ModelSerializer):
    destination_name = serializers.CharField(source='destination.destination', read_only=True)

    class Meta:
        model = VisaBanner
        fields = [
            'id', 'destination', 'destination_name', 'description',
            'document_1', 'document_2', 'document_3', 'document_4', 'document_5',
            'document_6', 'document_7', 'document_8', 'document_9', 'document_10',
            'document_11', 'date_added', 
        ]

    def validate(self, attrs):
        destination = attrs.get('destination') or getattr(self.instance, 'destination', None)
        if not destination:
            return attrs

        qs = VisaBanner.objects.filter(destination=destination)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise serializers.ValidationError({
                "destination": "A VisaBanner for this destination already exists."
            })

        return attrs


class VisaCardsSerializer(serializers.ModelSerializer):
    destination_name = serializers.CharField(source='destination.destination', read_only=True)

    class Meta:
        model = VisaCards
        fields = [
            'id', 'destination', 'destination_name', 'title', 'description',
            'date_added', 
        ]


class VisaYourObligationsSerializer(serializers.ModelSerializer):
    destination_name = serializers.CharField(source='destination.destination', read_only=True)

    class Meta:
        model = VisaYourObligations
        fields = [
            'id', 'destination', 'destination_name', 'description', 'image', 'image_alt',
            'content_1', 'content_2', 'content_3', 'content_4', 'content_5', 'content_6',
            'date_added', 
        ]


class ScholarshipBannerSerializer(serializers.ModelSerializer):
    destination_name = serializers.CharField(source='destination.destination', read_only=True)

    class Meta:
        model = ScholarshipBanner
        fields = [
            'id', 'destination', 'destination_name', 'description',
            'date_added', 
        ]


class ScholarshipCardsSerializer(serializers.ModelSerializer):
    destination_name = serializers.CharField(source='destination.destination', read_only=True)

    class Meta:
        model = ScholarshipCards
        fields = [
            'id', 'destination', 'destination_name',
            'title_1', 'description_1', 'image_1', 'image_alt_1',
            'title_2', 'description_2', 'image_2', 'image_alt_2',
            'date_added', 
        ]


class ScholarshipsSerializer(serializers.ModelSerializer):
    destination_name = serializers.CharField(source='destination.destination', read_only=True)

    class Meta:
        model = Scholarships
        fields = [
            'id', 'destination', 'destination_name', 'title', 'course',
            'university_name', 'funding_type', 'date_added',
        ]


class CostOfStudySerializer(serializers.ModelSerializer):
    destination_name = serializers.CharField(source='destination.destination', read_only=True)

    class Meta:
        model = CostOfStudy
        fields = [
            'id', 'destination', 'destination_name', 'description', 'page_title',
            'intro_paragraph', 'tuition_bachelor', 'tuition_postgrad', 'tuition_doctoral',
            'visa_fee', 'accommodation_title', 'accommodation_description',
            'accommodation_image', 'accommodation_image_alt', 'living_title',
            'living_description', 'living_image', 'living_image_alt',
            'transport_cost', 'entertainment_cost', 'books_supplies_cost',
            'health_title', 'health_description', 'health_image', 'health_image_alt',
            'tax_title', 'tax_description', 'tax_image', 'tax_image_alt',
            'footnote', 'date_added', 
        ]


class DestinationSpecializationSerializer(serializers.ModelSerializer):
    destination_name = serializers.CharField(source='destination.destination', read_only=True)
    # specialization_areas = SpecializationSerializer(many=True, read_only=True)
    

    class Meta:
        model = DestinationSpecialization
        fields = [
            'id', 'destination', 'destination_name', 'courses', 'description',
            'banner_image', 'banner_image_alt', 'specialization_areas',
            'benefits_description', 'benefits_image', 'benefits_image_alt',
            'benefit_1', 'benefit_2', 'benefit_3', 'benefit_4', 'benefit_5',
            'benefit_6', 'benefit_7', 'benefit_8', 'benefit_9', 'benefit_10',
            'date_added', 
        ]
        

    
    