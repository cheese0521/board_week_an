from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.files import ImageField

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    comment = models.TextField(blank=True)
    pic = models.ImageField(upload_to="user/%y/%m", default="none.png")
    point = models.IntegerField(default=0)