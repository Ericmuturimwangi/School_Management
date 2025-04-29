from django.contrib import admin
from .models import SchoolClass, Attendance, Result
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

admin.site.register(SchoolClass)
admin.site.register(Attendance)


@admin.register(Result)
class ResultAdmin (admin.ModelAdmin):
    list_display =(
        'student',
        'school_class',
        'subject',
        'remarks',
        'date_recorded'
    )
    list_filter = ('school_class', 'subject', 'date_recorded')
    search_fields = ('student__service_number', 'subject', 'school_class__name')
    ordering = ('date_recorded',)

class PerformanceReport(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    school_class = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    score = models.IntegerField()
    remarks = models.TextField()
    date_recorded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for {self.student.username} in {self.subject}"
    
@admin.register(PerformanceReport)
class PerformanceReportAdmin(admin.ModelAdmin):
    list_display = ('student', 'school_class', 'subject', 'score', 'remarks', 'date_recorded')
    search_fields = ('student__username', 'school_class', 'subject')
    list_filter = ('school_class', 'subject')
