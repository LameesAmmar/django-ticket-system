from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    #username = models.CharField(max_length = 50, unique = True)
    email = models.EmailField( unique = True)
    is_customer=models.BooleanField(default=False)
    is_engineer=models.BooleanField(default=False)
    

    def __str__(self) :
        return self.username