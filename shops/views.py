from django.shortcuts import render
from django.template.response import TemplateResponse

def user(request):
    return render(request, 'shops/user.html')

def contacts(request):
    return render(request, 'shops/contacts.html')

def products(request):
    return TemplateResponse(request, 'shops/products.html')
