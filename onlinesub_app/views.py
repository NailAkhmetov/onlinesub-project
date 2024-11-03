from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Subscription, Guide
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm

def home_page(request):
    categories = Category.objects.all()[:4]
    subscriptions = Subscription.objects.all().order_by('-created_at')[:4]

    context = {
        'categories': categories,
        'subscriptions': subscriptions
    }

    return render(request, "./home.html", context)

def subscriptions_page(request):
    subscriptions = Subscription.objects.all().order_by('-created_at')
    context = {
        'subscriptions': subscriptions
    }
    return render(request, "./subscriptions.html", context)

def categories_page(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, "./categories.html", context)

def guides_page(request):
    guides = Guide.objects.all()
    context = {
        'guides': guides
    }
    return render(request, "./guides.html", context)

def subscription_detail_page(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    context = {
        'subscription': subscription
    }
    return render(request, "./subscription-detail.html", context)

def guide_detail_page(request, pk):
    guide = get_object_or_404(Guide, pk=pk)
    context = {
        'guide': guide
    }
    return render(request, "./guide-detail.html", context)

def subscriptions_by_category_page(request, slug):
    category = get_object_or_404(Category, slug=slug)
    subscriptions = Subscription.objects.filter(category=category)
    context = {
        'category': category,
        'subscriptions': subscriptions
    }
    return render(request, "./subscriptions_by_category.html", context)


def sign_up_page(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login_page')
    else:
        form = NewUserForm()
    context = {
        'form': form
    }
    return render(request, "./sign-up.html", context)

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_page')
    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request, "./login.html", context)

def logout_action(request):
    logout(request)
    return redirect('home_page')
