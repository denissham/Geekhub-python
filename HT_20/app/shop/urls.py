from django.urls import path

from .views import show_categories ,remove_product_error, edit_error, user_login, product_list, product_detail, add_to_cart, user_logout

app_name = 'shop'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('', product_list, name='product_list'),
    path('product/<int:id>/', product_detail, name='product_detail'),
    path('product/edit/<int:id>', edit_error, name='edit'),
    path('product/add_to_cart/<int:id>', add_to_cart, name='cart'),
    path('product/remove/<int:id>', remove_product_error, name='remove'),
    path('logout/', user_logout, name='logout'),
    path('category/<str:category>', show_categories, name='category'),
    ]


# edit_error