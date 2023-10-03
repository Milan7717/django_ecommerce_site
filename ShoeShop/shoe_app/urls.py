from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
   path('',views.home,name='home'),
   path('categories',views.categories,name='categories'),
   
   # path('kids',views.kids),
   # path('mens',views.mens),
   # path('womens',views.womens),
   # path('contact',views.contact),
   path('product/<int:id>/',views.product,name='product'),
   path('login',views.login,name='login'),
   path('signup',views.signup,name='signup'),
   path('cart/<int:product_id>/<int:person_id>',views.cart,name='cart'),
   # path('addproduct',views.addproduct),

]