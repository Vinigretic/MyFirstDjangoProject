# тemplates - папка в которой описываем визуализацию приложения(могут быть и другие названия)
# Создаем ее в корневом каталоге проекта
# Основной html файл как правило называется index
# Папку тemplates необходимо указать в setting проекта
# 1. импортируем библиотеку os(библиотека для работы с системой)
# 2. создаем константу TEMPLATE_DIR
# TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
# в этой строке вызываем библиотеку os, затем вызываем модуль path и в join передаем два аргумента, первый BASE_DIR, второй
# название подключаемой папки templates
# 3. в стандартном списке TEMPLATES в ключ 'DIRS' передаем созданную константу
# 4. Создаем views index
#
# def index(request):
#     return render(request, 'index.html')
#
# render - стандартная функция обработки запроса при работе с html
# импортируется из модуля django.shortcuts
# 5. Прописываем url - всегда одна на весь проект
# 6. Можно описывать шаблоны для каждого приложения, для этого в temlates создаем папку с названием приложения
# 7. При создании views для отдельных приложений проекта необходимо прописать более развернутый путь
#
# def home(request):
#     return render(request, 'firstapp/home.html')

# 8. Для генерации ответа можно использовать не только render, а так же TemplateResponse(класс), импортируется из
# django.template.response
#
# def about(request):
#     return TemplateResponse(request, 'firstapp/about.html')