from django.db import models


# Create your models here.
class Movie(models.Model):

    img = models.ImageField(upload_to='images')
    name = models.CharField(max_length=250)
    desc = models.TextField()
    year = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
