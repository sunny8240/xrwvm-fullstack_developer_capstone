from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    """
    Stores information about car manufacturers.
    Each CarMake can have multiple CarModel(s) associated with it.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    founded_year = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(1800),
            MaxValueValidator(now().year)
        ]
    )

    def __str__(self):
        return self.name


class CarModel(models.Model):
    """
    Stores information about specific car models.
    Each CarModel belongs to a CarMake (Many-to-One relationship).
    """
    car_make = models.ForeignKey(
        CarMake,
        on_delete=models.CASCADE,
        related_name='models'
    )
    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('HATCHBACK', 'Hatchback'),
        ('COUPE', 'Coupe'),
        ('CONVERTIBLE', 'Convertible'),
    ]
    type = models.CharField(max_length=15, choices=CAR_TYPES, default='SEDAN')

    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ],
        default=2023
    )
    color = models.CharField(
        max_length=30, 
        blank=True, 
        null=True)
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        blank=True, 
        null=True)
    vin_number = models.CharField(max_length=17, 
        unique=True, 
        blank=True, 
        null=True)

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
