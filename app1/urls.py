from django.urls import path
from .views import home, productadd, product_list, product_view,category_list,category_product,product_with_product_varient

urlpatterns = [
    path('',home, name='home'),
    path('productlist/',product_list, name='product-list'),
    path('productadd/',productadd, name='productadd'),
    path('categorylist/', category_list,name='categorylist'),
    path('productview/<int:product_id>/view/',product_view,name='product_view'),
    path('categoryproduct/<int:category_id>/views',category_product,name='category_product'),
    path('productwithvarient/<int:product_id>/view/',product_with_product_varient,name='product_with_product_varient')
]