from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render

from .models import User, CoffeeBar, Menu, Review

def index(request):
    latest_coffeeBar_list = CoffeeBar.objects.order_by('-avg_vote')[:10]
    context = {'latest_coffeeBar_list': latest_coffeeBar_list}
    return render(request, 'reviews/index.html', context)

def detail(request, coffeeBar_id):
    return HttpResponse("Quán %s." % coffeeBar_id)

def results(request, coffeeBar_id):
    response = "Review quán %s."
    return HttpResponse(response % coffeeBar_id)

def vote(request, coffeeBar_id):
    return HttpResponse("Bạn đang đánh giá quán %s." % coffeeBar_id)