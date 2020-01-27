from django.db import models

# Create your models here.
class Parametertype(models.Model):
    parametertype = models.CharField(max_length=300)
    isactive = models.IntegerField()
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()