# from django.shortcuts import render
# from .forms import AboutForm
# from django.http import HttpResponse, HttpResponseRedirect
# import random
# from .forms import ModelsForm
# from .forms import AccountForm
# from .forms import ColorForm
#
# users = {
#     'cat': '12345',
#     'dog': '67890',
#     'bird': '258'
# }
#
#
# modelprice = {
#     'BMV': 10000,
#     'Mersedes': 15000,
#     'Toyota': 12000,
#     'Kia': 9000,
#     'Suzuki': 14000
# }
#
# color = ['red', 'yellow', 'black', 'blue', 'green', 'gray', 'white']
#
# def about(request):
#     if request.method == 'POST':
#         model = request.POST.get('model')
#         color = request.POST.get('color')
#         year = request.POST.get('year')
#
#         if model.lower() in (i.lower() for i in modelprice):
#             return HttpResponse(f'model: {model.capitalize()}, color: {color}, year: {year}, price: {modelprice[model.capitalize()]}')
#         else:
#             return HttpResponse(f'Извините данной модели нет в наличии')
#     else:
#         aboutform = AboutForm()
#         return render(request, 'cars/about.html', {'form': aboutform})
#
#
# def models(request):
#     if request.method == 'POST':
#         model = request.POST.get('model')
#         year = request.POST.get('year')
#         color_car = random.choice(color)
#         colorform = ColorForm()
#         data = {'model': model, 'year': year, 'color_car': color_car, 'colorform': colorform}
#         return render(request, 'cars/color.html', context=data)
#     else:
#         modelsform = ModelsForm()
#         return render(request, 'cars/models.html', {'model': modelsform})
#
#
# def account(request):
#     if request.method == 'POST':
#         login = request.POST.get('login')
#         password = request.POST.get('password')
#         if login in users and users[login] == password:
#             return HttpResponseRedirect('/about')
#         else:
#             return HttpResponse(f'Логин или пароль не верный, повторите попытку')
#     else:
#         accountform = AccountForm()
#         return render(request, 'cars/account.html', {'account': accountform})
#
#
#
#
