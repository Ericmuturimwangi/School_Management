from django.core.management.base import BaseCommand
from core.models import User
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):
    help = 'Create a teacher user with role=teacher'

    def handle (self, *args, **kwargs):
        username = input ('Username: ')
        email = input ('Email: ')
        service_number = input ('Service Number: ')
        rank = input ('Rank: ')
        password = input ('Password: ')

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.ERROR('User already exists'))
            return
        
        user = User(
            username = username,
            email = email,
            service_number = service_number,
            rank = rank,
            role = 'teacher',
            password = make_password(password)
        )
        user.save()
        self.stdout.write(self.style.SUCCESS(f'Teacher {username} created successfully'))