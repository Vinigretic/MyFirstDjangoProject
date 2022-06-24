# Типы полей в формах
# from django import forms сделать импорт
# forms.BooleanField - создает поле check-box, возвращает значение bool, True если флаг отмечен и False если нет
# forms.NullBooleanField - создает поле у которого есть три варианта - неизвестный, да, нет
# forms.CharField - создает поле для текстового ввода
# forms.EmailField - создает поле для ввода ел. адреса, имеет валлидацию на правильность ввода адреса
# forms.GenericIPAddressField - создает поле для ввода IP - адресса в формате IP4v и IP6v, имеет валлидацию на правильность ввода адреса
# forms.URLField - предназначен для ввода ссылок
# forms.FileField - предназначен для выбора файла который необходимо загрузить из устройства
# forms.ImageField - предназначен для выбора файлов изображения, но при этом имеет валлидацию на проверку изображения
# forms.DateField - предназначен для установки даты, в поле вводится текст который конвертируется в дату
# пример текста который можно ввести: 2020-12-25 или 11/25/17
# forms.TimeField - предназначен для ввода времени
# пример текста который можно ввести: 14:30:59 или 14:30
# forms.SplitDateTimeField - создает два текстовых поля для ввода даты и времени
# forms.FloatField - создает поле для ввода не целых чисел
# forms.ChoiceField(choises=((),())) - генерирует словарь из елементов кортежей, каждый кортеж должен
# содержать два элемента, первый елемент кортежа будет ключем(value в HTML), второй - значением

# С помощью парамерта label можем давать названия для полей
# name = forms.CharField(label='What is your name stranger' )

# Виджеты django
# с помощью параметра widget - можем менять поведение форм
# PasswordInput - генерирует поле для ввода пароля <input type='password'>
# HiddenInput - генерирует скрытое поле <input type='hidden'>
# MultipleHiddenInput - генерирует набор скрытых полей <input type='hidden'>
# TextInput - генерирует однострочное текстовое поле
# TextArea - генерирует многострочное текствое поле <textarea></textarea>
# RadioSelect - генерирует список переключателей(радиокнопок) <input type='radio'>
# CheckboxSelectMultiple - генерирует список флажков(чекбоксов) <input type='checkbox'>
# TimeInput - генерирует поле для ввода времени
# SelectDateWidget - генерирует три поля select для выбора дня, месяца и года
# FileInput - генерирует поле для выбора файла

# class UserForm(forms.Form):
#     name = forms.CharField(label='What is your name stranger', initial='name', help_text=' Input name here')
# initial - устанавдивает значение по умолчанию
# help_text - устанавливает подсказку рядом с полем ввода

# Пример передачи widgeta
# comment = forms.CharField(label='Комментарий', widget=forms.Textarea, initial='Please type your comment',
#                           help_text='Input comment here')
# field_order - для того что бы поменять порядок расположения форм на странице испоьзуем это свойство
# создаем переменную обязательно с названием field_order, передаем в нее список, и в этом списке в качестве аргументов
# передаем название полей, в нужном порядке отображения

# Настройка вида формы
# Используются три спец метода:
# 1. as_table(): отображение ввиде таблицы
# 2. as_ul(): отображение ввиде списка
# 3. as_p: отображение в каждом отдельном параграфе

# Пример описания в HTML
#
# <form method="POST">
#         {% csrf_token %}
#         <table>
#         {{ form.as_table }}
#         </table>
#         <input type="submit" value="send">
# </form>

# <form method="POST">
#         {% csrf_token %}
#         <ul>
#         {{ form.as_ul }}
#         </ul>
#         <input type="submit" value="send">
# </form>

# <form method="POST">
#         {% csrf_token %}
#         <div>
#         {{ form.as_p }}
#         </div>
#         <input type="submit" value="send">
# </form>

