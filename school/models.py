from django.db import models
from core.models import InstructorProfile

class SchoolClass(models.Model):
    name  = models.CharField(max_length=100)
    assigned_instructor = models.ForeignKey(InstructorProfile, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.name} - {self.subject}"
    
    
 


