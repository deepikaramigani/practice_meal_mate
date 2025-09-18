from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from .models import Restaurant

# Create your views here.
def index(request):
    return render(request,'index.html')

def open_signin(request):
    return render(request,'signin.html')

def open_signup(request):
    return render(request,'signup.html')

def signin(request):
    return HttpResponse("Login Success")

def signup(request):
    #return HttpResponse("Recieved")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        try:
            customer =Customer.objects.get(username=username,password=password)
            return HttpResponse("Duplicate username not allowed")
        except Customer.DoesNotExist:
                Customer.objects.create(username =username,
                            password=password,
                            email=email,
                            mobile=mobile,
                            address=address)
                return render(request,"signin.html")

def signin(request):
    #return HttpResponse("Recieved")
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            customer =Customer.objects.get(username=username,password=password)
            if username=="admin":
                return render(request,"admin_home.html")
            return render(request,"customer_home.html",{"username":username})
        except Customer.DoesNotExist:
            return render(request,"fail.html")
    else:
        return HttpResponse("Invalid request")

def open_add_restaurant(request):
    return render(request,"add_restaurant.html")

def add_restaurant(request):
    if (request.method == "POST"):
        name = request.POST.get('name')
        picture = request.POST.get('picture')
        cuisine = request.POST.get('cuisine')
        rating = request.POST.get('rating')

        try:
            reataurant = Restaurant.objects.get(name=name,cuisine=cuisine)
            return HttpResponse("Restaurant already exists")
        except Restaurant.DoesNotExist:
            Restaurant.objects.create(name=name,
                                      picture=picture,
                                      cuisine=cuisine,
                                      rating=rating)
            restaurants = Restaurant.objects.all()
            return render(request,"show_restaurants.html",{"restaurants":restaurants})
    return HttpResponse("Invalid Request")