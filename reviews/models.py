from django.db import models


class User(models.Model):
    id = models.IntegerField
    firstName = models.TextField(max_length=500)
    lastName = models.TextField(max_length=500)
    email = models.TextField(max_length=500)
    phone = models.TextField(max_length=10)
    password = models.TextField(max_length=50)
    role = models.TextField(max_length=50)

class CoffeeBar(models.Model):
    id = models.IntegerField
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=500)
    address = models.TextField(max_length=500)
    avg_vote = models.DecimalField
    created_at = models.DateTimeField('date published')

class Menu(models.Model):
    coffeeBar = models.ForeignKey(CoffeeBar, on_delete=models.CASCADE)
    id = models.IntegerField
    name = models.TextField(max_length=100)
    price = models.DecimalField
    image = models.ImageField
    description = models.TextField(max_length=500)
    # coffeeBarId = models.IntegerField

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coffeeBar = models.ForeignKey(CoffeeBar, on_delete=models.CASCADE)
    id = models.IntegerField
    vote = models.IntegerField(default=5)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField('date published')
    # coffeeBarId = models.IntegerField
    # userId = models.IntegerField
    

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)