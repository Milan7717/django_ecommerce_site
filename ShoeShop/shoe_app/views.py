from django.shortcuts import render,redirect
from django.contrib import messages

from shoe_app.models import People,Product,Cart
# from .models import Category
# Create your views here.
def home(request):
    return render(request,'home.html')

def categories(request):
    return render(request,'categories.html')



def kids(request):

    kids_products  = Product.objects.filter(catogory=3)
    print(kids_products)
    context = {
            "products" : kids_products
     }
    return render(request,'kids-product.html',context)
   





def mens(request):
    
    men_products  = Product.objects.filter(catogory=1)
    print(men_products)
    context = {
            "products" : men_products
     }
    return render(request,'men-product.html',context)
   


def womens(request):
     
    women_products  = Product.objects.filter(catogory=2)
    print(women_products)
    context = {
            "products" : women_products
     }
    return render(request,'women-product.html',context)
    

# def contact(request):
#     return render (request,'contact.html')

def product(request,id):
    kids_products  = Product.objects.filter(catogory=3)
    men_products  = Product.objects.filter(catogory=1)
    women_products  = Product.objects.filter(catogory=2)
    print(kids_products)
    print(women_products)
    print(men_products)
    if id==1:
        context = {
            "products" : men_products,
            "person" : request.session['person-id']
           
            
     }
    elif id==2:
        context = {
            "products" : women_products,
            "person" : request.session['person-id']
            
     } 
    elif id==3:
          context = {
            "products" : kids_products,
            "person" : request.session['person-id']
     }


    return render (request,'product.html',context)

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        # print (email,password)
        try:
            persons= People.objects.get(email=email,password=password)
            messages.success(request, "Logged in successfull")
            request.session['person']=persons.username
            request.session['person-id']= persons.id
            print(request.session['person-id'])
            return redirect('categories')
        except Exception as e:
               print(e)
               messages.error(request, "Password or email incorrect")
               return redirect ('signup')
    return render (request,'login.html')



def signup(request):
    if request.method=="POST":
        first_name=request.POST["fist_name"]
        lastName = request.POST["lastName"]
        username=request.POST["username"]
        password=request.POST["password"]
        email=request.POST["email"]

        try:
            newPerson=People(first_name=first_name,lastName=lastName,username=username,password=password,email=email)
            newPerson.save()
        except:
            return redirect('signup')
    
    return render (request,'signup.html')

def cart(request, slug):
    add_cart=Cart.objects.all()
    if Product.objects.all(slug=slug).exists():
        if Cart.objects.filter(slug=slug,checkout=False).exists():
            quantity = Cart.objects.get(slug=slug,checkout=False).quantity
            price = Product.objects.get(slug=slug).price
            
            quantity = quantity + 1
            
            total = price* quantity

            data = Cart.objects.create(
                
                slug = slug,
                total = total,
                quantity = 1,
                items = Product.objects.get(slug=slug)

             )
            data.save()

    else:
        return redirect('/')

    return redirect('/cart',{'add_cart':add_cart})

# def addproduct(request):
#     return render (request,'addproduct.html')
