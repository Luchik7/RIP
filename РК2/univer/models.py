from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Student(models.Model):
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    name = models.TextField()
    surname = models.TextField()

    def __str__(self):
        return "Name of student: {0}".format(self.name)

class Group(models.Model):
    name = models.CharField(max_length=32, null=False, unique=True)
    qnt_of_students = models.IntegerField(null=False)

    def __str__(self):
        return self.name