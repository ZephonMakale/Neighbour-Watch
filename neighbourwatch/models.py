from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from pyuploadcare.dj.models import ImageField

class NeighbourHood(models.Model):
    hood_name = models.CharField(max_length=10)
    hood_location = models.CharField(max_length=10)
    hood_photo = models.ImageField(upload_to= 'images/')
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    hood_nyumbakumi = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.hood_name} hood'

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    @classmethod
    def find_neighbourhood(cls, neighbourhood_id):
        return cls.objects.filter(id=neighbourhood_id)

