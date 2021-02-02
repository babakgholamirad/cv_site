from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import Truncator
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class User(AbstractUser):
    image = models.ImageField(upload_to='images/', null=True, blank=True)


class Member(models.Model):
    user = models.ForeignKey("cv.User", null=True,
                             blank=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def get_full_name(self):
        if self.user:
            return self.user.get_full_name() if self.user.get_full_name() else self.user.get_username()

    def get_abbreviation(self):
        if self.user:
            self.user.get_full



class Project(models.Model):
    title = models.CharField(max_length=200, blank=True)
    owner = models.ForeignKey('cv.User', on_delete=models.SET_NULL, null=True)
    members = models.ManyToManyField(
        'cv.Member', through='MemberOfProject', related_name='member_projects')
    description = models.TextField(null=True)

    STATUS_CHOICES = [
        ("OH", "On Hold"),
        ("SC", "Success"),
        ("CA", "Canceled"),
    ]
    status = models.CharField(max_length=50, default="On Hold", choices=STATUS_CHOICES)

    progress = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(100)
    ])
    start_date = models.DateTimeField()

    def __str__(self):
        return(self.title)

    def shrot_description(self):
        return Truncator(self.description).words(20)


class MemberOfProject(models.Model):
    member = models.ForeignKey('cv.Member', on_delete=models.CASCADE)
    project = models.ForeignKey('cv.Project', on_delete=models.CASCADE)
    role_in_project = models.CharField(max_length=150, null=False, blank=False)
    date_joined = models.DateTimeField()
    date_left = models.DateTimeField()
