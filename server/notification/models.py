from django.db import models

# Create your models here.

class notification(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    date_added = models.DateTimeField()
    status = models.IntegerField()