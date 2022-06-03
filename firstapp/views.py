from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.template.response import TemplateResponse


# def index(request):
#     return HttpResponse('<h2>Главная страница</h2>')
#
# def about(request):
#     return HttpResponse('<h2>О сайте</h2>')
#
# def users(request):
#     return HttpResponse('<h2>Пользователи</h2>')
#
# def contacts(request):
#     return HttpResponse('<h2>Контакты</h2>')
#
# def login(request):
#     return HttpResponse('<h2>Логин</h2>')
#
# def registred(request):
#     return HttpResponse('<h2>Регистрация</h2>')

# def products(request, product_id = 0):
#     # output = '<h2>product № {0}</h2>'.format(product_id)
#     output = f'<h2>product № {product_id}</h2>'
#     return HttpResponse(output)
#
# def users(request, id = 0, name = 'admin'):
#     # output = '<h2>User</h2> <h3>id:{0} name:{1}</h3>'.format(id, name)
#     output = f'<h2>User</h2> <h3>id:{id} name:{name}</h3>'
#     return HttpResponse(output)
#
# def contacts(request, id = 0, name = 'admin', phone_number = '098-96-40-698'):
#     output = f'<h1>Contacts page</h1> <h2>id:{id}</h2> <p>name:{name}, phone_number:{phone_number} </p>'
#     return HttpResponse(output)

# def products(request, product_id):
#     category = request.GET.get('cat', '')
#     output = f'<h2>Product number</h2> <p>id:{product_id}, category:{category}</p>'
#     return HttpResponse(output)
#
# def users(request):
#     id = request.GET.get('id', 1)
#     name = request.GET.get('name', 'Alina')
#     output = f'<h2>User info</h2> <p>id:{id}, name:{name}</p>'
#     return HttpResponse(output)

# Описати сторінку покупки продукту з параметрами ціна та строковими параметрами нейм юсера, ід
# юзера, нейм товару, айді товару, прайс доставки.

# def orders(request, price):
#     order_id = request.GET.get('o_id', '')
#     user_name = request.GET.get('u_name', '')
#     user_id = request.GET.get('u_id', '')
#     product_name = request.GET.get('p_name', '')
#     product_id = request.GET.get('p_id', '')
#     price_delivery = request.GET.get('prise_del', '')
#     output = f'<h1>Order number: {order_id}</h1> <p>user name:{user_name}, user_id{user_id}, ' \
#              f'product name: {product_name}, product id:{product_id}, price delivery: {price_delivery}</p>'
#     return HttpResponse(output)

# def index(request):
#     return HttpResponse('index')
#
# def about(request):
#     return HttpResponse('about')
#
# def contact(request):
#     return HttpResponseRedirect('/about')
#
# def details(request):
#     return HttpResponsePermanentRedirect('/')

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'firstapp/home.html')

def about(request):
    return TemplateResponse(request, 'firstapp/about.html')

