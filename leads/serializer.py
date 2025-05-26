from rest_framework import serializers
from .models import *




class EventRegistrationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRegistrationForm
        fields = '__all__'

class GetExpertAdviceFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetExpertAdviceForm
        fields = '__all__'

class FreeConsultationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeConsultationForm
        fields = '__all__'

class SpecializationEnquiryFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecializationEnquiryForm
        fields = '__all__'

class UniversityEnquiryFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityEnquiryForm
        fields = '__all__'

class EnrolForTrainingFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrolForTrainingForm
        fields = '__all__'

class TrainingContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingContactForm
        fields = '__all__'