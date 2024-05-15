from datetime import date
from api.accounts import models as accounts_models

from django.db import models


class Restaurant(models.Model):
    """Restaurant model"""

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    admin = models.OneToOneField(accounts_models.UserProfile, null=True, default=None, on_delete=models.CASCADE)

    date_created = models.DateField(default=date.today())


class Menu(models.Model):
    """Menu model"""

    dishes = models.TextField(blank=False)
    date = models.DateField(default=date.today(), blank=True)

    restaurant = models.ForeignKey(Restaurant, null = True, on_delete=models.CASCADE)


class EmployeeChoice(models.Model):
    """Chosen menus by employees."""
    user = models.ForeignKey(accounts_models.UserProfile, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    date = models.DateField(default=date.today())

