from tabnanny import verbose
from django.db import models

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.pizza_name

class Toppings(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    topping_name = models.CharField(max_length = 100)

    class Meta:
        verbose_name_plural = 'Toppings'

    def __str__(self):
        return self.topping_name