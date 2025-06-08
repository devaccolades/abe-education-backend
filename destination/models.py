from django.db import models

from core.models import *

# Create your models here.
class Destinations(BaseModel):
    destination = models.CharField(max_length=16, null=True, blank=True)
    flag_image = models.FileField(upload_to='destinations', blank=True, null=True)
    flag_alt = models.CharField(max_length=20, null=True, blank=True)
    home_image = models.FileField(upload_to='destinations', blank=True, null=True)
    home_image_alt = models.CharField(max_length=20, null=True, blank=True)
    home_description = models.CharField(max_length=260, null=True, blank=True)
    meta_title = models.CharField(max_length=100, null=True, blank=True)
    meta_description = models.CharField(max_length=200, null=True, blank=True)
    specialization_image = models.FileField(upload_to='destinations', blank=True, null=True)
    specialization_image_alt = models.CharField(max_length=20, null=True, blank=True)
    ug_description = models.CharField(max_length=260, null=True, blank=True)
    pg_description = models.CharField(max_length=260, null=True, blank=True)
    diploma_description = models.CharField(max_length=260, null=True, blank=True)
    slug = models.SlugField(max_length=200, default='destination', null=True, blank=True)

    class Meta:
        db_table = 'destination.destinations'
        verbose_name = 'Destinations'
        verbose_name_plural = 'a. Destinations'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Destinations {self.destination}"
    
