from django.urls import path

from .views import coffee_bars_list_view

app_name = 'reviews'
urlpatterns = [
    path('', coffee_bars_list_view, name='coffee-bar-list-view')
]
