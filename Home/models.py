from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# makemigrations = create changes and store in a file 
# migrate = apply the pending changes created by makemigrations


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class StudyMaterials(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    instructor = models.CharField(max_length=250)
    course_title = models.CharField(max_length=500)
    course_code = models.CharField(max_length=100)
    thumbnail = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.course_title + ' - ' + self.instructor


class Question(models.Model):
    subject = models.CharField(max_length=100)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.subject


class Answer(models.Model):
    subject = models.CharField(max_length=100)
    to = models.CharField(max_length=50, default="")
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.subject