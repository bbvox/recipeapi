import uuid
import os
from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin

from django.conf import settings


def recipe_image_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/recipe/', filename)



class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that suppors using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
""" """

class Diet(models.Model):
    
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Allergy(models.Model):
    
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Course(models.Model):
    
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Cousine(models.Model):
    
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Holiday(models.Model):
    
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Nutritions(models.Model):
   
    name = models.CharField(max_length=255)
    calories = models.IntegerField(blank=True)
    fat_calories = models.IntegerField(blank=True)
    total_fat = models.IntegerField(blank=True)
    sat_fat = models.IntegerField(blank=True)
    trans_fat = models.IntegerField(blank=True)
    sodium = models.IntegerField(blank=True)
    total_carb = models.IntegerField(blank=True)
    fibers = models.IntegerField(blank=True)
    sugar = models.IntegerField(blank=True)
    proteins = models.IntegerField(blank=True)
    vitamins = models.IntegerField(blank=True)
    calcium = models.IntegerField(blank=True)
    iron = models.IntegerField(blank=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name        
""" """
class Tag(models.Model):
    """Tag to be used for a recipe"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Recipe(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )
    title = models.CharField(max_length= 255)
    time_minutes = models.IntegerField()
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    link = models.CharField(max_length=255, blank=True)
    ingredients = models.ManyToManyField('Ingredient',blank=True)
    tags = models.ManyToManyField('Tag',blank=True)
    diet = models.ManyToManyField('Diet', blank=True)
    allergy = models.ManyToManyField('Allergy', blank=True)
    course = models.ManyToManyField('Course', blank=True)
    cousine = models.ManyToManyField('Cousine', blank=True)
    holiday = models.ManyToManyField('Holiday', blank=True)
    nutritions = models.ManyToManyField('Nutritions', blank=True)
    image = models.ImageField(upload_to=recipe_image_file_path, blank=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
