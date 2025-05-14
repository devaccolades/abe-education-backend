from django.db import models

from core.models import *

# Create your models here.
class Destinations(BaseModel):
    destination = models.CharField(max_length=16, null=True, blank=True)
    flag_image = models.FileField(upload_to='destinations', blank=True, null=True)
    flag_alt = models.CharField(max_length=20, null=True, blank=True)
    meta_title = models.CharField(max_length=100, null=True, blank=True)
    meta_description = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'destination.destinations'
        verbose_name = 'Destinations'
        verbose_name_plural = 'a. Destinations'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Destinations {self.id}"
    
class DestinationBanner(BaseModel):
    destination = models.ForeignKey(Destinations, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=45, null=True, blank=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    image = models.FileField(upload_to='destination_banner', blank=True, null=True)
    image_alt = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'destination.destination_banner'
        verbose_name = 'Destination Banner'
        verbose_name_plural = 'b. Destination Banner'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Destination banner {self.id}"
    
class DestinationWhyChoose(BaseModel):
    destination = models.ForeignKey(Destinations, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    title_feature1 = models.CharField(max_length=50, null=True, blank=True)
    text_feature1 = models.CharField(max_length=250, null=True, blank=True)
    title_feature2 = models.CharField(max_length=50, null=True, blank=True)
    text_feature2 = models.CharField(max_length=250, null=True, blank=True)
    title_feature3 = models.CharField(max_length=50, null=True, blank=True)
    text_feature3 = models.CharField(max_length=250, null=True, blank=True)
    title_feature4 = models.CharField(max_length=50, null=True, blank=True)
    text_feature4 = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        db_table = 'destination.destination_why_choose'
        verbose_name = 'Destination Why Choose'
        verbose_name_plural = 'c. Destination Why Choose'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Destinations Why Choose {self.id}"
    
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
        verbose_name_plural = 'd. Universities'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Universities {self.id}" 
    
    
class LifeAsStudent(BaseModel):
    destination = models.ForeignKey(Destinations, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    image = models.FileField(upload_to='life_as', blank=True, null=True)
    image_alt = models.CharField(max_length=100, null=True, blank=True)
    
    
    class Meta:
        db_table = 'destination.life_as_student'
        verbose_name = 'Life As Student'
        verbose_name_plural = 'e. Life As Student'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Life As Student {self.id}" 
    
class DestinationFaq(BaseModel):
    destination = models.ForeignKey(Destinations, on_delete=models.CASCADE, null=True, blank=True)
    question = models.CharField(max_length=300, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'destination.destination_faq'
        verbose_name = 'Destination Faq'
        verbose_name_plural = 'f. Destination Faqs'
        ordering = ('-date_added',)


    def __str__(self):
        return self.question




#visa page


class VisaBanner(BaseModel):
    destination = models.ForeignKey(Destinations, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField( null=True, blank=True)

    class Meta:
        db_table = 'destination.visa_banner'
        verbose_name = 'Visa Banner'
        verbose_name_plural = 'g. Visa Banner'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Visa Banner {self.id}"
    
class VisaDocuments(BaseModel):
    destination = models.ForeignKey(Destinations, on_delete=models.CASCADE, null=True, blank=True)
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
        db_table = 'destination.visa_documents'
        verbose_name = 'Visa Documents Required'
        verbose_name_plural = 'h. Visa Documents Required'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Visa Documents Required {self.id}"
    
class VisaCards(BaseModel):
    destination = models.ForeignKey(Destinations, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=280, null=True, blank=True)

    class Meta:
        db_table = 'destination.visa_cards'
        verbose_name = 'Visa Cards'
        verbose_name_plural = 'i. Visa Cards'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Visa Cards {self.id}"
    
class VisaYourObligations(BaseModel):
    destination = models.ForeignKey(Destinations, on_delete=models.CASCADE, null=True, blank=True)
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
        verbose_name_plural = 'j. Visa Your Obligations'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Visa Your Obligations {self.id}"


#scholarship page
class ScholarshipBanner(BaseModel):
    destination = models.ForeignKey(Destinations, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField( null=True, blank=True)

    class Meta:
        db_table = 'destination.scholarship_banner'
        verbose_name = 'Scholarship Banner'
        verbose_name_plural = 'k. Scholarship Banner'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Scholarship Banner {self.id}" 
    

class ScholarshipCards(BaseModel):
    destination = models.ForeignKey(Destinations, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=280, null=True, blank=True)
    image = models.FileField(upload_to='scholarship', blank=True, null=True)
    image_alt = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'destination.scholarship_cards'
        verbose_name = 'Scholarship Cards'
        verbose_name_plural = 'l. Scholarship Cards'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Scholarship Cards {self.id}"    
    
class Scholarships(BaseModel):
    destination = models.ForeignKey(Destinations, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    university_name =models.CharField(max_length=100, null=True, blank=True)
    funding_type = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'destination.scholarships'
        verbose_name = 'Scholarships'
        verbose_name_plural = 'm. Scholarships'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Scholarships {self.id}"


class CostOfStudy(BaseModel):
    destination = models.ForeignKey(Destinations, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField( null=True, blank=True)

    page_title = models.CharField(max_length=255, default="Tuition Costs", null=True, blank=True)
    intro_paragraph = models.TextField()

    # Tuition Fees
    tuition_bachelor = models.CharField(max_length=255, null=True, blank=True)

    tuition_postgrad = models.CharField(max_length=255, null=True, blank=True)

    tuition_doctoral = models.CharField(max_length=255, null=True, blank=True)

    visa_fee = models.CharField(max_length=255, null=True, blank=True)

    # Accommodation Section
    accommodation_title = models.CharField(max_length=255, default="Accommodation Costs")
    accommodation_description = models.TextField()
    accommodation_image = models.ImageField(upload_to="cost_images/", blank=True, null=True)
    accommodation_image_alt = models.CharField(max_length=100, null=True, blank=True)

    # Living Expenses Section
    living_title = models.CharField(max_length=255, default="Living Expenses", blank=True, null=True)
    living_description = models.TextField()
    living_image = models.ImageField(upload_to="cost_images/", blank=True, null=True)
    living_image_alt = models.CharField(max_length=100, null=True, blank=True)

    # Living Expenses Details
    transport_cost = models.CharField(max_length=255, null=True, blank=True)
    entertainment_cost = models.CharField(max_length=255, null=True, blank=True)
    books_supplies_cost = models.CharField(max_length=255, null=True, blank=True)
    

    # Health Insurance
    health_title = models.CharField(max_length=255, default="Health Insurance", null=True, blank=True)
    health_description = models.TextField()
    health_image = models.ImageField(upload_to="cost_images/", blank=True, null=True)
    health_image_alt = models.CharField(max_length=100, null=True, blank=True)

    # Taxes
    tax_title = models.CharField(max_length=255, default="Taxes Involved")
    tax_description = models.TextField()
    tax_image = models.ImageField(upload_to="cost_images/", blank=True, null=True)
    tax_image_alt = models.CharField(max_length=100, null=True, blank=True)

    # Footer/Note
    footnote = models.TextField()


    class Meta:
        db_table = 'destination.cost_of_study'
        verbose_name = 'Cost Of Study '
        verbose_name_plural = 'n. Cost Of Study'
        ordering = ('-date_added',)


    def __str__(self):
        return f"Cost Of Study  {self.id}"
    


    

    