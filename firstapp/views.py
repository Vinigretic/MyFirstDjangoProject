from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h2>Главная страница</h2>')

def about(request):
    return HttpResponse('<h2>О сайте</h2>')

def users(request):
    return HttpResponse('<h2>Пользователи</h2>')

def contacts(request):
    return HttpResponse('<h2>Контакты</h2>')

def login(request):
    return HttpResponse('<h2>Логин</h2>')

def registred(request):
    return HttpResponse('<h2>Регистрация</h2>')