from django.db import models
import uuid
from ckeditor.fields import RichTextField
from django.utils import timezone
from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Create your models here.



CAREER_TYPE_CHOICES = (
    ('full_time', 'Full-time'),
    ('part_time', 'Part-time'),
    ('hybrid', 'Hybrid'),
    ('remote', 'Remote'),
    ('freelancer', 'Freelancer'),
)

TESTIMONIALS_CHOICES = (
    ('text', 'text'),
    ('video', 'video'),
)


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(db_index=True, default=timezone.now, editable=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False, db_index=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.date_added:
            self.date_added = timezone.now()
        super(BaseModel, self).save(*args, **kwargs)


class SEO(BaseModel):
    page=models.CharField(max_length=200,blank=True,null=True)
    path=models.CharField(max_length=200)
    meta_title=models.TextField(blank=True,null=True)
    meta_description=models.TextField(blank=True,null=True)
    class Meta:
        db_table='core.seo'
        verbose_name = ('SEO')
        verbose_name_plural = ('SEO')
        ordering = ('date_added',)

    def __str__(self):
        return self.path if self.path else str(self.id)


BlogNews = (
    ('blog', 'Blog'),
    ('news', 'News'),
)
class Blogs(BaseModel):
    title = models.CharField(max_length=255)
    type = models.CharField(choices=BlogNews, max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='blogs')
    image_alt = models.CharField(max_length=255, blank=True, null=True)
    descriptions = RichTextField(blank=True, null=True)
    meta_title = models.CharField(max_length=300, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        db_table = 'core.blogs'
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ('-date_added',)

    def __str__(self):
        return self.title if self.title else str(self.id)


class Testimonials(BaseModel):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True, blank=True)
    review_text = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='testimonials/profile_pictures/', null=True, blank=True)
    profile_picture_alt = models.CharField(max_length=125, null=True, blank=True)
    type = models.CharField(choices=TESTIMONIALS_CHOICES, default='text', max_length=100)
    thumbnail = models.ImageField(upload_to='testimonials/thumbnail',blank=True,null=True)
    video = models.FileField(upload_to='testimonials/video',blank=True,null=True)
    video_alt = models.CharField(max_length=125, null=True, blank=True)
    ratings = models.FloatField(default=0, blank=True, null=True, help_text="Enter your rating out of 5. Leave blank if not applicable.")
    youtube_link = models.CharField(max_length=300, null=True, blank=True)

    class Meta:
        db_table = 'core.testimonials'
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Testimonial by {self.name} from {self.location}"

class Faq(BaseModel):
    question = models.CharField(max_length=300, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'core.faq'
        verbose_name = 'Faq'
        verbose_name_plural = 'Faqs'
        ordering = ('-date_added',)


    def __str__(self):
        return self.question
    
class BranchDetails(BaseModel):
    place = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone1 = models.CharField(max_length=255, blank=True, null=True)
    phone2 = models.CharField(max_length=255, blank=True, null=True)
    phone3 = models.CharField(max_length=255, blank=True, null=True)
    whatsapp1 = models.CharField(max_length=255, blank=True, null=True)
    whatsapp2 = models.CharField(max_length=255, blank=True, null=True)
    direction_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'core.branch_details'
        verbose_name = 'Branch Detail'
        verbose_name_plural = ' Branch Details'
        ordering = ('-date_added',)

    def __str__(self):
        return str(self.place) if self.place else str(self.id)
    

class HomeCards(BaseModel):
    title = models.CharField(max_length=16, null=True, blank=True)
    subtitle = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'core.home_cards'
        verbose_name = 'Home Cards'
        verbose_name_plural = 'Home Cards'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Home Card {self.id}"
    
    def clean(self):
        existing_cards = HomeCards.objects.exclude(id=self.id).count()
        if existing_cards >= 4:         
            raise ValidationError("Cannot create more than 4 Home Cards.")

    def save(self, *args, **kwargs):
       
        self.clean()
        super().save(*args, **kwargs)
    
class FooterDescription(BaseModel):
    description = models.CharField(max_length=160, null=True, blank=True)
    
    class Meta:
        db_table = 'core.footer_description'
        verbose_name = 'Footer Description'
        verbose_name_plural = 'Footer Description'
        ordering = ('-date_added',)

    def __str__(self):
        return f"Footer Description {self.id}"

    def clean(self):
        existing_cards = FooterDescription.objects.exclude(id=self.id).count()
        if existing_cards >= 1:         
            raise ValidationError("Cannot create more than 1 Footer Description.")

    def save(self, *args, **kwargs):
       
        self.clean()
        super().save(*args, **kwargs) 


class BankDetails(BaseModel):
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    bank_logo = models.FileField(upload_to='bank_details/images', blank=True, null=True)
    bank_logo_alt = models.CharField(max_length=125, null=True, blank=True)
    
    class Meta:
        db_table = 'core.bank_details'
        verbose_name = 'Bank Details'
        verbose_name_plural = 'Bank Details'
        ordering = ('-date_added',)

    def __str__(self):
        return f"Bank Details {self.id}"
    
class BankPropertyDocuments(BaseModel):
    list_content = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'core.BankPropertyDocuments'
        verbose_name = 'Bank Property Documents'
        verbose_name_plural = 'Bank Property Documents'
        ordering = ('-date_added',)

    def __str__(self):
        return str(self.id) if self.id else str(self.id)

class Gallery(BaseModel):
    image = models.FileField(upload_to='gallery/images', blank=True, null=True)
    image_alt = models.CharField(max_length=125, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'core.gallery'
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Gallery {self.id}"
   