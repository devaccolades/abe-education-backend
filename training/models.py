from django.db import models
from core.models import *
from destination.models import *

# Create your models here.
TRAINING_TYPE_CHOICES = (
    ('pte', 'PTE'),
    ('ielts', 'IELTS'),
    ('toefl', 'TOEFL'),
)

class ExamCentres(BaseModel):
    centre_name = models.CharField(max_length=255, null=True, blank=True)
    calender = models.DateField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    feature1 = models.CharField(max_length=200, null=True, blank=True)
    feature2 = models.CharField(max_length=200, null=True, blank=True)
    feature3 = models.CharField(max_length=200, null=True, blank=True)
    feature4 = models.CharField(max_length=200, null=True, blank=True)
    feature5 = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'training.exam_centres'
        verbose_name = 'Exam Centre'
        verbose_name_plural = 'Exam Centres'
        ordering = ('-date_added',)

    def __str__(self):
        return f"Exam Centre: {self.centre_name}"
    
class SetExamCentre(BaseModel):
    traing_type = models.CharField(max_length=10, choices=TRAINING_TYPE_CHOICES, null=True, blank=True)
    exam_centre = models.ManyToManyField(ExamCentres, blank=True, null=True)

    class Meta:
        db_table = 'training.set_exam_centre'
        verbose_name = 'Set Exam Centre'
        verbose_name_plural = 'Set Exam Centre'
        ordering = ('-date_added',)

    def __str__(self):
        return f"Set Exam Centre: {self.traing_type}"
    
class TrainingEvaluation(BaseModel):
    destination = models.ForeignKey(Destinations, on_delete=models.CASCADE, null=True, blank=True)
    points = models.TextField(blank=True, null=True)
    training_type = models.CharField(max_length=10, choices=TRAINING_TYPE_CHOICES, null=True, blank=True)   

    class Meta:
        db_table = 'training.training_evaluation'
        verbose_name = 'Training Evaluation'
        verbose_name_plural = 'Training Evaluation'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Training Evaluation: {self.points}"