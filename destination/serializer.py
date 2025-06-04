from rest_framework import serializers
from .models import *

class DestinationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destinations
        fields = '__all__'


class DestinationBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationBanner
        fields = '__all__'


class DestinationWhyChooseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationWhyChoose
        fields = '__all__'

class PostStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostStudy
        fields = '__all__'
        
class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class LifeAsStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LifeAsStudent
        fields = '__all__'


class DestinationFaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationFaq
        fields = '__all__'


class VisaBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaBanner
        fields = '__all__'


class VisaDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaDocuments
        fields = '__all__'


class VisaCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaCards
        fields = '__all__'


class VisaYourObligationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaYourObligations
        fields = '__all__'


class ScholarshipBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScholarshipBanner
        fields = '__all__'


class ScholarshipCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScholarshipCards
        fields = '__all__'


class ScholarshipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scholarships
        fields = '__all__'


class CostOfStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = CostOfStudy
        fields = '__all__'

class DestinationSpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationSpecialization
        fields = '__all__'