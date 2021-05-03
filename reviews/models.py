import datetime

from django.db import models
from django.utils import timezone

class User(models.Model):
    id = models.IntegerField
    firstName = models.TextField(max_length=500)
    lastName = models.TextField(max_length=500)
    email = models.TextField(max_length=500)
    phone = models.TextField(max_length=10)
    password = models.TextField(max_length=50)
    role = models.TextField(max_length=50)
    
    def __str__(self):
        return self.email

class CoffeeBar(models.Model):
    id = models.IntegerField
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=500)
    address = models.TextField(max_length=500)
    avg_vote = models.DecimalField(max_digits=3, decimal_places=1)
    created_at = models.DateTimeField('date published')

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)

class Menu(models.Model):
    coffeeBar = models.ForeignKey(CoffeeBar, on_delete=models.CASCADE)
    id = models.IntegerField
    name = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField
    description = models.TextField(max_length=500)
    # coffeeBarId = models.IntegerField

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coffeeBar = models.ForeignKey(CoffeeBar, on_delete=models.CASCADE)
    id = models.IntegerField
    vote = models.IntegerField(default=5)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField('date published')
    # coffeeBarId = models.IntegerField
    # userId = models.IntegerField

    def __str__(self):
        return str(self.coffeeBar)
 
    def was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)
    
    

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)