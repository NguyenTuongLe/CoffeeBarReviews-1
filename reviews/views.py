from django.contrib.auth import login, authenticate, logout
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import CoffeeBar, Review
from .forms import SignUpForm, ReviewForm
from django.contrib.auth.forms import AuthenticationForm
from django.views import generic
from django.utils import timezone


# coffee bars list view
def coffee_bars_list_view(request):
    coffee_bars = CoffeeBar.objects.order_by("-avg_vote")[:10]
    context = {
        "list": coffee_bars,
        "auth": request.user,
    }
    return render(request, 'reviews/coffee_bars.html', context)


# coffee bars detail
def coffee_bars_detail(request, coffee_bar_id):
    coffee_bar = get_object_or_404(CoffeeBar, pk=coffee_bar_id)
    reviews = coffee_bar.review_set.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']
            rating = form.cleaned_data['rating']
            r = Review(author=request.user, coffee_bar=coffee_bar, vote=rating, description=description)
            r.save()

            count = 1
            voted = int(rating)
            for review in reviews:
                voted += review.vote
                count += 1
            coffee_bar.avg_vote = round(voted / count, 1)
            coffee_bar.save()

    else:
        form = ReviewForm()

    context = {
        'coffee_bar': coffee_bar,
        'reviews': reviews,
        "auth": request.user,
        "form": form
    }
    return render(request, 'reviews/coffee_bars_detail.html', context)


# register view
def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/reviews')
    else:
        form = SignUpForm()
    return render(request, 'reviews/register.html', {'form': form})


# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.user_cache)
            return redirect('/reviews')
    else:
        form = AuthenticationForm()
    return render(request, 'reviews/login.html', {'form': form})


# Logout view
def logout_view(request):
    logout(request)
    return redirect('/reviews')
