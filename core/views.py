from django.shortcuts import render, redirect
from django.contrib.auth import logout

from item.models import Category, Item

from .forms import SignupForm

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[:8]
    categories = Category.objects.all()[:4]
    
    context = {
        'items': items,
        'categories': categories
    }
    
    return render(request, 'core/index.html', context)


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login')
        
    else:    
        form = SignupForm()
    
    return render(request, 'core/signup.html', {
        'form': form
    })
    
    
def logout_view(request):
    logout(request)
    return redirect('core:index')