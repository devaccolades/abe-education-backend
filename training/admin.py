from django.contrib import admin
from .models import *
from unfold.admin import ModelAdmin

# Register your models here.
@admin.register(TrainingEvaluation)
class TrainingEvaluationAdmin(ModelAdmin):
    list_display = ('destination', 'training_type', 'points', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('destination', 'training_type', 'points',)
    list_filter = ('training_type', 'date_added', 'is_deleted')


@admin.register(ExamCentres)
class ExamCentresAdmin(ModelAdmin):
    list_display = ('centre_name', 'calender', 'location', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('centre_name', 'location', 'address')
    list_filter = ('calender', 'date_added', 'is_deleted')


@admin.register(SetExamCentre)
class SetExamCentreAdmin(ModelAdmin):
    list_display = ( 'traing_type', 'date_added', 'date_updated', 'is_deleted')
    search_fields = ('traing_type',)
    list_filter = ('date_added', 'is_deleted')