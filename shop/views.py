from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FeedbackForm

DATA = [
    {"id": 1, "name": "Ноутбук Pro 15 ігровий потужний", "price": 45000, "in_stock": True},
    {"id": 2, "name": "Миша Wireless G бездротова", "price": 1200, "in_stock": True},
    {"id": 3, "name": "Клавіатура Mech механічна", "price": 3500, "in_stock": False},
]

def index(request):
    return render(request, 'shop/index.html', {
        'title': 'Головна сторінка',
        'site_name': 'TechStore Django',
        'items_count': len(DATA),
        'now': datetime.now(),
    })

def catalog(request):
    return render(request, 'shop/catalog.html', {
        'title': 'Каталог товарів',
        'items': DATA,
        'now': datetime.now(),
    })

def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            messages.success(request, "Ваше повідомлення успішно надіслано!")
            return redirect('contact')
    else:
        form = FeedbackForm()
    
    return render(request, 'shop/contact.html', {
        'title': "Зворотний зв'язок",
        'form': form,
        'now': datetime.now(),
    })