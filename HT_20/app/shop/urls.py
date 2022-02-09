from django.urls import path

from .views import user_login, product_list, product_detail, edit_product, add_to_cart, remove_product

app_name = 'shop'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('product/', product_list, name='product_list'),
    path('product/<int:id>/', product_detail, name='product_detail'),
    path('product/edit/<int:id>', edit_product, name='edit'),
    path('product/add_to_cart/<int:id>', add_to_cart, name='cart'),
    path('product/remove/<int:id>', remove_product, name='remove'),
    ]
