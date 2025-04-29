from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .serializers import SchoolClassSerializer, AttendanceSerializer, ResultSerializer
from .models import SchoolClass, Attendance, Result
from rest_framework import viewsets
from rest_framework.permissions import BasePermission
from rest_framework.decorators import action
from rest_framework.response import Response
class IsTeacherOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.role in ['teacher', 'admin']
class SchoolClassViewSet(viewsets.ModelViewSet):
    queryset = SchoolClass.objects.all()
    serializer_class =SchoolClassSerializer
    permission_classes = [IsAuthenticated]


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated,IsTeacherOrAdmin]

    def perform_create(self, serializer):
        serializer.save()

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def my_attendance(self, request):
        user = request.user
        attendance_records = Attendance.objects.filter(student=user)
        serializer = self.get_serializer(attendance_records, many=True)
        return Response(serializer.data)
    

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'student':
            return Result.objects.filter(student=user)
        elif user.role == 'teacher':
            return Result.objects.all()
        return Result.objects.none()
    
    def perform_create(self, serializer):
        serializer.save()
        
