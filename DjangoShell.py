import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from pizzas.models import Pizza

pizzas = Pizza.objects.all()

for p in pizzas:
    print(p.id, ' ', p.pizza_name)

p = Pizza.objects.get(id = 1)

print(p.pizza_name)


entries = p.toppings_set.all()

for e in entries:
    print(e.topping_name)