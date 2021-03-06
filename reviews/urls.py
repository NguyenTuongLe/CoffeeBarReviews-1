from django.urls import path

from .views import coffee_bars_detail, coffee_bars_list_view, register_view, login_view, logout_view

app_name = 'reviews'
urlpatterns = [
    path('', coffee_bars_list_view, name='home'),
    path('<int:coffee_bar_id>/', coffee_bars_detail, name='detail'),
    path('register', register_view, name='register'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
]
   