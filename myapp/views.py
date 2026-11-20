from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET'])
def welcome(request):
    return Response({
        "message": "Welcome to the Student API 🎓",
        "endpoints": {
            "students": "/api/students/",
            "admin": "/admin/",
        }
    })

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('-created_at')
    serializer_class = StudentSerializer