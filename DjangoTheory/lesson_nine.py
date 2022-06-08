# Передача данных в HTML файлы
# 1. Описываем views
# 2. Описываем в ней необходимые данные
#
# def index(request):
#     header = 'Personal Data'
#     langs = ['Ukrainian, English', 'German','French']
#     user = {
#         'name': 'Dima',
#         'age': 25,
#     }
#     address = ('Абрикосовая', 23, 2)
#
#     data = {
#         'header': header,
#         'langs': langs,
#         'user': user,
#         'address': address
#     }
#     return render(request, 'index.html', context=data)

# 3. Создаем переменную data в которую передаем все описанные переменные. Переменная должна быть обязательно словарем, так как
# параметр render - context работает только со словарем
# 4. Передаем данные в HTML файл
#
# <body>
#     <h2>{{ header }}</h2>
#     <p>Langs: {{ langs.0 }}, {{ langs.1 }}, {{ langs.2 }}, {{ langs.3 }} </p>
#     <p>Name: {{ user.name }}, age: {{ user.age }} </p>
#     <p>Address: street {{ address.0 }}, house {{ address.1 }}, flat {{ address.2 }}</p>
# </body>

# Строковые, числовые, булевые переменные передаем просто названием переменной - {{ header }}  в фигурных скобках
# Списковые параметры передаем по индексам - {{ langs.0 }}, {{ langs.1 }}
# Словари передаем по ключу(имя словаря.ключ) - {{ user.name }}

# 5 Описываем url
#
# urlpatterns = [
#     path('', views_firstapp.index),
# ]

# Описати сторінку user:
# 1) Має бути viev яка використовує типи данних (dict, int, str, typle)
# 2) Опис url
# 3) Опис html
# ВСІ ДАННІ ПОВИННІ БУТИ АДЕКВАТНІ, РОЗРАХОВАНІ НА РЕАЛЬНОГО КОРИСТУВАЧА