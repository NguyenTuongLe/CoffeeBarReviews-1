from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import User, CoffeeBar, Menu, Review


class IndexView(generic.ListView):
    template_name = 'reviews/index.html'
    context_object_name = 'latest_coffeeBar_list'

    def get_queryset(self):
        return CoffeeBar.objects.filter(
        created_at__lte=timezone.now()
        ).order_by('-avg_vote')[:10]


class DetailView(generic.DetailView):
    model = CoffeeBar
    template_name = 'reviews/detail.html'

    def get_queryset(self):
        return CoffeeBar.objects.filter(created_at__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = CoffeeBar
    template_name = 'reviews/results.html'


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