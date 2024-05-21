from django.shortcuts import render, redirect, get_object_or_404
from .models import Tour, Category, AirCategory
from .forms import TourForm

def index(request):
    category = Category.objects.all()
    aircategory = AirCategory.objects.all()
    context = {
        'category': category,
        'aircategory': aircategory
    }
    return render(request, 'index.html', context)

def about(request):
    category = Category.objects.all()
    aircategory = AirCategory.objects.all()
    context = {
        'category': category,
        'aircategory': aircategory
    }
    return render(request, 'about.html', context)   


def gallery(request):
    return render(request, 'gallery.html')

def batafsil(request, id):
    product = get_object_or_404(Tour, id=id)
    categories = Category.objects.all()
    tour = Tour.objects.all()
    context = {
        'product': product,
        'categories': categories,
        'tour': tour
    }
    return render(request, 'batafsil.html', context)

def home(request):
    products = Tour.objects.all()
    categories = Category.objects.all()
    aircategory = AirCategory.objects.all()

    selected_destination = request.GET.get('travel_destination')
    selected_type = request.GET.get('travel_type')

    if selected_destination:
        products = products.filter(category__aircategory__id=selected_destination)

    if selected_type:
        products = products.filter(category__id=selected_type)

    context = {
        'category': categories,
        'aircategory': aircategory,
        'products': products,
    }

    return render(request, 'tour.html', context)

def category(request, id):
    cat = get_object_or_404(Category, id=id)
    products = cat.products.all()
    categories = Category.objects.all()
    return render(request, 'tour.html', {"products": products, "cats": categories})

def product_list(request):
    products = Tour.objects.all()
    return render(request, 'tour.html', {'products': products})

# Create
def product_create(request):
    count = TourForm()
    category = Tour.objects.all()
    if request.method == 'POST':
        count = TourForm(request.POST, request.FILES)
        if count.is_valid():
            count.save()
            return redirect('home')
    return render(request, template_name="product_form.html", context={"count": count, "cats":category})

# Update
def product_update(request, id):
    product = get_object_or_404(Tour, id=id)
    if request.method == 'POST':
        form = TourForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TourForm(instance=product)
    return render(request, 'product_form.html', {'count': form})

# Delete
def product_delete(request, id):
    product = get_object_or_404(Tour, id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'tour.html', {'product': product})






