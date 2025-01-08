from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from user import views as user_views
from Locker_Api import views as locker_views  # Import the Locker_Api views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', locker_views.index, name='Locker_Api-index'),  # Root URL mapped to Locker_Api index view
    path('index/', locker_views.index, name='Locker_Api-index'),
    path('products/', locker_views.products, name='Locker_Api-products'),
    path('products/delete/<int:pk>/', locker_views.product_delete, name='Locker_Api-products-delete'),
    path('products/detail/<int:pk>/', locker_views.product_detail, name='Locker_Api-products-detail'),
    path('products/edit/<int:pk>/', locker_views.product_edit, name='Locker_Api-products-edit'),
    path('customers/', locker_views.customer_list, name='Locker_Api-customers'),
    path('customers/detail/<int:pk>/', locker_views.customer_detail, name='Locker_Api-customer-detail'),
    path('order/', locker_views.order_list, name='Locker_Api-order'),
    path('register/', user_views.register, name='user-register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='user-logout'),
    path('profile/', user_views.profile, name='user-profile'),
    path('profile/update/', user_views.profile_update, name='user-profile-update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
