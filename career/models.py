from django.db import models

from core.models import *

# Create your models here.
CAREER_TYPE_CHOICES = (
    ('full_time', 'Full-time'),
    ('part_time', 'Part-time'),
    ('hybrid', 'Hybrid'),
    ('remote', 'Remote'),
    ('freelancer', 'Freelancer'),
)

class Careers(BaseModel):
    ordering_priority = models.PositiveIntegerField(default=0, blank=True, null=True, help_text="Order of the jobs for display purposes")
    job_title = models.CharField(max_length=300, blank=True, null=True)
    type = models.CharField(choices=CAREER_TYPE_CHOICES, max_length=255, blank=True, null=True)
    description =  models.TextField(blank=True, null=True, help_text="Job description")
    location1 = models.CharField(max_length=255, blank=True, null=True)
    location2 = models.CharField(max_length=100, null=True, blank=True)
    location3 = models.CharField(max_length=100, null=True, blank=True)
    location4 = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table='career.careers'
        verbose_name = ('Careers')
        verbose_name_plural = ('Careers')
        ordering = ('-date_added',)

    def __str__(self):
        return self.job_title if self.job_title else str(self.id)
    
class JobApplicationForm(BaseModel):
    name = models.CharField(max_length=255, blank=  True, null=True)
    position = models.CharField(blank=True, null=True, max_length=255)
    email = models.EmailField()
    number = models.PositiveBigIntegerField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    cv_file = models.FileField(upload_to='cvs/')

    class Meta:
        db_table = 'career.job_applications'
        verbose_name = ('Job Application')
        verbose_name_plural = ('Job Applications Enquiry')
        ordering = ('-date_added',)

    def __str__(self):
        return f"{self.name} - {self.position}"
    
class Perks(BaseModel):
    title = models.CharField(max_length=50, blank=True, null=True)
    description =  models.CharField(max_length=200, blank=True, null=True)
    gif = models.FileField(upload_to='perks/gif', null=True, blank=True)
    gif_alt = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table='career.perks'
        verbose_name = ('Perks')
        
        verbose_name_plural = ('Perks')
        ordering = ('-date_added',)

    def __str__(self):
        return self.title if self.title else str(self.id)