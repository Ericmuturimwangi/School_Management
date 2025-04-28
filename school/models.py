from django.db import models
from core.models import InstructorProfile
from django.utils import timezone
from core.models import User

class SchoolClass(models.Model):
    name  = models.CharField(max_length=100)
    assigned_instructor = models.ForeignKey(InstructorProfile, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.name} - {self.subject}"
    
class Attendance (models.Model):
    ATTENDANCE_CHOICES = (
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
    )
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=ATTENDANCE_CHOICES, default='present')


    def __str__(self):
        return f"{self.student.username}- {self.school_class.name} - {self.status} on {self.date}"
    
 


