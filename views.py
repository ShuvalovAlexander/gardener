from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import FeedbackForm
from .forms import OrderForm
from django.core.mail import send_mail
from django.conf import settings
def index(request):
    form = FeedbackForm()
    return render(request, 'main/index.html', {'form': form})

def about(request):
    return render(request, 'main/about.html')

def katalog(request):
    products = Product.objects.all()
    return render(request, 'main/katalog.html', {'products': products})

def productCard(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    discount_percent = None
    if product.old_price and product.old_price > product.price:
        discount_percent = round((product.old_price - product.price) / product.old_price * 100)
    return render(request, 'main/productCard.html', {
        'product': product,
        'discount_percent': discount_percent,
    })

def kontact(request):
    return render(request, 'main/kontact.html')

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER', '/')) 
    return redirect(request.META.get('HTTP_REFERER', '/'))



def make_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save() 
            return render(request, 'main/thanks.html')  
    else:
        initial = {
            'product': request.GET.get('product', ''),
            'price': request.GET.get('price', ''),
        }
        form = OrderForm(initial=initial)
    return render(request, 'main/make_order.html', {'form': form})