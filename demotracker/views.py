from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    return render(request, "login.html") 

def accounts(request):
    return render(request, "accounts.html") 

def addproduct(request):
    return render(request, "add-product.html") 
