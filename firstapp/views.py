from django.shortcuts import render
from django.http import HttpResponse


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

def products(request, product_id = 0):
    # output = '<h2>product № {0}</h2>'.format(product_id)
    output = f'<h2>product № {product_id}</h2>'
    return HttpResponse(output)

def users(request, id = 0, name = 'admin'):
    # output = '<h2>User</h2> <h3>id:{0} name:{1}</h3>'.format(id, name)
    output = f'<h2>User</h2> <h3>id:{id} name:{name}</h3>'
    return HttpResponse(output)

def contacts(request, id = 0, name = 'admin', phone_number = '098-96-40-698'):
    output = f'<h1>Contacts page</h1> <h2>id:{id}</h2> <p>name:{name}, phone_number:{phone_number} </p>'
    return HttpResponse(output)
