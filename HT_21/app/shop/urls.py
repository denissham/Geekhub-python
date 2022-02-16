from django.urls import path, include

from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'category', CategoryViewSet, basename='category')


app_name = 'shop'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('', product_list, name='product_list'),
    path('product/<int:id>/', product_detail, name='product_detail'),
    path('product/edit/<int:id>', edit_error, name='edit'),
    path('product/add-to-cart', add_to_cart, name='add_to_cart'),
    path('product/remove/<int:id>', remove_product_error, name='remove'),
    path('logout/', user_logout, name='logout'),
    path('category/<str:category>', show_categories, name='category'),
    path('api/', include(router.urls)),
    path('cart/', cart, name='cart'),
    ]

