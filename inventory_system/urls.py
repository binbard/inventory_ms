"""
URL configuration for inventory_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("products/add/", views.add_product, name="add_product"),
    path("products/", views.list_products, name="list_products"),
    path("suppliers/add/", views.add_supplier, name="add_supplier"),
    path("suppliers/", views.list_suppliers, name="list_suppliers"),
    path("sale_orders/add/", views.create_sale_order, name="create_sale_order"),
    path('sale_order/update_status/<int:order_id>/', views.update_sale_order_status, name='update_sale_order_status'),
    path("sale_orders/", views.list_sale_orders, name="list_sale_orders"),
    path("stock_movements/", views.stock_movements, name="stock_movements"),
    path("check_stock_level/", views.stock_level_check, name="check_stock_level"),
]
