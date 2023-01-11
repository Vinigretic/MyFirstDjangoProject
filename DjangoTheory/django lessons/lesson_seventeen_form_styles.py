# Стилизация форм

# Первый способ
# 1.Описываем форму
#
# class UserForm(forms.Form):
#     name = forms.CharField(min_length=3, max_length=20)
#     age = forms.IntegerField(min_value=18, max_value=100)

# 2. Создаем views

# def index(request):
#     if request.method == 'POST':
#         userform = UserForm(request.POST)
#         if userform.is_valid():
#             name = userform.cleaned_data['name']
#             age = userform.cleaned_data['age']
#             email = userform.cleaned_data['email']
#             return HttpResponse(f'{name}, {age}, {email}')
#         else:
#             return HttpResponse('Invalid data')
#     else:
#         userform = UserForm()
#         return render(request, 'index.html', {'form': userform})

# 3.Создаем html - файл
#
# <!--<!DOCTYPE html>-->
# <!--<html lang= "en">-->
# <!--<head>-->
# <!--    <meta charset="UTF-8">-->
# <!--    <title>Django forms</title>-->
# <!--    <style>-->
# <!--        .alert{color:red;}-->
# <!--        .form-group{margin:10px 0;}-->
# <!--        .form-group input{width: 250px; height: 25px; border-radius: 3px;}-->
# <!--    </style>-->
# <!--</head>-->
# <!--<body class="container">-->
# <!--    <form method="POST" novalidate>-->
# <!--        {% csrf_token %}-->
# <!--        <div>-->
# <!--            {% for field in form %}--> передаем форму сразу в цикл
# <!--            <div class="form-group">-->
# <!--                {{ field.label_tag }}--> меняем расположения названия формы
# <!--                <div>{{ field }}</div>--> выводим поле
# <!--                {% if field.errors %}--> описываем условие если данные не валидные
# <!--                {% for error in field.errors %}-->
# <!--                <div class="alert alert-danger">-->
# <!--                    {{ error }}-->
# <!--                </div>-->
# <!--                {% endfor %}-->
# <!--                {% endif %}-->
# <!--            </div>-->
# <!--            {% endfor %}-->
# <!--        </div>-->
# <!--        <input type="submit" value="send">-->
# <!--    </form>-->
# <!--</body>-->
# <!--</html>-->

# 4. Описываем url

# Второй способ

# 1.Описываем форму

# class UserForm(forms.Form):
#     name = forms.CharField(min_length=3, max_length=20)
#     age = forms.IntegerField(min_value=18, max_value=100)
#     request_css_class = 'field'
#     error_css_class = 'error'

# переменная request_css_class - отвечает за обработку request с помощью css, значение которое даем этой переменной
# будет названием класса который мы передаем в css и присваеваем стили

# переменная error_css_class = отвечает за обработку error, значение которое даем этой переменной
# будет названием класса который мы передаем в css и присваеваем стили

# 2. Создаем views

# def index(request):
#     if request.method == 'POST':
#         userform = UserForm(request.POST)
#         if userform.is_valid():
#             name = userform.cleaned_data['name']
#             age = userform.cleaned_data['age']
#             email = userform.cleaned_data['email']
#             return HttpResponse(f'{name}, {age}, {email}')
#         else:
#             return HttpResponse('Invalid data')
#     else:
#         userform = UserForm()
#         return render(request, 'index.html', {'form': userform})

# 3 Создаем html - файл

# <!DOCTYPE html>
# <html lang= "en">
# <head>
#     <meta charset="UTF-8">
#     <title>Django forms</title>
#     <style>
#         .field{font-weiget: bold;} класс(наша переменная см выше)
#         .error{color:red;}
#     </style>
# </head>
# <body class="container">
#     <form method="POST" novalidate>
#         {% csrf_token %}
#         <table>
#             {{ form }}
#         </table>
#         <input type="submit" value="send">
#     </form>
# </body>
# </html>
