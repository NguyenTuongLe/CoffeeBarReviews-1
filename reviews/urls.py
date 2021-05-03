from django.urls import path

from . import views

app_name = 'reviews'
urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:coffeeBar_id>/', views.detail, name='detail'),
    # path('<int:coffeeBar_id>/results/', views.results, name='results'),
    # path('<int:coffeeBar_id>/vote/', views.vote, name='vote'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:coffeeBar_id>/vote/', views.vote, name='vote'),
]