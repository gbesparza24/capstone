from django.db import models

# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='images/')
    realty_company = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    experience = models.IntegerField(default=0)
    def __str__(self):
        return self.name