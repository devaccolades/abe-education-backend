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
    path('events/<slug:slug>', views.EventsViewset.as_view(), name='get_event_by_slug'),

    path('event-faq/', views.EventFaqViewset.as_view(), name='event-faq-list'),
    
    
    # Career URLs
    path('perks/', views.PerksView.as_view(), name='perks'),
    path('careers/', views.CareersViewset.as_view(), name='careers-list'),
    path('job-application/', views.JobApplicationPostAPIView.as_view(), name='job-application'),

    #Destination URLs
    path('destinations/', views.DestinationsView.as_view(), name='destinations'),
    path('destinations/<slug:slug>', views.DestinationsView.as_view(), name='get_destinations_by_slug'),

    path('destination-banner/', views.DestinationBannerView.as_view(), name='destination_banner'),
    path('destination-why-choose/', views.DestinationWhyChooseView.as_view(), name='destination_why_choose'),
    path('universities/', views.UniversityView.as_view(), name='universities'),
    path('life-as-student/', views.LifeAsStudentView.as_view(), name='life_as_student'),
    path('destination-faqs/', views.DestinationFaqView.as_view(), name='destination_faqs'),
    path('post-study/', views.PostStudyView.as_view(), name='post-study'),


    # #destinationVisa URLs
    path('visa-banner/', views.VisaBannerView.as_view(), name='visa_banner'),
    path('visa-documents/', views.VisaDocumentsView.as_view(), name='visa_documents'),
    path('visa-cards/', views.VisaCardsView.as_view(), name='visa_cards'),
    path('visa-your-obligations/', views.VisaYourObligationsView.as_view(), name='visa_your_obligations'),

    # #destinationScholarship URLs
    path('scholarship-banner/', views.ScholarshipBannerView.as_view(), name='scholarship_banner'),
    path('scholarship-cards/', views.ScholarshipCardsView.as_view(), name='scholarship_cards'),
    path('scholarships/', views.ScholarshipsView.as_view(), name='scholarships'),

    # #destinationCost of Study
    path('cost-of-study/', views.CostOfStudyView.as_view(), name='cost_of_study'),
    
    #Leads URLs
    path('event-registration/', views.EventRegistrationPostAPIView.as_view(), name='event_registration'), 
    path('get-expert-advice/', views.GetExpertAdvicePostAPIView.as_view(), name='get_expert_advice'),
    path('free-consultation/', views.FreeConsultationPostAPIView.as_view(), name='free_consultation'),
    path('specialization-enquiry/', views.SpecializationEnquiryPostAPIView.as_view(), name='specialization_enquiry'),
    path('university-enquiry/', views.UniversityEnquiryPostAPIView.as_view(), name='university_enquiry'),
    path('enrol-for-training/', views.EnrolForTrainingPostAPIView.as_view(), name='enrol_for_training'),
    path('training-contact/', views.TrainingContactPostAPIView.as_view(), name='training_contact'),

    #Training URLs
    path('training-evaluation/', views.TrainingEvaluationViewset.as_view(), name='training-evaluation'),
    path('exam-centres/', views.ExamCentresViewset.as_view(), name='exam-centres'),
    path('set-exam-centre/', views.SetExamCentreViewset.as_view(), name='set-exam-centre'),


]