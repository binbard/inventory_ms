from django.contrib import admin
from .models import Supplier, Product, StockMovement, SaleOrder

admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(StockMovement)
admin.site.register(SaleOrder)
