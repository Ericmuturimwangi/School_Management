from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    ROLE_CHOICES =(
        ('admin', 'Admin'),
        ('instructor', 'Instructor'),
        ('student', 'Student'),
    )
    RANK_CHOICES = (
        ('SGT', 'Sergeant'),
        ('CPL', 'Corporal'),
        ('SPTE', 'Private'),
        ('WOII', 'Warrant Officer II'),
        ('PTE', 'Private'),
        ('LCPL', 'Lance Corporal'),
        ('WOI', 'Warrant Officer I'),
        ('2LT', 'Second Lieutenant'),
        ('LT', 'Lieutenant'),
        ('CAPT', 'Captain'),
        ('MAJ', 'Major'),
        ('LT COL', 'Lieutenant Colonel'),
        ('COL', 'Colonel'),
    )

    service_number = models.CharField(max_length=20, unique=True)
    rank = models.CharField(max_length=20, choices=RANK_CHOICES)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.rank} ({self.username}) - ({self.role})"
    
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    current_class = models.CharField(max_length=50)

    def __str__(self):
        return f"Student: {self.user.username} - {self.current_class}"
    
class InstructorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='instructor_profile')
    subject_specialty = models.CharField(max_length=100)

    def __str__(self):
        return f"Teacher: {self.user.username} - {self.subject_specialty}"

    @receiver(post_save, sender=User)    
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            if instance.role == 'student':
                StudentProfile.objects.create(user=instance)
            elif instance.role == 'instructor':
                InstructorProfile.objects.create(user=instance)    
