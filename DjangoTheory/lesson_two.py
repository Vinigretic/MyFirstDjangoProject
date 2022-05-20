# Views.py
# from django.shortcuts import render - импорт функции рендер, обрабатывает ответ views

# from django.http import HttpResponse - импорт функции HttpResponse, обрабатывает текстовые views,
# удобно для обработки HTML

# Описываем в этом файле страницы которые будут отображаться
# request - запрос пользователя, отправляется на сервер(все функции во view принимают его в качестве аргумента)
# response - ответ сервера, который возвращается пользователю

# def index(request):  # создаем функцию которая всегда принимает request
#     return HttpResponse('<h2>Главная страница</h2>') # возвращаем ответ пользователю

# Urls.py
# from django.contrib import admin - импорт admin дает возможность сделать url с сылкой на админ страницу
# path('admin/', admin.site.urls) - подключаем админ панель
# from django.urls import path - импорт path функция с помощью которой создаем url на view
# from firstapp import views # импорт из приложения

# urlpatterns = [
#     path('', views.index, name='home'), # url на главную страницу
#     path('admin/', admin.site.urls), # url k admin панели
#     path('about/', views.about), # url к about странице
# ]  # список в котором описываем наши url
