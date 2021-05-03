from django.contrib import admin

from .models import User, CoffeeBar, Menu, Review

class MenuInline(admin.TabularInline):
    model = Menu
    extra = 0


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0


class CoffeeBarAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['avg_vote']}),
        (None, {'fields': ['address']}),
        (None, {'fields': ['description']}),
        (None, {'fields': ['created_at'], 'classes': ['collapse']}),
    ]
    inlines = [MenuInline, ReviewInline]
    list_display = ('name', 'avg_vote')
    search_fields = ['name']


class MenuAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['coffeeBar']}),
        (None, {'fields': ['name']}),
        (None, {'fields': ['price']}),
        (None, {'fields': ['description'], 'classes': ['collapse']}),
    ]
    list_display = ('coffeeBar', 'name', 'price')
    search_fields = ['name']


class ReviewAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['coffeeBar']}),
        (None, {'fields': ['user']}),
        (None, {'fields': ['vote']}),
        (None, {'fields': ['description']}),
        (None, {'fields': ['created_at'], 'classes': ['collapse']}),
    ]
    list_display = ('coffeeBar', 'vote', 'description')
    search_fields = ['coffeeBar']


class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['firstName']}),
        (None, {'fields': ['lastName']}),
        (None, {'fields': ['email']}),
        (None, {'fields': ['phone']}),
        (None, {'fields': ['password']}),
        (None, {'fields': ['role'], 'classes': ['collapse']}),
    ]
    list_display = ('firstName', 'lastName', 'email', 'phone')
    search_fields = ['firstName']


admin.site.register(CoffeeBar, CoffeeBarAdmin)

admin.site.register(Menu, MenuAdmin)

admin.site.register(Review, ReviewAdmin)

admin.site.register(User, UserAdmin)
