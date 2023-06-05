from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Sauce(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('sauce-detail', kwargs={"pk": self.id})
    

class Taco(models.Model):
    name = models.CharField(max_length=100)
    meat = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    order = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("taco-detail", kwargs={"taco_id": self.id})
    
    def served_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)


class Feeding(models.Model):
    date = models.DateField('Order Date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )

    taco = models.ForeignKey(Taco, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']