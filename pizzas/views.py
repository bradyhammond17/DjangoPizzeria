from django.shortcuts import render
from .models import Pizza
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
    entries = pizza.toppings_set.order_by('-topping_name')

    context = {'pizza':pizza,'entries':entries}

    return render(request, 'pizzas/pizza.html', context)