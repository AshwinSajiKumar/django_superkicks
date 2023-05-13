from django.shortcuts import render
from .models import product

def display(request):
    a=product.objects.all()
    return render(request,'index.html',{"product":a})
