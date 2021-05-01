import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from Pizzeria.models import Pizza, Topping

pizza = Pizza.objects.all()

for pizza in pizza:
    print(pizza.id, pizza.name)

toppings = Pizza.name.all()

for topping in toppings:
    print(topping)
