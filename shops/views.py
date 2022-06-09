from django.shortcuts import render
from django.template.response import TemplateResponse

# def user(request):
#     return render(request, 'shops/user.html')
#
# def contacts(request):
#     return render(request, 'shops/contacts.html')
#
# def products(request):
#     return TemplateResponse(request, 'shops/products.html')

# def user(request):
#     header = 'Personal data'
#     user = {
#         'last_name':'Petrov',
#         'first_name':'Ivan',
#         'age':35,
#         'city':'Lviv',
#         'address':'вул. Степана Бандери, буд. 6, кв. 16',
#         'status':'is married'
#     }
#     parameters = (185, 85)
#     salary = 30000
#
#     data = {
#         'header':header,
#         'user':user,
#         'parameters':parameters,
#         'salary':salary
#     }
#     return render(request, 'shops/user.html', context=data)
