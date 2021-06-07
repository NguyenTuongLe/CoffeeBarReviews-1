from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, null=True)


class CoffeeBar(models.Model):
    name = models.CharField(max_length=255)
    summary = models.TextField(null=True)
    description = models.TextField()
    address = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to="coffee_bars", null=True)
    avg_vote = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Menu(models.Model):
    coffee_bar = models.ForeignKey(CoffeeBar, on_delete=models.CASCADE)
    name = models.CharField(null=False, blank=False, max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to='menus', null=True, blank=True)
    description = models.CharField(null=True, max_length=255, blank=True)


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    coffee_bar = models.ForeignKey(CoffeeBar, on_delete=models.CASCADE)
    vote = models.PositiveIntegerField(default=5)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
