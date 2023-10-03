from django.db import models

# Create your models here.

    
class People(models.Model):
    first_name= models.CharField(max_length=50,null=False,default='')
    lastName= models.CharField(max_length=50,null=False,default='')
    username= models.CharField(max_length=50,null=False,default='')
    email=models.CharField(max_length=200,null=False,default='')
    password=models.CharField(max_length=20,null=False,default='')
 
    def __str__(self):
        return self.email
    
class login(models.Model):
    email=models.CharField(max_length=200,null=False,default='')
    password=models.CharField(max_length=20,null=False,default='')
 
    def __str__(self):
        return 
    
    
class signup(models.Model):
    email=models.CharField(max_length=200,null=False,default='')
    name=models.CharField(max_length=200,null=False,default='')
    phone=models.CharField(max_length=200,null=False,default='')
    password=models.CharField(max_length=20,null=False,default='')
 
    def __str__(self):
        return 
    
    # male,female or kids category
class Category(models.Model):
    category_name = models.CharField(max_length=30)
    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    shopName=models.CharField(max_length=200,null=False,default='ShopName')
    contact=models.CharField(max_length=200,null=False,default='')
    brand=models.CharField(max_length=200,null=False,default='Brand name')
    price=models.IntegerField(null=False)
    color=models.CharField(max_length=10)
    size=models.IntegerField(null=True)
    quantity=models.IntegerField(null=False,default=1)
    image=models.ImageField(null=True,upload_to='media')
    catogory  = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return  self.brand
    

  

class Cart(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    person_id = models.ForeignKey(People, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return  self.product_id
