from django.core.management.base import BaseCommand
from core.models import Account
import getpass

class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **options):
        email = input("Enter email for superuser: ")
        password = getpass.getpass("Enter password for superuser: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone_number = input("Enter phone number: ")

        # Create superuser
        Account.objects.create_superuser(email=email, password=password, first_name=first_name, last_name=last_name, phone_number=phone_number)
        self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
