# Переадрисация
# Отправка статусных кодов

# Переадрисация это смена адресса(пути) к определенному документу
# Переадрисация - бывает временная и постоянная

# Временная  - указываем что документ временно перемещен на новый адресс, статус код: 302
# для создания времененной переадрисации применянется class - HttpResponseRedirect принимает первым параметром
# url

# Постоянная - указываем что документ постоянно доступен по новому адрессу
# для создания постоянной переадрисации применянется class - HttpResponsePermanentRedirect принимает первым
# параметром url

# class HttpResponseRedirect и HttpResponsePermanentRedirect импортируются из библиотеки django.http
# from django.http import HttpResponseRedirect
# from django.http import HttpResponsePermanentRedirect

# def index(request):
#     return HttpResponse('index') создание главной страницы
#
# def about(request):
#     return HttpResponse('about') создание страницы about
#
# def contact(request):
#     return HttpResponseRedirect('/about') создание временной переадрисации на страницу about
#
# def details(request):
#     return HttpResponsePermanentRedirect('/') создание постоянной переадрисации на главную страницу