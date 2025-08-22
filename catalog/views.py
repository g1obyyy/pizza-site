from django.shortcuts import render
from .models import Pizza, Category


# Create your views here.
def menu(request, city=''):
    if city:
        pizzas = Pizza.objects.filter(city=city)
    else:
        pizzas = Pizza.objects.order_by("-cost")

    category = Category.objects.order_by("id")

    citys = set()
    for x in Pizza.objects.all():
        citys.add(x.city)
    citys=list(citys)
    citys.sort()

    isNone = set()
    for x in category:
        flag=False
        for pizza in pizzas:
            if x in pizza.category.all():
                flag=True
        if flag==False:
            isNone.add(x)
    print(isNone)

    return render(request, 'catalog/menu.html', {"pizzas": pizzas, "city": city, "category": category, 'citys':citys, 'isNone':isNone})


def idint(request, ident=None, category=None, city=None):
    obj = Pizza.objects.get(id=ident)
    pizza = {
        'tittle': obj.tittle,
        'description': obj.description,
        'cost': obj.cost,
        'city': obj.city,
        'sale': obj.sale,
        'img': obj.img,
        'protein': obj.protein,
        'fats': obj.fats,
        'carbon': obj.carbon,
        'calories': obj.calories
    }
    return render(request, 'catalog/id.html', pizza)
