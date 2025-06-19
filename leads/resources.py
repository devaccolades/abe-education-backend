from import_export import resources, fields, widgets
from .models import *

# BASE_URL = "http://127.0.0.1:8000" 
BASE_URL="https://admin.abeedu.com/"

class EventsResource(resources.ModelResource):
    class Meta:
        model = EventRegistrationForm
        exclude = ['id', 'is_deleted', 'date_updated']


class GetExpertResource(resources.ModelResource):
    class Meta:
        model = GetExpertAdviceForm
        exclude = ['id', 'is_deleted', 'date_updated']


class GetExpertCoaching(resources.ModelResource):
    class Meta:
        model = GetExpertCoachingForm
        exclude = ['id', 'is_deleted', 'date_updated']

class FreeConsultationResource(resources.ModelResource):
    class Meta:
        model = FreeConsultationForm
        exclude = ['id', 'is_deleted', 'date_updated']

class SpecializationEnquiryResource(resources.ModelResource):
    class Meta:
        model = SpecializationEnquiryForm
        exclude = ['id', 'is_deleted', 'date_updated']

class UniversityEnquiryResource(resources.ModelResource):
    class Meta:
        model = UniversityEnquiryForm
        exclude = ['id', 'is_deleted', 'date_updated']

class EnrolForTrainingResource(resources.ModelResource):
    class Meta:
        model = EnrolForTrainingForm
        exclude = ['id', 'is_deleted', 'date_updated']

class TrainingContactResource(resources.ModelResource):
    class Meta:
        model = TrainingContactForm
        exclude = ['id', 'is_deleted', 'date_updated']

class ScholarshipEnquireResource(resources.ModelResource):
    class Meta:
        model = ScholarshipEnquireForm
        exclude = ['id', 'is_deleted', 'date_updated']
