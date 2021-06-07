from django.contrib import admin

# Register your models here.
from .models import CoffeeBar, Review, Menu


class MenuInline(admin.TabularInline):
    model = Menu


class CoffeeBarAdmin(admin.ModelAdmin):
    inlines = [MenuInline]
    list_display = ('name', 'avg_vote', "image")
    search_fields = ['name', 'description']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('coffee_bar', 'vote', 'description')
    search_fields = ['description']


admin.site.register(CoffeeBar, CoffeeBarAdmin)
admin.site.register(Review, ReviewAdmin)
