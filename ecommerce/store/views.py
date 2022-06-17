from copyreg import constructor
from distutils.log import error
from ipaddress import summarize_address_range
from itertools import product
import json
from django.shortcuts import redirect, render
from .models import *
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import registerForm,loginForm
from django.views import View
from django.contrib.auth import authenticate,login,logout
# Create your views here.

class LoginUser(View):  
    def get(self,request):
        lgForm = loginForm()
        context = {
            'lgForm': lgForm
        }
        return render(request,'store/login.html',context)

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        try: 
            user = authenticate(request,username=User.objects.get(email=username),password=password)
        except:
            user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('store:home')
        else: 
            return HttpResponse('login false')


class RegisterUser(View):
    def get(self, request):
        rgForm = registerForm
        context = {
            'rgForm': rgForm
        }
        return render(request,'store/register.html',context)

    def post(self, request):
        if request.method == 'POST':
            rgForm = registerForm(request.POST)
            if rgForm.is_valid():
                username = request.POST['username']
                email = request.POST['email']
                password = request.POST['password']
                user = User.objects.create_user(username,email,password)
                user.save()
            context = {
                'rgForm': rgForm
                    }
            return render(request,'store/login.html',context)  
        else:
            return HttpResponse('falure')


def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer ,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        customer = None
        order = {'get_cart_total':0,'get_cart_items':0}
        cartItems = order['get_cart_items']
        
        
    products = Product.objects.all()
        
        
    context = {
        'products': products,
        'items': items,
        'order': order,
        'customer': customer,
        'categoryId': 0
    }
    return render(request,'store/store.html',context)
    
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer ,complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
        
    context = {'items':items , 'order': order}
    return render(request,'store/cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer ,complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
        
    context = {'items':items , 'order': order}
    return render(request,'store/checkout.html',context)  

def updateItem(request):
    data = json.loads(request.body.decode("utf-8"))
    productId = data['productId']
    action = data['action']
    print('Action: ', action)
    print('Product: ', productId)
    
    customer = request.user.customer 
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer = customer, complete = False)
    orderItem, created = OrderItem.objects.get_or_create(order = order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1) 
    
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse({'status':'Item was add'}, safe=False)

class logoutUser(View):
    def get(self, request):
        logout(request)
        return redirect('store:home')

def storeCategory(request,id):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer ,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        customer = None
        order = {'get_cart_total':0,'get_cart_items':0}
        cartItems = order['get_cart_items']
        
        
    products = Product.objects.all()
    
    if id==1: 
        products = Product.objects.all().filter(category='shoes')
    elif id==2: 
        products = Product.objects.all().filter(category='bag')
    elif id==3: 
        products = Product.objects.all().filter(category='shirt')
    elif id==4: 
        products = Product.objects.all().filter(category='skirt')
    else: 
        products = Product.objects.all()
        
    context = {
        'products': products,
        'items': items,
        'order': order,
        'customer': customer,
        'categoryId': id
    }
    return render(request,'store/store.html',context)   

def detail(request,id):
    product = Product.objects.get(id=id)
    context = {
        'product': product
    }
    return render(request, 'store/detail.html',context)

    