from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField()
    image = models.FileField()
    category = models.CharField(max_length=100,null=True)
    numStock = models.IntegerField()
    discount = models.FloatField(null=True)
    color = models.CharField(max_length=100,null=True)
    isNew = models.BooleanField(null=True)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField()
    transaction_id = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 
    

class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=0)
    date_add = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        total = self.product.price*self.quantity
        return total
    
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address = models.CharField(max_length=1000,null=True)
    city = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address
    


