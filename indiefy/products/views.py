from itertools import product

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.template.context_processors import request

from .models import *
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.http import HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist

@login_required(login_url='login')
def home(request):
    categories=ProductType.objects.all()
    return render(request,'products/index.html',{'categories':categories})
@login_required(login_url='login')
def state(request):
    state=StateCategory.objects.all()
    return render(request,'products/state.html',{'state':state})
@login_required(login_url='login')
def subcategories_by_state(request, state_id):
    state = get_object_or_404(StateCategory, id=state_id)
    subcategories = substate.objects.filter(state_category=state)  # Get all subcategories for this state
    return render(request, 'products/state_products.html', {
        'state': state,
        'subcategories': subcategories
    })
@login_required(login_url='login')
def products_by_subcategory(request, subcategory_id):
    subcategory = get_object_or_404(substate, id=subcategory_id)
    products = Product.objects.filter(sub_type=subcategory,stock=True)  # Get all products for this subcategory
    return render(request, 'products/products_by_subcategory.html', {
        'subcategory': subcategory,
        'products': products
    })
@login_required(login_url='login')
def product_type_products(request, product_type_id):
    product_type = get_object_or_404(ProductType, id=product_type_id)
    products = Product.objects.filter(product_type=product_type, stock=True)
    return render(request, 'products/category_products.html', {
        'product_type': product_type,
        'products': products
    })
@login_required(login_url='login')
def iteminc(request, pid):
    user=request.user
    car=get_object_or_404(cart,user=user)
    pro=get_object_or_404(Product,id=pid)
    obj=get_object_or_404(cartitem,cart=car,product=pro)
    obj.quantity+=1
    obj.save()

    return redirect('details',pid)
@login_required(login_url='login')
def itemdec(request, pid):
    user=request.user
    car=get_object_or_404(cart,user=user)
    pro=get_object_or_404(Product,id=pid)
    obj=get_object_or_404(cartitem,cart=car,product=pro)
    obj.quantity-=1
    obj.save()
    if obj.quantity==0:
        obj.delete()
    return redirect('details',pid)
def iteminc1(request, pid):
    user=request.user
    car=get_object_or_404(cart,user=user)
    pro=get_object_or_404(Product,id=pid)
    obj=get_object_or_404(cartitem,cart=car,product=pro)
    obj.quantity+=1
    obj.save()

    return redirect('cartdetails')
@login_required(login_url='login')
def itemdec1(request, pid):
    user=request.user
    car=get_object_or_404(cart,user=user)
    pro=get_object_or_404(Product,id=pid)
    obj=get_object_or_404(cartitem,cart=car,product=pro)
    obj.quantity-=1
    obj.save()
    if obj.quantity==0:
        obj.delete()
    return redirect('cartdetails')
@login_required(login_url='login')
def details(request, product_id):
    user = request.user
    obj = cart.objects.filter(user=user).first()
    product = get_object_or_404(Product, id=product_id)
    cartu = cartitem.objects.filter(cart=obj, product=product).first()
    return render(request, 'products/details.html', {'product': product, 'cartu': cartu})
@login_required(login_url='login')
def deletecart(request, pid):
    user = request.user
    pro=get_object_or_404(Product,id=pid)
    obj=get_object_or_404(cart,user=user)
    obj2=get_object_or_404(cartitem,cart=obj,product=pro)
    obj2.delete()
    return redirect('details',pid)
@login_required(login_url='login')
def deletecart1(request, pid):
    user = request.user
    pro=get_object_or_404(Product,id=pid)
    obj=get_object_or_404(cart,user=user)
    obj2=get_object_or_404(cartitem,cart=obj,product=pro)
    obj2.delete()
    return redirect('cartdetails')
@login_required(login_url='login')
def cartdetails(request):
    user = request.user
    obj1=cart.objects.filter(user=user).first()
    obj2=cartitem.objects.filter(cart=obj1)
    total=0
    for i in obj2:
        total+=i.product.price*i.quantity
    return render(request,'products/cart.html',{'obj2':obj2,'total':total})
@login_required(login_url='login')
def addcart(request, pid):
    user = request.user
    pro=get_object_or_404(Product,id=pid)
    obj=get_object_or_404(cart,user=user)
    if obj is None:
        obj.save()
    obj2=cartitem.objects.create(cart=obj,product=pro)
    obj2.save()
    return redirect('details',pid)

def userreg(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'products/register.html', context)


