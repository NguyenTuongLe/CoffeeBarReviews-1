from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('reviews/', include('reviews.urls')),
    path('admin/', admin.site.urls),
]