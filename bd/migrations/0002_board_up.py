# Generated by Django 3.2.7 on 2021-10-02 09:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='up',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