def slogin2(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user1 = authenticate(request, username=username, password=password)
            if user1 is not None:
                try:
                    user2 = seller.objects.get(user=user1)
                    login(request, user1)
                    return redirect('dashboard')
                except ObjectDoesNotExist:
                    messages.error(request, 'User is not a seller')
                except Exception as e:
                    messages.error(request, f'An error occurred: {str(e)}')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Form is invalid')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'products/login.html', {'form': form})

def slogin(request):
    user = request.user
    obj = seller.objects.filter(user=user)
    if obj is not None:
        if request.method == "POST":
            form = CustomAuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                user2 = get_object_or_404(seller,user=user)
                if user is not None and user2 is not None:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    messages.error(request,'Please enter the correct credentials')
                    return redirect('slogin')
        form = CustomAuthenticationForm()
        return render(request, 'products/login.html',{'form':form})
    else:
        return redirect('cred')
def loginview(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request,'Please enter the correct credentials')
        else:
            messages.error(request,'Please enter the correct credentials')
    form = CustomAuthenticationForm()
    return render(request, 'products/login.html',{'form':form})
@login_required(login_url='login')
def cred(request):
    user = request.user
    user2 = seller.objects.filter(user=user)
    if not user2.exists():
        seller.objects.create(user=user)
        return redirect('sellerdetails')
    else:
        return render(request,'products/error.html')

@login_required(login_url='login')
def sellerdetails(request):
    if request.method == 'POST':
        user = request.user
        user2 = seller.objects.filter(user=user).first()
        mob = request.POST.get('mobile_number')
        aad = request.POST.get('aadhar_number')
        pan = request.POST.get('pan_number')
        user2.mobileno = mob
        user2.adharno = aad
        user2.panno = pan
        user2.save()
        return redirect('dashboard')
    else:
        user = request.user
        user2 = seller.objects.filter(user=user).first()
        return render(request,'products/cred.html',{'user2':user2})
@login_required(login_url='login')
def logoutview(request):
    logout(request)
    return redirect('login')
@login_required(login_url='slogin2')
def dashboard(request):
    user = request.user
    user2 = seller.objects.filter(user=user).first()
    if user2 is not None:
        return render(request,'products/sellerdashboard.html',{'user2':user2})
    else:
        return redirect('slogin2')
@login_required(login_url='slogin2')
def products(request):
    user = request.user
    user2 = seller.objects.filter(user=user).first()
    if user2 is not None:
        obj = Product.objects.filter(seller=user2)
        return render(request, 'products/products.html', {'user2': user2,'obj':obj})
    else:
        return redirect('slogin2')

@login_required(login_url='slogin2')
def addproducts(request):
    user = request.user
    user2 = seller.objects.filter(user=user).first()
    if user2 is not None:
        if request.method == 'POST':
            for image in request.FILES.getlist('images'):
                p1 = Product(
                    seller=user2,
                    name=request.POST.get('name'),
                    description=request.POST.get('description'),
                    price=request.POST.get('price'),
                    product_type=get_object_or_404(ProductType, name=request.POST.get('cat')),
                    sub_type=get_object_or_404(substate, name=request.POST.get('sub')),
                    image=image
                )
                p1.save()
            return redirect('products')  # Redirect after successful upload

        sub = substate.objects.all()
        category = ProductType.objects.all()
        return render(request, 'products/addproduct.html', {'user2': user2, 'sub': sub, 'category': category})
    else:
        return redirect('slogin2')

@login_required(login_url='slogin2')
def stocks(request, eid):
    obj = get_object_or_404(Product,id=eid)
    obj.stock = not obj.stock
    obj.save()
    return redirect('products')
@login_required(login_url='login')
def addresss(request):
    user = request.user
    u = address.objects.filter(user=user).first()
    if request.method=='POST':
        if u is None:
            street_address = request.POST.get("street1")
            city = request.POST.get("city")
            states = request.POST.get("states")
            zip_code = request.POST.get("zipcode")
            obj=address.objects.create(user=user,street_address=street_address,city=city,state=states,zip_code=zip_code)
            obj.save()
        else:
            u.street_address = request.POST.get("street1")
            u.city = request.POST.get("city")
            u.states = request.POST.get("states")
            u.zip_code = request.POST.get("zipcode")
            u.save()
        return redirect('payment')
    return render(request,'products/order.html',{'u':u})
@login_required(login_url='login')
def payment( request):
    users = request.user
    add=get_object_or_404(address,user=users)

    obj1=get_object_or_404(cart,user=users)
    obj2=cartitem.objects.filter(cart=obj1)
    for i in obj2:
        obj3=order.objects.create(buyer=users,product=i.product,seller=i.product.seller,address=add,quantity=i.quantity,total=i.quantity*i.product.price)
        obj3.save()
        i.delete()
    return render(request, 'products/payment.html')
@login_required(login_url='login')
def aboutus(request):
    return render(request,'products/aboutus.html')
@login_required(login_url='login')
def contact(request):
    user=request.user
    if request.method=="POST":
        obj = feeback.objects.create(user=user)
        obj.fname=request.POST.get('fname')
        obj.lname = request.POST.get('lname')
        obj.email = request.POST.get('email')
        obj.phone = request.POST.get('phone')
        obj.message = request.POST.get('fname')
        obj.save()
        messages.success(request,'Feedback submitted succesfully')
        return render(request, 'products/contact.html')
    return render(request,'products/contact.html')
@login_required(login_url='login')
def blog(request):
    return render(request,'products/blog.html')
@login_required(login_url='slogin2')
def sorders(request):
    user=request.user
    sell=get_object_or_404( seller ,user=user)
    ord=order.objects.filter(seller=sell)[::-1]
    return render(request,'products/sellerorders.html',{'ord':ord})