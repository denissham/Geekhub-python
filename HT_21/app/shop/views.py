import json

from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse

from rest_framework import viewsets

from .models import Category, Product
from .forms import LoginForm, EditProduct
from .serializers import ProductSerializer, CategorySerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            user = authenticate(
                username=form_data['username'],
                password=form_data['password']
            )
            if user:
                if user.is_active:
                    superusers = User.objects.filter(is_superuser=True)
                    if user in superusers:
                        request.session['role'] = "superuser"
                    else:
                        request.session['role'] = "user"
                    login(request, user)
                    return HttpResponseRedirect('../', user)
                else:
                    messages.error(request, 'You can not login')
                    return redirect('/login')
            else:
                messages.error(request, 'Invalid username or Password')
                return redirect('/login')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'shop/login.html', context)


def product_list(request):
    products = Product.objects.filter(is_active=True)
    role = request.session.get('role')
    print(dict(request.session))
    return render(request,
              'shop/product/list.html',
                  locals()
             )


def product_detail(request, id):
    product = get_object_or_404(Product, id=id, is_active=True)
    role = request.session.get('role')
    return render(request, 'shop/product/details.html', locals())


def edit_error(request, id):
    if request.user.is_anonymous:
        messages.warning(request, 'You must be a superuser to edit product')
    return edit_product(request, id)


@login_required(login_url='../../')
def edit_product(request, id):
    user = request.user
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = EditProduct(request.POST)
        if user.is_superuser:
            if form.is_valid:
                product.name = request.POST["name"]
                product.description = request.POST["description"]
                product.sku = request.POST["sku"]
                product.price = request.POST["price"]
                product.save()
                url = f'/../product/{id}'
                messages.success(request, "Data inserted successfully")
                return redirect(url)

        else:
            messages.error(request, 'You are not a superuser')
            return redirect('/product')

    else:
        form = EditProduct(initial={'name': product.name,
                                 'description': product.description,
                                 'price': product.price,
                                 'sku': product.sku})
        return render(request, 'shop/product/edit.html', {'form': form})


def remove_product_error(request, id):
    if request.user.is_anonymous:
        messages.warning(request, 'You must be a superuser to remove product')
    return remove_product(request, id)


@login_required(login_url='../../')
def remove_product(request, id):
    user = request.user
    product = Product.objects.get(id=id)
    if user.is_superuser:
        product.delete()
        messages.success(request, "Item Deleted")
        return HttpResponseRedirect('../', id)


@login_required(login_url='../../')
def add_to_cart(request):
    product_id = request.POST.get('product_id')
    if product_id:
        product = Product.objects.get(id=product_id)
        cart = request.session.setdefault('cart', {})
        products = cart.setdefault('products', [])
        products.append(product_id)
        cart_total = cart.get('total') or 0
        product.quantity -= 1
        product.save()
        cart['total'] = cart_total + round(float(product.price), 2)
        request.session.modified = True
        messages.success(request, f"Item Added to cart, total $ {request.session['cart']['total']}")
        return redirect("../")
    return JsonResponse({"error": 'product.quantity'})


def cart(request):
    try:
        id_products = request.session['cart']['products']
        print(len(id_products))
        cart_list = []
        product_quantity = {}
        for j in id_products:
            product = Product.objects.get(id=j)
            if product.name in product_quantity:
                product_quantity[product.name] += 1
            else:
                cart_list.append(product)
                product_quantity[product.name] = 1
        return render(request, "shop/product/cart.html", {'cart_products': cart_list,
                                                          'product_quantity': product_quantity})
    except:
        return render(request, "shop/product/cart.html", {'cart_products': None,
                                                          'product_quantity': None})


def user_logout(request):
    logout(request)
    return render(request, 'shop/logged_out.html')


def show_categories(request, category):
    products = Product.objects.filter(is_active=True)
    category_name = get_object_or_404(Category, name=category)
    products = products.filter(category_fk=category_name)
    role = request.session.get('role')
    return render(request,
                  'shop/product/list.html',
                  locals()
                  )

