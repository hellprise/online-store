from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from products.models import ProductCategory, Product, Basket


def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):
    context = {
        'title': 'Каталог',
        'categories': ProductCategory.objects.all(),
    }
    if category_id: # здесь мы начинаем код, который поможет фильтровать товары в шаблоне при клике пользователем на опреденённый фильтр
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all() # тут заканчивается
    paginator = Paginator(products, per_page=3) # per_page позволяет выводить выбранное кол-во товаров на странице.
    products_paginator = paginator.page(page) # page, которая в скобках говорит о том, что при переходе на страницу
    context.update({'products': products_paginator})
    # с товарами будем прогружена первая страница, ибо мы указали в параметрах ф-ции products значение по умолчанию 1.
    return render(request, 'products/products.html', context)


@login_required
def basket_add(request, product_id):
    current_page = request.META.get('HTTP_REFERER')

    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(current_page)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(current_page)


@login_required
def basket_delete(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))