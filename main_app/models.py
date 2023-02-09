from django.db import models
from django.urls import reverse

class Shore(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"shore_id": self.id})

class Feeding(models.Model):
    MEALS = (
        ('B', 'Brunch'),
        ('L', 'Lunch'),
        ('D', 'Dinner')
    )
    date = models.DateField('revervation day')
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])
    shore = models.ForeignKey(Shore, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

