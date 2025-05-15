from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
import os
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework.pagination import PageNumberPagination

from core import models as core_models
from core import serializer as core_serializer

from destination import models as destination_models
from destination import serializer as destination_serializer

from leads import models as leads_models
# from leads import serializer as leads_serializer

from career import models as careers_models
from career import serializer as careers_serializer





import logging

logger = logging.getLogger(__name__)

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size' 
    max_page_size = 50

class BlogsViewset(APIView):
    
    """
    API view for fetching Blog and Blog Details for users with pagination.
    """
    pagination_class = CustomPageNumberPagination
    model = core_models.Blogs
    serializers_class = core_serializer.BlogSerializer

    def get(self, request, slug = None):
        try:
            if slug:
                instance = self.get_object(slug)
                if not instance:
                    return Response({
                        "StatusCode": 6002,
                        "details": "Error",
                        "message": "Blog not found",
                    }, status=status.HTTP_404_NOT_FOUND)

                serializer = core_serializer.BlogSerializer(
                    instance, 
                    context={'request': request}
                )

                related_blogs = self.model.objects.filter(is_deleted=False).exclude(slug=slug)[:3]
                related_serializer = core_serializer.BlogSerializer(
                    related_blogs, 
                    many=True,
                    context={'request': request}
                )
                response_data = {
                    "StatusCode": 6000,
                    "details": "Success",
                    "data": serializer.data,
                    "related_blogs": related_serializer.data,
                    "message": "Blog details retrieved successfully"
                }
                return Response(response_data, status=status.HTTP_200_OK)

            queryset = self.model.objects.filter(is_deleted=False)
            paginator = self.pagination_class()
            page = paginator.paginate_queryset(queryset, request)

            serializer = self.serializers_class(
                    page, 
                    many=True, 
                    context={'request': request}
                )

            response_data = {
                "StatusCode" : 6000,
                "details" : "Success",
                "data" : serializer.data,
                "pagination": {
                        "total_items": paginator.page.paginator.count,
                        "total_pages": paginator.page.paginator.num_pages,
                        "current_page": paginator.page.number,
                        "next": paginator.get_next_link(),
                        "previous": paginator.get_previous_link()
                    },
                "message" : "Blog's data fetched successfully"
            }
            return Response(response_data,status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error retrieving Blog's: {str(e)}")
            return Response({
                "StatusCode": 6002,
                "api": request.get_full_path(),
                "details": "Error",
                "message": "Failed to retrieve Blog's",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def get_object(self, slug):
        try:
            return self.model.objects.filter(slug=slug).first()
        except Exception as e:
            logger.error(f"Error retrieving object: {str(e)}")
            return None
        

class SEOViewset(APIView):
    """
    Get Seo details for user side
    """
    model = core_models.SEO
    serializer_class = core_serializer.SEOSerializer

    def get(self, request):
        path = request.query_params.get('path', None)
        try:
            if path:
                queryset = self.model.objects.filter(path=path).first()
                serializer = self.serializer_class(queryset,context={'request': request})
            else:
                queryset = self.model.objects.filter(is_deleted=False)
                serializer = self.serializer_class(queryset, many=True, context={'request': request})

            response_data = {
                "StatusCode": 6000,
                "detail": "Success",
                "data": serializer.data,
                "message": "SEO's Data fetched successfully"
            }
            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f"Error fetching SEO details: {str(e)}")
            response_data = {
                "StatusCode": 6002,
                "detail": "Error",
                "data": "",
                "message": f"Something went wrong: {str(e)}"
            }
            return Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
class TestimonialsViewset(APIView):
    serializer_class = core_serializer.TestimonialsSerializer
    
    def get(self, request):
        try:
            data = core_models.Testimonials.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
            
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class FaqViewset(APIView):
    serializer_class = core_serializer.FaqSerializer 

    def get(self, request):
        try:
            data = core_models.Faq.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
            
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BranchDetailsViewset(APIView):
    serializer_class = core_serializer.BranchDetailsSerializer

    def get(self, request):
        try:
            data = core_models.BranchDetails.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class HomeCardsViewset(APIView):
    serializer_class = core_serializer.HomeCardsSerializer

    def get(self, request):
        try:
            data = core_models.HomeCards.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FooterDescriptionViewset(APIView):
    serializer_class = core_serializer.FooterDescriptionSerializer

    def get(self, request):
        try:
            data = core_models.FooterDescription.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BankDetailsViewset(APIView):
    serializer_class = core_serializer.BankDetailsSerializer

    def get(self, request):
        try:
            data = core_models.BankDetails.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GalleryViewset(APIView):
    serializer_class = core_serializer.GallerySerializer

    def get(self, request):
        try:
            data = core_models.Gallery.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
class BankPropertyDocumentsView(APIView):
    serializer_class = core_serializer.BankPropertyDocumentsSerializer

    def get(self, request):
        try:
            data = core_models.BankPropertyDocuments.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CountryViewset(APIView):
    serializer_class = core_serializer.CountrySerializer

    def get(self, request):
        try:
            data = core_models.Country.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class StudyLevelViewset(APIView):
    serializer_class = core_serializer.StudyLevelSerializer

    def get(self, request):
        try:
            data = core_models.StudyLevel.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
class EventsViewset(APIView):
    serializer_class = core_serializer.EventSerializer
    def get(self, request):
        try:
            data = core_models.Events.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
#careers
class CareersViewset(APIView):
    serializer_class = careers_serializer.CareerSerializer

    def get(self, request):
        try:
            data = careers_models.Careers.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class JobApplicationPostAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request):
        try:
            print(request.data, "checking the data")
            serializer = careers_serializer.JobApplicationSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                instance = serializer.save()

                context = {
                    'job_name': instance.position,
                    'name': instance.name,
                    'email': instance.email,
                    'number': instance.number,
                    'location': instance.location,
                    'date_added': instance.date_added,
                }

                html_content = get_template('JobApplication.html').render(context)
                subject = 'Enquiry for abe-education'
                from_email = settings.EMAIL_HOST_USER
                to_email = ['manjima.accolades@gmail.com']

                msg = EmailMultiAlternatives(subject, '', from_email, to_email)
                msg.attach_alternative(html_content, "text/html")

                
                if instance.cv_file:
                    cv_path = instance.cv_file.path
                    msg.attach_file(cv_path)


                # Send the email
                msg.send()

                response_data = {
                    "StatusCode": 6001,
                    "detail": "success",
                    "data": serializer.data,
                    "message": "Job Application successfully"
                }
            else:
                response_data = {
                    "StatusCode": 6002,
                    "detail": "validation error",
                    "data": serializer.errors,
                    "message": "Invalid data"
                }

        except Exception as e:
            response_data = {
                "StatusCode": 6002,
                "detail": "error",
                "data": "",
                "message": f'Something went wrong: {e}'
            }

        return Response(response_data, status=status.HTTP_200_OK)
    

class PerksView(APIView):
    serializer_class = careers_serializer.PerksSerializer

    def get(self, request):
        try:
            data = careers_models.Perks.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
 

#destination
class DestinationsView(APIView):
    serializer_class = destination_serializer.DestinationsSerializer

    def get(self, request):
        try:
            data = destination_models.Destinations.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DestinationBannerView(APIView):
    serializer_class = destination_serializer.DestinationBannerSerializer

    def get(self, request):
        try:
            data = destination_models.DestinationBanner.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DestinationWhyChooseView(APIView):
    serializer_class = destination_serializer.DestinationWhyChooseSerializer

    def get(self, request):
        try:
            data = destination_models.DestinationWhyChoose.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UniversityView(APIView):
    serializer_class = destination_serializer.UniversitySerializer

    def get(self, request):
        try:
            data = destination_models.University.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LifeAsStudentView(APIView):
    serializer_class = destination_serializer.LifeAsStudentSerializer

    def get(self, request):
        try:
            data = destination_models.LifeAsStudent.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DestinationFaqView(APIView):
    serializer_class = destination_serializer.DestinationFaqSerializer

    def get(self, request):
        try:
            data = destination_models.DestinationFaq.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VisaBannerView(APIView):
    serializer_class = destination_serializer.VisaBannerSerializer

    def get(self, request):
        try:
            data = destination_models.VisaBanner.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VisaDocumentsView(APIView):
    serializer_class = destination_serializer.VisaDocumentsSerializer

    def get(self, request):
        try:
            data = destination_models.VisaDocuments.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VisaCardsView(APIView):
    serializer_class = destination_serializer.VisaCardsSerializer

    def get(self, request):
        try:
            data = destination_models.VisaCards.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VisaYourObligationsView(APIView):
    serializer_class = destination_serializer.VisaYourObligationsSerializer

    def get(self, request):
        try:
            data = destination_models.VisaYourObligations.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ScholarshipBannerView(APIView):
    serializer_class = destination_serializer.ScholarshipBannerSerializer

    def get(self, request):
        try:
            data = destination_models.ScholarshipBanner.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ScholarshipCardsView(APIView):
    serializer_class = destination_serializer.ScholarshipCardsSerializer

    def get(self, request):
        try:
            data = destination_models.ScholarshipCards.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ScholarshipsView(APIView):
    serializer_class = destination_serializer.ScholarshipsSerializer

    def get(self, request):
        try:
            data = destination_models.Scholarships.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CostOfStudyView(APIView):
    serializer_class = destination_serializer.CostOfStudySerializer

    def get(self, request):
        try:
            data = destination_models.CostOfStudy.objects.filter(is_deleted=False)
            serializer = self.serializer_class(data, many=True, context={"request": request})
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)