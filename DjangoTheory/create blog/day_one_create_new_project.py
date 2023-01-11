# 1. Создаем папку проекта
# django-admin startproject Blog
# 2. Создаем виртуальное окружение
# 3. Инсталируем django проект
# pip install django
# Обязательно после этого проверить что виртуальное окружение подключилось и django установилось, это можно проверить
# в settings. Если оно не подключилось его нужно подключать вручную через терминал с помощью команды
# .\venv\Scripts\activate.
# 4.Создаем приложение для API
# python manage.py startapp api
# 5. Делаем миграции
# python manage.py migrate
# 6. Создаем суперюзера
# python manage.py createsuperuser
# 7.Скачиваем rest framework
# pip install djangorestframework
# 8.Подключаем в settings REST и приложение api
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'rest_framework',
#     'api.apps.ApiConfig'
# ]
# 9. Подключаем git
# 10. Создаем readme.md - описываем в нем что нужно скачать или изменить разработчику что бы запустить
# проект
# 11. Заливаем на git

# Rest (Representational State Transfer - передача состояния представления) - облегчает для систем
# обмен данными друг с другом.

# 1. Разделение клиента и сервера
# Реализация клиента и реализация сервера могут быть выполнены независимо друг от друга.
# Это означает, что код на стороне клиента может быть изменён в любое время
# без ущерба для работы сервера, а код на стороне сервера может быть изменён без влияния на работу
# клиента.
# Это повышает гибкость интерфейса между платформами и расширяемость за счёт упрощения компонентов
# сервера
# Используя интерфейс REST, различные клиенты попадают в одни и те же конечные точки REST, выполняют
# те же действия и получают одинаковые ответы

# 2. Отсутствие сохранения состояния
# Системы, которые следуют парадигме REST, не имеют сохранения состояния, серверу не нужно знать
# о состоянии клиента и наоборот. Таким образом, и сервер, и клиент могут понять любое полученное
# сообщение, даже не увидев предыдущих сообщений. Это отсутствие сохранения состояния обеспечивается
# за счёт использования ресурсов, а не команд. Они описывают любые объекты, документы или вещи,
# которые могут потребоваться для хранения или отправки в другие службы.

# Serializator (Сериализатор) - аналог класса Form и Models
# 1. В приложении для API необходимо создать файл serializator.py
# 2. В него необходимо сделать импорты

# from rest_framework import serializers - импортируем serializers

# from django.contrib.auth.models import User - импортируем встроенный class User(модель)

# Описываем serializer который будет возвращать информацию в json, для дальнейшего использования

# Название класса состоит всегда из двух частей - название модели и serializer
# Класс Мета является обязательным при описании serializer
# в model - передаем название модели которую используем
# fields - передаем поля которые будут обрабатываться
# fields может быть задан в виде списка либо кортежа (даже если поле одно) или строки __all__.
# с помощью строки __all__ мы передадим в обработку все поля
# fields = '__all__'
# exclude - в нее передаем поля которые следует исключить из обработки
# Переменую fields и exclude нельзя использовать в одном классе
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'first_name', 'last_name']

# Описываем views
# Делаем импорты
# from rest_framework import generics - импорт generics - набор классов которые используются для
# endpoint с различным доступом и методов обработки HTTP запросов
# К примеру
# generics.ListAPIView - используется для endpoint с доступом только для чтения, метод обработки GET
# generics.CreateAPIView - используется для endpoint с доступом только для чтения-записи, метод
# обработки GET и POST
# generics.RetrieveAPIView - используется для endpoint с доступом только для чтения одной записи, метод GET
# generics.RetrieveUpdateAPIView - используется для endpoint с доступом для обновления записи, метод PUT

# from . import serializers - импорт созданного файла serializer во views

# from django.contrib.auth.models import User - импорт передаем serializer который обрабатывает нужную модельвстроенного класса(модель)

# Описываем views которая отображает список users и наследуется от generics.ListAPIView
# Переменная queryset (переменная по стандарту) забирает набор данных из модели User
# Переменная serializer_class (переменная по стандарту) -
#
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserSerializer

# Описываем views которая отображает одного пользователя по запросу через id который передается в url
# и наследуется от generics.RetrieveAPIView

# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserSerializer

# Описываем url для api
# Делаем импорты

# from django.urls import path импортируем path для url - функция path создает элемент, который Django использует
# для показа страницы приложения.

# from rest_framework.urlpatterns import format_suffix_patterns мпортируем из rest_framework.urlpatterns суфиксы
# По стандарту DRY мы должны использовать патерны суфиксов для url

# from . import views

# Описываем url
# метод для views - as_view() для правильных обработок запросов и ответов

# urlpatterns = [
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view())
# ]

# Приводим url к формату DRY(Don't repeat youself)
# urlpatterns = format_suffix_patterns(urlpatterns)

# format_suffix_patterns - может принимать три аргумента
# format_suffix_patterns(urlpatterns, suffix_required=False, allowed=None)
# Аргументы
# urlpatterns : Требуется. Список шаблонов URL.
#
# suffix_required : Необязательный. Булево значение, указывающее, должны ли суффиксы в URL быть необязательными
# или обязательными. По умолчанию имеет значение False , что означает, что суффиксы по умолчанию необязательны.
#
# allowed : Необязательно. Список или кортеж допустимых суффиксов формата. Если он не указан, будет использован
# шаблон суффикса формата.

# format_suffix_patterns не поддерживает спуск по шаблонам URL include.


# Опсываем url для проекта
#
# from django.contrib import admin
# from django.urls import path, include - добавляем метод include
#
# метод include - позволяет обращаться к url приложений
# в качестве аргумента передаем путь к файлам url приложений
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('api.urls'))
# ]

