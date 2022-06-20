# Формы
# Forms - класс, в котором есть встроенные функции которые мы можем использовать

# Необходимо создать файл forms.py
# сделать импорт - from django import forms
# Создать класс который наследуется от forms.Form - class UserForm(forms.Form):
# В этом классе мы можем создать необходимые нам поля(числа, строки и т.д)
# name = forms.CharField()
# age = forms.IntegerField()
# После этого обязательно нужно сделать импорт класса во views

# from .forms import UserForm

# Далее создаем views
#
# def index(request):
#     userform = UserForm() # создаем обьект класса
#     return render(request, 'index.html', {'form': userform})  # третьим параметром передаем словарь, ключ придумываем произвольно,
#                                                               # значением передаем обьект класса

# Далее ключ словаря передаем в качестве переменной в HTML

# < table >
# {{form}}
# < / table >

# Создаем в HTML форму
# <body>
#     <form method="POST">
#         {% csrf_token %}
#
#     <table>
#         {{ form }}
#     </table>
#     <input type="submit" value="Send">
#     </form>
# </body>

# Передаем в нее метод запроса POST(запрос на создание данных) с помощью которго мы получим доступ к информации которую пользователь
# введет в форму

# {% csrf_token %} добавляем токен безопасности, защищает от csrf атак(защита сервера от большого кол-ва запросов)

# <input type="submit" value="Send"> - кнопка отправки данных

# Создаем views

# def index(request):
#     if request.method == 'POST':
#         name = request.POST.get('name') # передаем данные которые ввел пользователь в переменную
#         age = request.POST.get('age')
#         return HttpResponse(f'Hello {name}, I am {age}')
#     else:
#         userform = UserForm()
#         return render(request, 'index.html', {'form': userform})



# <tr><th><label for="id_name">Name:</label></th><td><input type="text" name="name" required id="id_name" /></td></tr>
# <tr><th><label for="id_age">Age:</label></th><td><input type="number" name="age" required id="id_age" /></td></tr>