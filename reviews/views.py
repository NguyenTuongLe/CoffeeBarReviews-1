from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse

from .models import User, CoffeeBar, Menu, Review

def index(request):
    latest_coffeeBar_list = CoffeeBar.objects.order_by('-avg_vote')[:10]
    context = {'latest_coffeeBar_list': latest_coffeeBar_list}
    return render(request, 'reviews/index.html', context)

def detail(request, coffeeBar_id):
    coffeeBar = get_object_or_404(CoffeeBar, pk=coffeeBar_id)
    return render(request, 'reviews/detail.html', {'coffeeBar': coffeeBar})
  
def results(request, coffeeBar_id):
    coffeeBar = get_object_or_404(CoffeeBar, pk=coffeeBar_id)
    return render(request, 'reviews/results.html', {'coffeeBar': coffeeBar})

def vote(request, coffeeBar_id):
    coffeeBar = get_object_or_404(CoffeeBar, pk=coffeeBar_id)
    try:
        selected_review = coffeeBar.review_set.get(pk=request.POST['review'])
    except (KeyError, Review.DoesNotExist):
        return render(request, 'reviews/detail.html', {
            'coffeeBar': coffeeBar,
            'error_message': "Bạn chưa đánh giá quán.",
        })
    else:
        selected_review.vote += 1
        selected_review.save()
        return HttpResponseRedirect(reverse('reviews:results', args=(coffeeBar.id,)))