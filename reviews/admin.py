from django.contrib import admin

from .models import User, CoffeeBar, Menu, Review

admin.site.register(User)
admin.site.register(CoffeeBar)
admin.site.register(Menu)
admin.site.register(Review)
