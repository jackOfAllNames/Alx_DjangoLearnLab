from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extras):
        if not email:
            raise ValueError("Users must have an email address")
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extras)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None, **extras):
        extras.setdefault('is_staff', True)
        extras.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extras)
    

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
