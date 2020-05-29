from django.db import models

# Create your models here.
class Job (models.Model):
    title = models.CharField(max_length=50)
    start_date = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    description = models.CharField(max_length=200)


#class Teams(models.Model):
#    name = models.CharField(max_length=20)
