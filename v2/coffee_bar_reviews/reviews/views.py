from django.shortcuts import render
from .models import CoffeeBar


# Create your views here.
def coffee_bars_list_view(request):
    coffee_bars = CoffeeBar.objects.order_by("-created_at").all()
    context = {
        "list": coffee_bars
    }
    return render(request, "reviews/coffee_bars.html", context)
