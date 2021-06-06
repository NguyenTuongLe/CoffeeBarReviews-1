from django.contrib.auth import login, authenticate, logout
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import CoffeeBar
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.views import generic
from django.utils import timezone

        
# coffee bars list view
def coffee_bars_list_view(request):
    coffee_bars = CoffeeBar.objects.order_by("-created_at").all()
    context = {
        "list": coffee_bars,
        "auth": request.user,
    }
    return render(request, 'reviews/coffee_bars.html', context)


# coffee bars detail
def coffee_bars_detail(request, coffeeBar_id):
    coffeeBar = get_object_or_404(CoffeeBar, pk=coffeeBar_id)
    return render(request, 'reviews/coffee_bars_detail.html', {'coffeeBar': coffeeBar})
  

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
