from django.contrib import admin

from app.models import Supplier, Product, Customer
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

