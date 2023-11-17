from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.forms.models import model_to_dict

def home(request, homepage_id=None, event_id=None):
    events = Event.objects.all()
    if event_id:
            events = events.filter(event_id=event_id)
            
    return render(request,'app/home.html', {'events': events} )

def about(request):
    return render(request,'app/about.html')


def catalog(request, category_id=None):
    categories = Category.objects.all()
    products = Product.objects.all()
    
    if category_id:
        products = products.filter(category_id=category_id)
    
    return render(request,'app/catalog.html', {'products': products, 'categories': categories} )

from django.http import JsonResponse


def filtered_products(request, category_id):
    try:
        if category_id:
            products = Product.objects.filter(categories__id=category_id)
        else:
            products = Product.objects.all()

        # Construire une liste de dictionnaires à partir des objets Product
        products_data = []
        for product in products:
        #Filtre si une remise est associée au produit
            discount = Discount.objects.filter(product=product).first()
            
            product_dict = {
                'name': product.name,
                'description': product.description,
                'initial_price': product.initial_price,
                'thumbnail_url': product.thumbnail.url,  
                'discount': {
                    'active': discount.active if discount else None,
                    'discounted_price': discount.discounted_price if discount else None,
                    'discount_percentage': discount.discount_percentage if discount else None,
                },
            }
            products_data.append(product_dict)

        # Renvoyer la réponse JSON
        return JsonResponse({'products': products_data})
    except Exception as e:
        # En cas d'erreur, renvoyer une réponse JSON avec le message d'erreur
        return JsonResponse({'error': str(e)}, status=500)
