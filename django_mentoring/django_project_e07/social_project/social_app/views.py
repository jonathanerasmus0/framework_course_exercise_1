from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def home(request):
#     return HttpResponse("Hello from our social app")
def home(request):
    return render(request,"social_app/home.html")

def about(request):
    return render(request,"social_app/about.html")

def first_page(request):
    return render(request,"social_app/page1.html")

def profile(request):
    profile_data = {
        'name':'John',
        'age':20,
        'adress':'some place'
    }
    car = {'brand':'BMW','year':2007}
    return render(request,'social_app/profil.html',{'data':profile_data,'car':car})

def shop(request):
    items =[
        {'item':'Laptop',
         'price':1000},
        {'item':'Smartphone',
         'price':600},
        {'item':'Tablet',
         'price':500}
    ]
    return render(request,'social_app/store.html',{'items':items})
