from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import Truncator
from django.core.validators import MaxValueValidator, MinValueValidator
from utils.useful_functions import get_accronym
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your models here.


class User(AbstractUser):
    image = models.ImageField(upload_to='images/', null=True, blank=True)


class Member(models.Model):
    user = models.ForeignKey("cv.User", null=True,
                             blank=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/', default=staticfiles_storage.url(
        'account/images/boxed-bg.png'), null=False, blank=False)

    def get_full_name(self):
        if self.user:
            return self.user.get_full_name() if self.user.get_full_name() else self.user.get_username()
        return "{} {}".format(self.first_name, self.last_name)

    def get_accronym(self):
        return get_accronym(self.get_full_name())

    def get_image(self):
        default_image_url = staticfiles_storage.url(
            'account/images/user_2.svg')
        if self.user and self.user.image:
            return self.user.image
        return default_image_url

    def __str__(self):
        return self.get_full_name()


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True,
                            null=False, blank=False)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)
    project = models.ForeignKey(
        "cv.Project", on_delete=models.CASCADE, null=True)
    assigner = models.ForeignKey(
        "cv.Member", on_delete=models.SET_NULL, null=True)
    members = models.ManyToManyField(
        "cv.MemberOfProject", related_name='tasks')
    tags = models.ManyToManyField("cv.Tag")
    description = models.TextField()
    date_created = models.DateTimeField()
    deadline = models.DateTimeField(null=True, blank=True)
    finished = models.BooleanField(default=False, null=False, blank=False)

    def short_description(self):
        return Truncator(self.description).words(20)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200, blank=True)
    leader = models.ForeignKey('cv.User', on_delete=models.SET_NULL, null=True)
    client = models.CharField(max_length=200, blank=True)

    members = models.ManyToManyField(
        'cv.Member', through='MemberOfProject', related_name='member_projects')

    description = models.TextField(null=True)

    STATUS_CHOICES = [
        ("On Hold", "On Hold"),
        ("On Going", "On Going"),
        ("Success", "Success"),
        ("Canceled", "Canceled"),
    ]
    status = models.CharField(
        max_length=50, default="On Hold", choices=STATUS_CHOICES)

    progress = models.PositiveSmallIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    start_date = models.DateTimeField()

    def __str__(self):
        return(self.title)

    def short_description(self):
        return Truncator(self.description).words(20)

    def tasks(self):
        return Task.objects.filter(members__project__id=self.id)


class MemberOfProject(models.Model):
    member = models.ForeignKey('cv.Member', on_delete=models.CASCADE)
    project = models.ForeignKey('cv.Project', on_delete=models.CASCADE)
    role_in_project = models.CharField(max_length=150, null=False, blank=False)
    date_joined = models.DateTimeField()
    date_left = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return("{} ({}) of {}".format(self.member.get_full_name(),
                                      self.role_in_project,
                                      self.project))
