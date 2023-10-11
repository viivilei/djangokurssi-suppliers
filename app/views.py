from django.shortcuts import render, redirect
from .models import Supplier, Product, Customer, Store
from django.contrib.auth import authenticate, login, logout

#tätä ei nyt sitten enää tarvita
def landingview(request):
   return render(request, 'landingpage.html')

# Loginpage
def loginview(request):
    return render (request, "loginpage.html")

# Login action
def login_action(request):
    user = request.POST['username']
    passw = request.POST['password']
    # Löytyykö kyseistä käyttäjää?
    user = authenticate(username = user, password = passw)
    #Jos löytyy:
    if user:
        # Kirjataan sisään
        login(request, user)
        # Tervehdystä varten context
        context = {'name': user.first_name}
        # Kutsutaan suoraan landingview.html
        return render(request,'landingpage.html',context)
    # Jos ei kyseistä käyttäjää löydy
    else:
        return render(request, 'loginerror.html')


# Logout action
def logout_action(request):
    logout(request)
    return render(request, 'loginpage.html')

#Product views, if else looppi asettaa eston, ettei kirjautumatta pääse livahtamaan tälle sivulle
def productlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        productlist = Product.objects.all()
        supplierlist = Supplier.objects.all()
        context = {'products': productlist, 'suppliers': supplierlist}
        return render (request, "productlist.html",context)

def addproduct(request):
    a = request.POST['productname']
    b = request.POST['packagesize']
    c = request.POST['unitprice']
    d = request.POST['unitsinstock']
    e = request.POST['supplier']
    
    Product(productname = a, packagesize = b, unitprice = c, unitsinstock = d, supplier = Supplier.objects.get(id = e)).save()
    return redirect(request.META['HTTP_REFERER'])


def confirmdeleteproduct(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        product = Product.objects.get(id = id)
        context = {'product': product}
        return render (request,"confirmdelprod.html",context)


def deleteproduct(request, id):
    Product.objects.get(id = id).delete()
    return redirect(productlistview)

def edit_product_get(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        product = Product.objects.get(id = id)
        context = {'product': product}
        return render (request,"edit_product.html",context)


def edit_product_post(request, id):
        item = Product.objects.get(id = id)
        item.unitprice = request.POST['unitprice']
        item.unitsinstock = request.POST['unitsinstock']
        item.save()
        return redirect(productlistview)

def products_filtered(request, id):
    productlist = Product.objects.all()
    filteredproducts = productlist.filter(supplier = id)
    context = {'products': filteredproducts}
    return render (request,"productlist.html",context)




#Supplier views
def supplierlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        supplierlist = Supplier.objects.all()
        context = { 'suppliers': supplierlist}
        return render (request, "supplierlist.html",context)


def addsupplier(request):
    a = request.POST['companyname']
    b = request.POST['contactname']
    c = request.POST['address']
    d = request.POST['phone']
    e = request.POST['email']
    f = request.POST['country']
    Supplier(companyname = a, contactname = b, addres = c, phone = d, email = e, country = f).save()
    return redirect(request.META['HTTP_REFERER'])

def confirmdeletesupplier(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        supplier = Supplier.objects.get(id = id)
        context = {'supplier': supplier}
        return render (request,"confirmdelsupp.html",context)


def deletesupplier(request, id):
    Supplier.objects.get(id = id).delete()
    return redirect(supplierlistview)

def searchsuppliers(request):
    search = request.POST['search']
    filtered = Supplier.objects.filter(companyname__icontains=search)
    context = {'suppliers': filtered}
    return render (request,"supplierlist.html",context)

def edit_supplier_get(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        supplier = Supplier.objects.get(id = id)
        context = {'supplier': supplier}
        return render (request,"edit_supplier.html",context)


def edit_supplier_post(request, id):
        item = Supplier.objects.get(id = id)
        item.phone = request.POST['phone']
        item.addres = request.POST['address']
        item.save()
        return redirect(supplierlistview)

#Customer views

def customerlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        customerlist = Customer.objects.all()
        context = { 'customers': customerlist}
        return render (request, "customerlist.html",context)

def addcustomer(request):
    a = request.POST['customername']
    b = request.POST['contactname']
    c = request.POST['address']
    d = request.POST['phone']
    e = request.POST['email']
    f = request.POST['country']
    Customer(customername = a, contactname = b, addres = c, phone = d, email = e, country = f).save()
    return redirect(request.META['HTTP_REFERER'])

def edit_customer_get(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        customer = Customer.objects.get(id = id)
        context = {'customer': customer}
        return render (request,"edit_customer.html",context)


def edit_customer_post(request, id):
        item = Customer.objects.get(id = id)
        item.phone = request.POST['phone']
        item.addres = request.POST['address']
        item.save()
        return redirect(customerlistview)

def confirmdeletecustomer(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        customer = Customer.objects.get(id = id)
        context = {'customer': customer}
        return render (request,"confirmdelcust.html",context)


def deletecustomer(request, id):
    Customer.objects.get(id = id).delete()
    return redirect(customerlistview)


#Store views

def storelistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        storelist = Store.objects.all()
        context = { 'stores': storelist}
        return render (request, "storelist.html",context)

def addstore(request):
    a = request.POST['storename']
    b = request.POST['contactname']
    c = request.POST['address']
    d = request.POST['phone']
    e = request.POST['email']
    f = request.POST['country']
    Store(storename = a, contactname = b, addres = c, phone = d, email = e, country = f).save()
    return redirect(request.META['HTTP_REFERER'])

def edit_store_get(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        store = Store.objects.get(id = id)
        context = {'store': store}
        return render (request,"edit_store.html",context)


def edit_store_post(request, id):
        item = Store.objects.get(id = id)
        item.contactname = request.POST['contactname']
        item.save()
        return redirect(storelistview)

def confirmdeletestore(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        store = Store.objects.get(id = id)
        context = {'store': store}
        return render (request,"confirmdelsto.html",context)


def deletestore(request, id):
    Store.objects.get(id = id).delete()
    return redirect(storelistview)

