from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='Locker_Api-index'),
    path('products/', views.products, name='Locker_Api-products'),
    path('products/delete/<int:pk>/', views.product_delete, name='Locker_Api-products-delete'),
    path('products/detail/<int:pk>/', views.product_detail, name='Locker_Api-products-detail'),
    path('products/edit/<int:pk>/', views.product_edit, name='Locker_Api-products-edit'),
    path('customers/', views.customer_list, name='Locker_Api-customers'),  # Changed to match view function name
    path('customers/detail/<int:pk>/', views.customer_detail, name='Locker_Api-customer-detail'),
    path('order/', views.order_list, name='Locker_Api-order'),  # Changed to match view function name
]