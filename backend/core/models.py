from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
    
class Account(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to="core/assets/accounts/images", null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Publication(models.Model):
    publication_name = models.CharField(max_length=255)
    publication_image = models.ImageField(
        upload_to="core/assets/products/publications")
    publication_description = models.TextField()
    publication_price = models.IntegerField()
    publication_author = models.CharField(max_length=255)
    publication_size = models.IntegerField()
    publication_ISBN = models.BigIntegerField()
    publication_price_tag = models.CharField(
        max_length=255, default="In Stock")
    publication_language = models.CharField(max_length=255)
    publication_offer = models.CharField(max_length=255, null=True)
    publication_reviews = models.IntegerField(null=True)
    publication_stars = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.publication_name}"
