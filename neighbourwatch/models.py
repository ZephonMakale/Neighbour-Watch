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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=10)
    bio = models.TextField(max_length=50, blank=True)
    profile_photo = models.ImageField(upload_to='images/', default='default.png')
    location = models.CharField(max_length=10, blank=True, null=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.SET_NULL, related_name='members', blank=True)


    def __str__(self):
        return f'{self.user.username} profile' 

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Business(models.Model):
    name = models.CharField(max_length=10)
    biz_email = models.EmailField(max_length=15)
    description = models.TextField(max_length=30, blank=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete = models.CASCADE, related_name='business')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return f'{self.name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()
    
    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()

class Post(models.Model):
    title = models.CharField(max_length=10, null=True)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
    hood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='hood_post')