class DestinationBanner(BaseModel):
    destination = models.OneToOneField(Destinations, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=45, null=True, blank=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    image = models.FileField(upload_to='destination_banner', blank=True, null=True)
    image_alt = models.CharField(max_length=100, null=True, blank=True)
    why_choose = models.CharField(max_length=200, null=True, blank=True)
    title_feature1 = models.CharField(max_length=50, null=True, blank=True)
    text_feature1 = models.CharField(max_length=250, null=True, blank=True)
    title_feature2 = models.CharField(max_length=50, null=True, blank=True)
    text_feature2 = models.CharField(max_length=250, null=True, blank=True)
    title_feature3 = models.CharField(max_length=50, null=True, blank=True)
    text_feature3 = models.CharField(max_length=250, null=True, blank=True)
    title_feature4 = models.CharField(max_length=50, null=True, blank=True)
    text_feature4 = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        db_table = 'destination.destination_banner'
        verbose_name = 'Destination Banner'
        verbose_name_plural = 'b. Destination Banner'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Destination banner {self.title}"
    
# class DestinationWhyChoose(BaseModel):
#     destination = models.ForeignKey(Destinations, on_delete=models.CASCADE, null=True, blank=True)
#     description = models.CharField(max_length=200, null=True, blank=True)
#     title_feature1 = models.CharField(max_length=50, null=True, blank=True)
#     text_feature1 = models.CharField(max_length=250, null=True, blank=True)
#     title_feature2 = models.CharField(max_length=50, null=True, blank=True)
#     text_feature2 = models.CharField(max_length=250, null=True, blank=True)
#     title_feature3 = models.CharField(max_length=50, null=True, blank=True)
#     text_feature3 = models.CharField(max_length=250, null=True, blank=True)
#     title_feature4 = models.CharField(max_length=50, null=True, blank=True)
#     text_feature4 = models.CharField(max_length=250, null=True, blank=True)

#     class Meta:
#         db_table = 'destination.destination_why_choose'
#         verbose_name = 'Destination Why Choose'
#         verbose_name_plural = 'c. Destination Why Choose'
#         ordering = ('-date_added',)


#     def __str__(self):
#         return f"Destinations Why Choose {self.destination}"
    
# class PostStudy(BaseModel):
#     destination = models.ForeignKey(Destinations, on_delete=models.CASCADE, null=True, blank=True)
#     description = models.CharField(max_length=250, null=True, blank=True)
#     title_1 = models.CharField(max_length=40, null=True, blank=True)
#     description_1 = models.CharField(max_length=250, null=True, blank=True)
#     title_2 = models.CharField(max_length=40, null=True, blank=True)
#     description_2 = models.CharField(max_length=250, null=True, blank=True)

#     class Meta:
#         db_table = 'destination.post_study'
#         verbose_name = 'Post Study'
#         verbose_name_plural = 'd. Post Study'
#         ordering = ('-date_added',)


#     def __str__(self):
#         return f"Post Study {self.destination}"
    
class University(BaseModel):
    destination = models.ForeignKey(Destinations, on_delete=models.CASCADE, null=True, blank=True)
    university_name = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(upload_to='university', blank=True, null=True)
    image_alt = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    students = models.CharField(max_length=100, null=True, blank=True)
    ranking = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'destination.university'
        verbose_name = ' University'
        verbose_name_plural = 'c. Universities'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Universities {self.university_name}" 
    
    
class LifeAsStudent(BaseModel):
    destination = models.OneToOneField(Destinations, on_delete=models.CASCADE, null=True, blank=True)
    main_description = models.CharField(max_length=250, null=True, blank=True)

    card_title_1 = models.CharField(max_length=40, null=True, blank=True)
    card_content_1 = models.CharField(max_length=250, null=True, blank=True)
    card_image_1 = models.FileField(upload_to='life_as', blank=True, null=True)
    image_alt_1 = models.CharField(max_length=100, null=True, blank=True)

    card_title_2 = models.CharField(max_length=40, null=True, blank=True)
    card_content_2 = models.CharField(max_length=250, null=True, blank=True)
    card_image_2 = models.FileField(upload_to='life_as', blank=True, null=True)
    image_alt_2 = models.CharField(max_length=100, null=True, blank=True)

    card_title_3 = models.CharField(max_length=40, null=True, blank=True)
    card_content_3 = models.CharField(max_length=250, null=True, blank=True)
    card_image_3 = models.FileField(upload_to='life_as', blank=True, null=True)
    image_alt_3 = models.CharField(max_length=100, null=True, blank=True)

    post_study_description = models.CharField(max_length=250, null=True, blank=True)
    post_title_1 = models.CharField(max_length=40, null=True, blank=True)
    post_description_1 = models.CharField(max_length=250, null=True, blank=True)
    post_title_2 = models.CharField(max_length=40, null=True, blank=True)
    post_description_2 = models.CharField(max_length=250, null=True, blank=True)
    
    class Meta:
        db_table = 'destination.life_as_student'
        verbose_name = 'Life As Student'
        verbose_name_plural = 'd. Life As Student'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Life As Student {self.card_title_1}" 
    
class DestinationFaq(BaseModel):
    destination = models.ForeignKey(Destinations, on_delete=models.CASCADE, null=True, blank=True)
    question = models.CharField(max_length=300, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'destination.destination_faq'
        verbose_name = 'Destination Faq'
        verbose_name_plural = 'e. Destination Faqs'
        ordering = ('-date_added',)


    def __str__(self):
        return self.question




#visa page


class VisaBanner(BaseModel):
    destination = models.OneToOneField(Destinations, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField( null=True, blank=True)
    document_1 = models.CharField(max_length=255, null=True, blank=True)
    document_2 = models.CharField(max_length=255, null=True, blank=True)
    document_3 = models.CharField(max_length=255, null=True, blank=True)
    document_4 = models.CharField(max_length=255, null=True, blank=True)
    document_5 = models.CharField(max_length=255, null=True, blank=True)
    document_6 = models.CharField(max_length=255, null=True, blank=True)
    document_7 = models.CharField(max_length=255, null=True, blank=True)
    document_8 = models.CharField(max_length=255, null=True, blank=True)
    document_9 = models.CharField(max_length=255, null=True, blank=True)
    document_10 = models.CharField(max_length=255, null=True, blank=True)
    document_11 = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'destination.visa_banner'
        verbose_name = 'Visa Banner'
        verbose_name_plural = 'f. Visa Banner'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Visa Banner {self.id}"
    
# class VisaDocuments(BaseModel):
#     destination = models.ForeignKey(Destinations, on_delete=models.CASCADE, null=True, blank=True)
#     document_1 = models.CharField(max_length=255, null=True, blank=True)
#     document_2 = models.CharField(max_length=255, null=True, blank=True)
#     document_3 = models.CharField(max_length=255, null=True, blank=True)
#     document_4 = models.CharField(max_length=255, null=True, blank=True)
#     document_5 = models.CharField(max_length=255, null=True, blank=True)
#     document_6 = models.CharField(max_length=255, null=True, blank=True)
#     document_7 = models.CharField(max_length=255, null=True, blank=True)
#     document_8 = models.CharField(max_length=255, null=True, blank=True)
#     document_9 = models.CharField(max_length=255, null=True, blank=True)
#     document_10 = models.CharField(max_length=255, null=True, blank=True)
#     document_11 = models.CharField(max_length=255, null=True, blank=True)
    

#     class Meta:
#         db_table = 'destination.visa_documents'
#         verbose_name = 'Visa Documents Required'
#         verbose_name_plural = 'i. Visa Documents Required'
#         ordering = ('-date_added',)


#     def __str__(self):
#         return f"Visa Documents Required {self.destination}"
    
class VisaCards(BaseModel):
    destination = models.ForeignKey(Destinations, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=280, null=True, blank=True)

    class Meta:
        db_table = 'destination.visa_cards'
        verbose_name = 'Visa Cards'
        verbose_name_plural = 'g. Visa Cards'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Visa Cards {self.title}"
    
class VisaYourObligations(BaseModel):
    destination = models.OneToOneField(Destinations, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    image = models.FileField(upload_to='visa', blank=True, null=True)
    image_alt = models.CharField(max_length=100, null=True, blank=True)
    content_1 = models.CharField(max_length=50, null=True, blank=True)
    content_2 = models.CharField(max_length=250, null=True, blank=True)
    content_3 = models.CharField(max_length=50, null=True, blank=True)
    content_4 = models.CharField(max_length=250, null=True, blank=True)
    content_5 = models.CharField(max_length=50, null=True, blank=True)
    content_6 = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        db_table = 'destination.visa_your_obligations'
        verbose_name = 'Visa Your Obligations'
        verbose_name_plural = 'h. Visa Your Obligations'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Visa Your Obligations {self.destination}"


#scholarship page
class ScholarshipBanner(BaseModel):
    destination = models.OneToOneField(Destinations, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField( null=True, blank=True)

    class Meta:
        db_table = 'destination.scholarship_banner'
        verbose_name = 'Scholarship Banner'
        verbose_name_plural = 'i. Scholarship Banner'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Scholarship Banner {self.destination}" 
    

class ScholarshipCards(BaseModel):
    destination = models.OneToOneField(Destinations, on_delete=models.CASCADE, null=True, blank=True)
    title_1 = models.CharField(max_length=75, null=True, blank=True)
    description_1 =  models.TextField(null=True, blank=True)
    image_1 = models.FileField(upload_to='scholarship', blank=True, null=True)
    image_alt_1 = models.CharField(max_length=100, null=True, blank=True)
    title_2 = models.CharField(max_length=75, null=True, blank=True)
    description_2 = models.TextField(null=True, blank=True)
    image_2 = models.FileField(upload_to='scholarship', blank=True, null=True)
    image_alt_2 = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'destination.scholarship_cards'
        verbose_name = 'Scholarship Cards'
        verbose_name_plural = 'j. Scholarship Cards'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Scholarship Cards {self.title_1}"    
    
class Scholarships(BaseModel):
    destination = models.ForeignKey(Destinations, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    university_name =models.CharField(max_length=100, null=True, blank=True)
    funding_type = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'destination.scholarships'
        verbose_name = 'Scholarships'
        verbose_name_plural = 'k. Scholarships'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Scholarships {self.title}"


class CostOfStudy(BaseModel):
    destination = models.OneToOneField(Destinations, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField( null=True, blank=True)

    page_title = models.CharField(max_length=255, default="Tuition Costs", null=True, blank=True)
    intro_paragraph = models.TextField(blank=True, null=True)

    # Tuition Fees
    tuition_bachelor = models.CharField(max_length=255, null=True, blank=True)
    tuition_postgrad = models.CharField(max_length=255, null=True, blank=True)
    tuition_doctoral = models.CharField(max_length=255, null=True, blank=True)
    visa_fee = models.CharField(max_length=255, null=True, blank=True)

    # Accommodation Section
    accommodation_title = models.CharField(max_length=255, default="Accommodation Costs")
    accommodation_description = models.TextField(blank=True, null=True)
    accommodation_image = models.ImageField(upload_to="cost_images/", blank=True, null=True)
    accommodation_image_alt = models.CharField(max_length=100, null=True, blank=True)

    # Living Expenses Section
    living_title = models.CharField(max_length=255, default="Living Expenses", blank=True, null=True)
    living_description = models.TextField(blank=True, null=True)
    living_image = models.ImageField(upload_to="cost_images/", blank=True, null=True)
    living_image_alt = models.CharField(max_length=100, null=True, blank=True)

    # Living Expenses Details
    transport_cost = models.CharField(max_length=255, null=True, blank=True)
    entertainment_cost = models.CharField(max_length=255, null=True, blank=True)
    books_supplies_cost = models.CharField(max_length=255, null=True, blank=True)
    

    # Health Insurance
    health_title = models.CharField(max_length=255, default="Health Insurance", null=True, blank=True)
    health_description = models.TextField(blank=True, null=True)
    health_image = models.ImageField(upload_to="cost_images/", blank=True, null=True)
    health_image_alt = models.CharField(max_length=100, null=True, blank=True)

    # Taxes
    tax_title = models.CharField(max_length=255, default="Taxes Involved")
    tax_description = models.TextField(blank=True, null=True)
    tax_image = models.ImageField(upload_to="cost_images/", blank=True, null=True)
    tax_image_alt = models.CharField(max_length=100, null=True, blank=True)

    # Footer/Note
    footnote = models.TextField(blank=True, null=True)


    class Meta:
        db_table = 'destination.cost_of_study'
        verbose_name = 'Cost Of Study '
        verbose_name_plural = 'l. Cost Of Study'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Cost Of Study  {self.id}"
    


#specialization page

COURSE_CHOICES = (
    ('Diploma', 'Diploma'),
    ('Undergraduate', 'Undergraduate'),
    ('Postgraduate', 'Postgraduate'),
)

class DestinationSpecialization(BaseModel):
    destination = models.OneToOneField(Destinations, on_delete=models.CASCADE, null=True, blank=True)
    courses = models.CharField(choices=COURSE_CHOICES, max_length=255, null=True, blank=True)
    description = models.TextField( null=True, blank=True)
    banner_image = models.FileField(upload_to='specialization', blank=True, null=True)
    banner_image_alt = models.CharField(max_length=100, null=True, blank=True)
    specialization_areas = models.ManyToManyField(Specialization, blank=True)

    benefits_description = models.CharField(max_length=180, null=True, blank=True)
    benefits_image = models.FileField(upload_to='specialization', blank=True, null=True)
    benefits_image_alt = models.CharField(max_length=100, null=True, blank=True)
    benefit_1 = models.CharField(max_length=200, null=True, blank=True)
    benefit_2 = models.CharField(max_length=200, null=True, blank=True)
    benefit_3 = models.CharField(max_length=200, null=True, blank=True)
    benefit_4 = models.CharField(max_length=200, null=True, blank=True)
    benefit_5 = models.CharField(max_length=200, null=True, blank=True)
    benefit_6 = models.CharField(max_length=200, null=True, blank=True)
    benefit_7 = models.CharField(max_length=200, null=True, blank=True)
    benefit_8 = models.CharField(max_length=200, null=True, blank=True)
    benefit_9 = models.CharField(max_length=200, null=True, blank=True)
    benefit_10 = models.CharField(max_length=200, null=True, blank=True)
    

    class Meta:
        db_table = 'destination.destination_specialization'
        verbose_name = 'Destination Specialization'
        verbose_name_plural = 'm. Destination Specialization'
        ordering = ('-date_added',)

    def __str__(self):
        return f"Destination Specialization {self.destination} - {self.courses}"
    

    