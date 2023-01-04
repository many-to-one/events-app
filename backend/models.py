from django.db import models
from drf_user.urls import User


class Event(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    event = models.TextField(
        null=True,
        max_length=500,
    )
    hours = models.IntegerField(
        default=0,
    )
    minutes = models.IntegerField(
        default=0,
    )
    visits = models.IntegerField(
        default=0,
    )
    publications = models.IntegerField(
        default=0,
    )
    films = models.IntegerField(
        default=0,
    )
    studies = models.IntegerField(
        default=0,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self) -> str:
        return str(self.date)[:16]


class EventsHistory(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    event = models.TextField(
        null=True,
        max_length=500,
    )
    hours = models.IntegerField(
        default=0,
    )
    minutes = models.IntegerField(
        default=0,
    )
    visits = models.IntegerField(
        default=0,
    )
    publications = models.IntegerField(
        default=0,
    )
    films = models.IntegerField(
        default=0,
    )
    studies = models.IntegerField(
        default=0,
    )
    user = models.ForeignKey(
        NewUser,
        on_delete=models.CASCADE,
        null=True,
    )
    month = models.ForeignKey(
        'Months',
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self) -> str:
        return str(self.date)[:16]


class HoursResult(models.Model):
    date = models.CharField(
        null=True,
        max_length=20,
    )
    hours = models.IntegerField(
        default=0,
    )
    minutes = models.IntegerField(
        default=0,
    )
    visits = models.IntegerField(
        default=0,
    )
    publications = models.IntegerField(
        default=0,
    )
    films = models.IntegerField(
        default=0,
    )

    def __str__(self) -> str:
        return str(self.hours)


class Months(models.Model):
    date = models.CharField(
        null=True,
        max_length=20,
    )
    hours = models.IntegerField(
        default=0,
    )
    minutes = models.IntegerField(
        default=0,
    )
    visits = models.IntegerField(
        default=0,
    )
    publications = models.IntegerField(
        default=0,
    )
    films = models.IntegerField(
        default=0,
    )
    user = models.ForeignKey(
        NewUser,
        on_delete=models.CASCADE,
        null=True
    )  

    def __str__(self) -> str:
        return str(self.id)    


class Image (models.Model):
    name = models.CharField(
        max_length=20,
        null=True,
    )  
    image = models.ImageField(
        upload_to=('maps')
    )  

    def __str__(self) -> str:
        return str(self.name) 