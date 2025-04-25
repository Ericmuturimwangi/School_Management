from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES =(
        ('admin', 'Admin'),
        ('instructor', 'Instructor'),
        ('student', 'Student'),
    )
    RANK_CHOICES = (
        ('SGT', 'Sergeant'),
        ('CPL', 'Corporal'),
        ('SPTE', 'Specialist'),
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