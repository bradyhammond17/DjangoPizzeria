from django.shortcuts import render
from .models import Pizza, Toppings
# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.all()


    context = {'pizzas': pizzas}


    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    ## view must be consistent with url
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.toppings_set.order_by('-topping_name')

    context = {'pizza': pizza, 'toppings': toppings}

    return render(request, 'pizzas/pizza.html', context)