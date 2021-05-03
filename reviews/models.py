import datetime

from django.db import models
from django.utils import timezone

class User(models.Model):
    id = models.IntegerField
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    
    def __str__(self):
        return self.email

class CoffeeBar(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=500)
    description = models.TextField(max_length=500)
    address = models.CharField(max_length=500)
    avg_vote = models.DecimalField(max_digits=3, decimal_places=1)
    created_at = models.DateTimeField('date published')

    def __str__(self):
        return self.name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_at <= now
    
    def total_votes(self):
        vote = Review.objects.filter(coffeeBar__id__exact=self.id)
        total = 0
        for x in vote:
            total += x.vote
        return total


class Menu(models.Model):
    coffeeBar = models.ForeignKey(CoffeeBar, on_delete=models.CASCADE)
    id = models.IntegerField
    name = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField
    description = models.CharField(max_length=500)
    # coffeeBarId = models.IntegerField

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coffeeBar = models.ForeignKey(CoffeeBar, on_delete=models.CASCADE)
    id = models.IntegerField
    vote = models.IntegerField(default=5)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField('date published')
    # coffeeBarId = models.IntegerField
    # userId = models.IntegerField

    # def __str__(self):
    #     return str(self.coffeeBar)

    def __str__(self):
        return self.description
 
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_at <= now
    
    