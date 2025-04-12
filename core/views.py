from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class HelloAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({
            'message': f'Hello, {request.user.username} 👋',
            'authenticated': True
        })