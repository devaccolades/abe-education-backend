from django.db import models
from destination.models import *
from core.models import *


# Create your models here.

class EventRegistrationForm(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    nearest_office = models.CharField(max_length=100, blank=True, null=True)
    event = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'leads.eventregistrationform'
        verbose_name = 'Event Registration'
        verbose_name_plural = 'Event Registrations'
        ordering = ('-date_added',)

    def __str__(self):
        return str(self.name) if self.name else str(self.id)
 
class GetExpertAdviceForm(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=18, blank=True, null=True)
    preferred_country = models.CharField(max_length=100, null=True, blank=True)
    preferred_course = models.CharField(max_length=100, null=True, blank=True)
    nearest_office = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'leads.get_expert_advice_form'
        verbose_name = 'Get Expert Advice'
        verbose_name_plural = 'Contact Get Expert Advice'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Get Expert Advice by {self.name}"
    
class GetExpertCoachingForm(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=18, blank=True, null=True)
    preferred_country = models.CharField(max_length=100, null=True, blank=True)
    preferred_time = models.CharField(max_length=100, null=True, blank=True)
    mode_of_coaching = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'leads.get_expert_coaching_form'
        verbose_name = 'Home Get Expert Coaching'
        verbose_name_plural = 'Contact Get Expert Coaching'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Get Expert Coaching by {self.name}"
    
class FreeConsultationForm(BaseModel):
    name =  models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=18, blank=True, null=True)
    preferred_country = models.CharField(max_length=255, null=True, blank=True)
    preferred_course = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'leads.free_consultation_form'
        verbose_name = 'Free Consultation'
        verbose_name_plural = 'Free Consultation'
        ordering = ('-date_added',)


    def __str__(self):
        return f"free consultation - {self.name}"
    

class SpecializationEnquiryForm(BaseModel):
    name = name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    specialization = models.CharField(max_length=255, null=True, blank=True)
    course = models.CharField(max_length=255, null=True, blank=True)
    destination = models.CharField(max_length=255, null=True, blank=True)


    class Meta:
        db_table = 'leads.specialization_enquiry_form'
        verbose_name = 'Specialization Enquiry'
        verbose_name_plural = 'Specialization Enquiry'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Specialization Enquiry - {self.name}"
    

class UniversityEnquiryForm(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    university = models.CharField(max_length=255, null=True, blank=True)
    destination = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'leads.university_enquiry_form'
        verbose_name = 'University Enquiry'
        verbose_name_plural = 'University Enquiry'
        ordering = ('-date_added',)


    def __str__(self):
        return f"University Enquiry - {self.name}"
    

class ScholarshipEnquireForm(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    scholarship_title = models.CharField(max_length=255, null=True, blank=True)
    preferred_country = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'leads.scholarship_enquiry_form'
        verbose_name = 'Scholarship Enquiry'
        verbose_name_plural = 'Scholarship Enquiries'
        ordering = ('-date_added',)


    def __str__(self):
        return f"{self.name}"
    
#training
class EnrolForTrainingForm(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=18, blank=True, null=True)
    training_for = models.CharField(max_length=100, null=True, blank=True)
    preferred_course = models.CharField(max_length=100, null=True, blank=True)
    nearest_office = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'leads.enrol_for_training_form'
        verbose_name = 'Enrol For Training'
        verbose_name_plural = 'Enrol For Training'
        ordering = ('-date_added',)

    def __str__(self):
        return f"Enrol For Training by {self.name}"
    
class TrainingContactForm(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=18, blank=True, null=True)
    preferred_centre = models.CharField(max_length=100, null=True, blank=True)
    training_type = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        db_table = 'leads.training_contact_form'
        verbose_name = 'Training Contact'
        verbose_name_plural = 'Training Contact'
        ordering = ('-date_added',)

    def __str__(self):
        return f"Training Contact: {self.name}"
    

