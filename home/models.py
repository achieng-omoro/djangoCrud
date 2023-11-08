from django.db import models


# Create your models here.
class driver (models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField()
    phone = models.IntegerField()
    licence = models.CharField(max_length=1, blank=False, null=False)
    image = models.ImageField(upload_to="uploads/media", default="uploads/images/profile.jpg")

    def __str__(self):
        return self.name


class Slider(models.Model):
    text = models.CharField(max_length=50, blank=False, null=False)
    text1 = models.CharField(max_length=30, blank=False, null=False)
    image = models.ImageField(upload_to="uploads/slider", default="uploads/slider/profile.jpg")

    def __str__(self):
        return self.text
