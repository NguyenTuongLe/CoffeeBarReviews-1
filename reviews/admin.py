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
        (None,               {'fields': ['name']}),
        (None, {'fields': ['avg_vote']}),
        (None, {'fields': ['address']}),
        (None, {'fields': ['description']}),
        (None, {'fields': ['created_at'], 'classes': ['collapse']}),
    ]
    inlines = [MenuInline, ReviewInline]
    list_display = ('name', 'created_at')
    search_fields = ['name']


admin.site.register(CoffeeBar, CoffeeBarAdmin)

admin.site.register(User)

admin.site.register(Menu)

admin.site.register(Review)
