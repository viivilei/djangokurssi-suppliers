from django.urls import path

from .views import landingview, productlistview, supplierlistview, addsupplier, addproduct, \
    deleteproduct, confirmdeleteproduct, deletesupplier, confirmdeletesupplier, edit_product_get, \
    edit_product_post, searchsuppliers, products_filtered, loginview, login_action, logout_action, \
    customerlistview, addcustomer, storelistview, addstore, edit_customer_get, edit_customer_post

urlpatterns = [
   #Landing page after login
   path('landing/', landingview),

   #Login view and authentication method
   path('', loginview),
   path('login/', login_action),
   path('logout/', logout_action),

   path('products/', productlistview),
   path('add-product/', addproduct),
   path('delete-product/<int:id>/', deleteproduct),
   path('confirm-delete-product/<int:id>/', confirmdeleteproduct),
   path('edit-product-get/<int:id>/', edit_product_get),
   path('edit-product-post/<int:id>/', edit_product_post), 
   path('products-by-supplier/<int:id>/', products_filtered),


   path('suppliers/', supplierlistview),
   path('add-supplier/', addsupplier),
   path('delete-supplier/<int:id>/', deletesupplier),
   path('confirm-delete-supplier/<int:id>/', confirmdeletesupplier),
   path('search-suppliers/', searchsuppliers),

   path('customers/', customerlistview),
   path('add-customer/', addcustomer),
   path('edit-customer-get/<int:id>/', edit_customer_get),
   path('edit-customer-post/<int:id>/', edit_customer_post), 

   path('stores/', storelistview),
   path('add-store/', addstore)
   

]
