from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .serializers import SchoolClassSerializer, AttendanceSerializer
from .models import SchoolClass, Attendance
from rest_framework import viewsets
from rest_framework.permissions import BasePermission

class IsTeacherOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['teacher', 'admin']
class SchoolClassViewSet(viewsets.ModelViewSet):
    queryset = SchoolClass.objects.all()
    serializer_class =SchoolClassSerializer
    permission_classes = [IsAuthenticated]


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsTeacherOrAdmin]

    def perform_create(self, serializer):
        serializer.save()

