from django.contrib import admin
from django.urls import path
from firstapp import views # импорт из приложения

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('users/', views.users),
    path('contacts/', views.contacts),
    path('login/', views.login),
    path('registred/', views.registred),
]
