# Валидация полей форм - проверка вводимых данных пользователем на правильность.
# Может осуществляться на стороне клиента и на сервере

# Проверка на стороне клиента осуществляется с помощью доп параметров которые мы описываем в формах

# class UserForm(forms.Form):
#     name = forms.CharField(label='name', required=False, min_length=4, max_length=20)
#     age = forms.IntegerField(label='age', min_value=1, max_value=100)
#     email = forms.EmailField(label='email', required=False)

# Параметры:
# 1. параметр required - отвечает за заполнение поля, по умолчанию поле должно быть заполнено, если присвоить этому параметру
# значение False - required=False, заполнение поля станет не обязательным
# 2. параметры min_length и max_length(текстовые поля) - отвечают за количесво введденых минимальных и максимальных символов
# в поле
# 3. параметры min_value и max_value(числовые поля) - используются для установки граничных значений в числовых полях

# Проверка на стороне сервера

# Так как проверку на стороне клиента можно отключить с помощью параметра(novalidate), обязательно делать проверку на сервере
# Сервер будет осуществлять проверку так же по параметрам которые мы опишем в формах, но еще необходимо описать логику во view

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

# userform = UserForm(request.POST) - создаем обьект класса и с помощью request.POST забираем данные которые пользователь
# ввел в форму(даже если они не валидные).

# if userform.is_valid(): - описываем условие, если данные валидные
#
# name = userform.cleaned_data['name'] - присваеваем информацию из формы в переменную  с помощью метода cleaned_data
# cleaned_data - всегда работает со списком

# else:
#     return HttpResponse('Invalid data') - если данные не валидные возвращаем сообщение

