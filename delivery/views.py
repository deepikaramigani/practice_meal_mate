from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer

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
            return render(request,"customer_home.html")
        except Customer.DoesNotExist:
            return render(request,"fail.html")
    else:
        return HttpResponse("Invalid request")

def add_restaurant_page(request):
    return render(request,"add_restaurant.html")