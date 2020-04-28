from django.db import models
from django.utils import timezone
from django.urls import reverse  # To generate URLS by reversing URL patterns

class Car(models.Model):
    """Model representing a car (but not a specific instance of a car)."""
    brand = models.CharField(max_length=200)
    year = models.IntegerField()
    doors = models.IntegerField()
    diesel = models.BooleanField()
    persons = models.IntegerField()

    def get_absolute_url(self):
        """Returns the url to access a particular car instance."""
        return reverse('car-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Car object."""
        return self.brand

import uuid  # Required for unique car instances
from datetime import date

from django.contrib.auth.models import User  # Required to assign User as a borrower

class CarInstance(models.Model):
    """Model representing a specific instance of a car."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular car")
    car = models.ForeignKey('Car', on_delete=models.SET_NULL, null=True)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    LOAN_STATUS = (
        ('d', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Car availability')

    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set car as returned"),)

    def __str__(self):
        """String for representing the Model object."""
        return '{0} ({1})'.format(self.id, self.book.brand)
