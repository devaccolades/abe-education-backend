from rest_framework import serializers
from .models import *


class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Careers
        fields = '__all__'

class JobApplicationSerializer(serializers.ModelSerializer):
    date_added = serializers.SerializerMethodField()
    class Meta:
        model = JobApplicationForm  
        fields = '__all__'
        
    def get_date_added(self, obj):  
        return obj.date_added.strftime("%d/%m/%Y")
    
    
class PerksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perks 
        fields = '__all__'