from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .models import User, CoffeeBar, Menu, Review

def index(request):
    latest_coffeeBar_list = CoffeeBar.objects.order_by('-avg_vote')[:10]
    context = {'latest_coffeeBar_list': latest_coffeeBar_list}
    return render(request, 'reviews/index.html', context)

def detail(request, coffeeBar_id):
    # coffeeBar = get_object_or_404(CoffeeBar, pk=coffeeBar_id)
    # return render(request, 'reviews/detail.html', {'coffeeBar': coffeeBar})
    # return HttpResponse("Quán %s." % coffeeBar_id)
    try:
        coffeeBar = CoffeeBar.objects.get(pk=coffeeBar_id)
    except CoffeeBar.DoesNotExist:
        raise Http404("CoffeeBar does not exist")
    return render(request, 'reviews/detail.html', {'coffeeBar': coffeeBar})

def results(request, coffeeBar_id):
    response = "Review quán %s."
    return HttpResponse(response % coffeeBar_id)

def vote(request, coffeeBar_id):
    return HttpResponse("Bạn đang đánh giá quán %s." % coffeeBar_id)