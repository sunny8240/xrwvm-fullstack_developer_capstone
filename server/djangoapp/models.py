# Uncomment the following imports before adding the Model code
from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# ===============================
# Car Make Model
# ===============================
class CarMake(models.Model):
    """
    CarMake stores information about the manufacturer of cars.
    Each CarMake can have multiple CarModel(s) associated with it.
    """

    # Name of the manufacturer (e.g., Toyota, Ford)
    name = models.CharField(max_length=100, unique=True)

    # Description or details about the manufacturer
    description = models.TextField(blank=True, null=True)

    # Optional field: Country of origin
    country = models.CharField(max_length=50, blank=True, null=True)

    # Optional field: Year the manufacturer was founded
    founded_year = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(1800),  # Cars not before 1800
            MaxValueValidator(now().year)  # Cannot be a future year
        ]
    )

    # String representation of the CarMake
    def __str__(self):
        return self.name

# ===============================
# Car Model
# ===============================
class CarModel(models.Model):
    """
    CarModel stores information about specific car models.
    Each CarModel belongs to a CarMake (Many-to-One relationship).
    """

    # Many-to-One relationship with CarMake
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')

    # Name of the car model (e.g., Corolla, Mustang)
    name = models.CharField(max_length=100)

    # Choices for type of car
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('HATCHBACK', 'Hatchback'),
        ('COUPE', 'Coupe'),
        ('CONVERTIBLE', 'Convertible'),
    ]

    # Type of car, limited to choices above
    type = models.CharField(max_length=15, choices=CAR_TYPES, default='SEDAN')

    # Year of manufacture with validators for realistic range
    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ],
        default=2023
    )

    # Optional field: color of the car
    color = models.CharField(max_length=30, blank=True, null=True)

    # Optional field: price of the car
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # Optional field: VIN (Vehicle Identification Number), unique for each car
    vin_number = models.CharField(max_length=17, unique=True, blank=True, null=True)

    # String representation to display car make and model together
    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"

