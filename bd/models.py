from django.db import models
from acc.models import User

# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.CharField(max_length=50)
    content = models.TextField()
    up = models.ManyToManyField(User, blank=True)

    def summary(self):
        return self.content[:10] + "..."

class Reply(models.Model):
    subject = models.ForeignKey(Board, on_delete=models.CASCADE)
    replyer = models.CharField(max_length=100)
    replyer_pic = models.ImageField()
    comment = models.TextField()
    agree = models.ManyToManyField(User, blank=True)