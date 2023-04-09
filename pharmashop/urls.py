from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index/',views.index, name='index'),
    path('about/',views.home, name='about'),
    path('home/',views.home, name='home'),
    path('',auth_views.LoginView.as_view(template_name='products/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='products/logout.html'), name='logout'),
    path('index/<int:product_id>', views.product_detail, name='product_detail'),
    path('issued_item/<str:pk>/', views.issued_item, name='issued_item'),
    path('add_to_stock/<str:pk>/', views.add_to_stock, name='add_to_stock'),
    path('reciept', views.reciept, name='reciept'),#handle a reciept after a successful sale
    path('all_sales', views.all_sales, name ='all_sales'),#handles all all_sales from the browser
    path('reciept_detail/<int:reciept_id>/', views.reciept_detail, name ='reciept_detail'),
]

