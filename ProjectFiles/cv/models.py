from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import Truncator

# Create your models here.


class User(AbstractUser):
    image = models.ImageField(upload_to='images/', null=True, blank=True)


class Project(models.Model):
    title = models.CharField(max_length=200, blank=True)
    owner = models.ForeignKey('cv.User', on_delete=models.SET_NULL, null=True)
    members = models.ManyToManyField(
        'cv.User', through='MemberOfProject', related_name='member_projects')
    description = models.TextField(null=True)
    start_date = models.DateTimeField()

    def __str__(self):
        return(self.title)

    def shrot_description(self):
        return Truncator(self.description).words(20)


class MemberOfProject(models.Model):
    member = models.ForeignKey('cv.User', on_delete=models.CASCADE)
    project = models.ForeignKey('cv.Project', on_delete=models.CASCADE)
    role_in_project = models.CharField(max_length=100, null=False, blank=False)
    date_joined = models.DateTimeField()
    date_left = models.DateTimeField()
