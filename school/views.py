from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .serializers import SchoolClassSerializer
from .models import SchoolClass
from rest_framework import viewsets

class SchoolClassViewSet(viewsets.ModelViewSet):
    queryset = SchoolClass.objects.all()
    serializer_class =SchoolClassSerializer
    permission_classes = [IsAuthenticated]

    
