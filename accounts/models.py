from django.db import models
from  django.contrib.auth.models import AbstractUser
from django.db import models
from . manager import CustomUserManager
from . manage import *




class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_verified=models.BooleanField(default=False )
    phone_no = models.CharField(max_length=12)
    is_phone_no_verified = models.BooleanField(default=False)

    


    objects = CustomUserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

# Create your models here.
