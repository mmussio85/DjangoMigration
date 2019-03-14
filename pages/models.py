from django.db import models
from django.urls import reverse

# Create your models here.

class Team(models.Model):
    name = models.TextField()
    floor = models.IntegerField()
    section = models.TextField()

class Person(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    profession = models.TextField()
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
    )

    def get_absolute_url(self):  # new
        return reverse('person_detail', args=[str(self.id)])

