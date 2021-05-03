from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:coffeeBar_id>/', views.detail, name='detail'),
    path('<int:coffeeBar_id>/results/', views.results, name='results'),
    path('<int:coffeeBar_id>/vote/', views.vote, name='vote'),
]