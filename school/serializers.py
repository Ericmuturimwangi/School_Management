from rest_framework import serializers
from .models import SchoolClass, Attendance, Result
from core.models import InstructorProfile


class SchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = ['id', 'name', 'assigned_instructor', 'subject']

class AttendanceSerializer(serializers.ModelSerializer):
    student = serializers.CharField(source='student.username', read_only=True)
    school_class = serializers.CharField(source='school_class.name', read_only=True)
    class Meta:
        model = Attendance
        fields = ['id','student', 'school_class', 'date', 'status']

class ResultSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.username', read_only=True)

    class Meta:
        model = Result
        fields = ['id', 'student', 'student_name', 'school_class', 'subject', 'score', 'remarks', 'date_recorded']
        read_only_fields = ['student_name', 'date_recorded']

        


