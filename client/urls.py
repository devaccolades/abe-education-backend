from django.urls import path
from .import views

urlpatterns = [
    path('seo/', views.SEOViewset.as_view(), name='seo-list'),
    path('blogs/', views.BlogsViewset.as_view(), name='blogs-list'),
    path('blogs/<slug:slug>', views.BlogsViewset.as_view(), name='get_blog_by_slug'),
    path('testimonials/', views.TestimonialsViewset.as_view(), name='testimonials-list'),
    path('faq/', views.FaqViewset.as_view(), name='faq-list'),
    path('branch-details/', views.BranchDetailsViewset.as_view(), name='branch-details-list'),
    path('home-cards/', views.HomeCardsViewset.as_view(), name='home-cards'),
    path('footer-description/', views.FooterDescriptionViewset.as_view(), name='footer-description'),
    path('bank-details/', views.BankDetailsViewset.as_view(), name='bank-details'),
    path('gallery/', views.GalleryViewset.as_view(), name='gallery-list'),
    path('bank-property-documents/', views.BankPropertyDocumentsView.as_view(), name='bank-property-documents'),
    path('countries/', views.CountryViewset.as_view(), name='countries-list'),
    path('study-level/', views.StudyLevelViewset.as_view(), name='study-level-list'),
    path('events/', views.EventsViewset.as_view(), name='events-list'),
    

    path('perks/', views.PerksView.as_view(), name='perks'),
    path('careers/', views.CareersViewset.as_view(), name='careers-list'),
    path('job-application/', views.JobApplicationPostAPIView.as_view(), name='job-application'),


    path('destinations/', views.DestinationsView.as_view(), name='destinations'),
    path('destination-banner/', views.DestinationBannerView.as_view(), name='destination_banner'),
    path('destination-why-choose/', views.DestinationWhyChooseView.as_view(), name='destination_why_choose'),
    path('universities/', views.UniversityView.as_view(), name='universities'),
    path('life-as-student/', views.LifeAsStudentView.as_view(), name='life_as_student'),
    path('destination-faqs/', views.DestinationFaqView.as_view(), name='destination_faqs'),

    # Visa URLs
    path('visa-banner/', views.VisaBannerView.as_view(), name='visa_banner'),
    path('visa-documents/', views.VisaDocumentsView.as_view(), name='visa_documents'),
    path('visa-cards/', views.VisaCardsView.as_view(), name='visa_cards'),
    path('visa-your-obligations/', views.VisaYourObligationsView.as_view(), name='visa_your_obligations'),

    # Scholarship URLs
    path('scholarship-banner/', views.ScholarshipBannerView.as_view(), name='scholarship_banner'),
    path('scholarship-cards/', views.ScholarshipCardsView.as_view(), name='scholarship_cards'),
    path('scholarships/', views.ScholarshipsView.as_view(), name='scholarships'),

    # Cost of Study
    path('cost-of-study/', views.CostOfStudyView.as_view(), name='cost_of_study'),
    
     

]