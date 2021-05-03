from django.contrib import admin

from .models import User, CoffeeBar, Menu, Review

class CoffeeBarAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None, {'fields': ['avg_vote']}),
        (None, {'fields': ['address']}),
        (None, {'fields': ['description']}),
        (None, {'fields': ['created_at']}),
    ]

admin.site.register(CoffeeBar, CoffeeBarAdmin)

admin.site.register(User)
# admin.site.register(CoffeeBar)
admin.site.register(Menu)
admin.site.register(Review)
