from django.db import models
from acc.models import User

# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    writer_pic = models.ImageField()
    comment = models.TextField()
    voter = models.ManyToManyField(User, blank=True)

class Choice(models.Model):
    title = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pic = models.ImageField(upload_to="vote", blank=True)
    choicer = models.ManyToManyField(User, blank=True)