# Static files подключение

# 1. Создаем папку static
# 2 Подключаем папку static в settings проекта
#
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]
# 2. В папке static создаем отдельные папки для всех стилей
# 3. Подключаем статические файлы в HTML
#
# {% load static %}

# 4. Подключаем css стили и img в HTML файл
#
# <head>
#     <meta charset="UTF-8">
#     <link rel="stylesheet" href="{% static 'css/style.css'%}"> подключение css
#     <title>Index page</title>
# </head>
# <body>
#     <h1>My beautiful cat</h1>
#     <img src="{% static 'images/1560329641_2.jpg'%}" alt='Picture is not open'> подключение img
# </body>
# 5. Создаем views
#
# def index(request):
#     return render(request, 'index.html')

# 6. Описываем url
#
# urlpatterns = [
#     path('', views_firstapp.index)
# ]
