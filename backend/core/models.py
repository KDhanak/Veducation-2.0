from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class Account(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to="core/assets/accounts/images", null=True, blank=True)

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
