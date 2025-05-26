from rest_framework import serializers
from .models import *

class TrainingEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingEvaluation
        fields = '__all__'




class ExamCentresSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamCentres
        fields = '__all__'


class SetExamCentreSerializer(serializers.ModelSerializer):
    exam_centre = ExamCentresSerializer(many=True, read_only=True)

    class Meta:
        model = SetExamCentre
        fields = '__all__'