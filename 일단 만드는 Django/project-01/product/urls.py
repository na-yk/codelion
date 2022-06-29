from django.urls import path
from product import views

urlpatterns = [
    path('',views.productlist), # 우리 사이트/products/
    path('first/',views.productfirst) # 우리사이트/products/first/
]