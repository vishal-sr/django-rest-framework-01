from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=25)
    score = models.DecimalField(max_digits=2, decimal_places=2, validators=[
        MinValueValidator(0), MaxValueValidator(100)
    ])
