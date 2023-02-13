from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User


class Attraction(models.Model):
    name = models.CharField(max_length=50)
    fun_type = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.fun_type} {self.name}'

    def get_absolute_url(self):
        return reverse("attractions_detail", kwargs={"pk": self.id})


class Shore(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    attractions = models.ManyToManyField(Attraction)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"shore_id": self.id})
    

class Reservation(models.Model):
    MEALS = (
        ('B', 'Brunch'),
        ('L', 'Lunch'),
        ('D', 'Dinner')
    )
    date = models.DateField('revervation day')
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ('-date',)

class Image(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')


