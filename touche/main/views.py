from django.shortcuts import render
from gallery.models import *
from menu.models import *
from chefs.models import *
from .forms import ContactForm
from .models import Contact
# Create your views here.


def index(request):
    error_form = ''

    if request.method == 'POST':
        contact = ContactForm(request.POST)
        print(request.POST)
        if contact.is_valid():
            contact.save()
        else:
            error_form = 'неверные данные'

    gallery_cat = Categorie.objects.all()
    gallery = Gallery.objects.all()
    cat_dish = CategorieDish.objects.all()
    dish = Dish.objects.all()
    chef = Chef.objects.all()
    contact = ContactForm
    feedbacks = Contact.objects.all()
    menu = {
        'About': 'about',
        'Gallery': 'portfolio',
        'Chefs': 'team',
        'Contact': 'call-reservation'
    }
    data = {
        'gallery_cat': gallery_cat,
        'gallery': gallery,
        'title': 'Main Page',
        'icon': 'static/img/favicon.ico',
        'menu': menu,
        'phone': '+375 (44) 710-68-86',
        'email': 'touch.@gmail.com',
        'about_image': 'static/img/about.jpg',
        'cat_dish': cat_dish,
        'dish': dish,
        'chef': chef,
        'contact': contact,
        'error_form': error_form,
        'feedbacks': feedbacks

    }
    return render(request, 'main/index.html', data)
