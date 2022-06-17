# Встроенные теги
# <!--{% extends 'base.html' %}-->
# <!--{% block title %} Index page {% endblock title %}-->
# <!--{% block header %} Главная страница {% endblock header %} &lt;!&ndash; эти строки кода выполняются и прописываются в-->
# <!--первую очередь в коде HTML&ndash;&gt;-->

# <p>{% now 'Y' %}</p> - выводит текущий год в формате 4х цифр
# <p>{% now 'F j Y' %}</p> - выводит текущую дату в формате June 17 2022
# <p>{% now 'F j, Y, P' %}</p> - выводит текущую дату в формате June 17, 2022, 2:22 p.m.
# now - реальное время
# Y - год
# F - месяц
# j - текущее число месяца
# P - время
# Работает по часовому поясу который указан в setting django, который менять нельзя

# Блок условных выражений в HTML
# Обязательно работаем с views так как нам нужно передать данные в HTML

# Создаем view с данными
#
# def index(request):
#     data = {
#         'n': -5
#     }
#     return render(request, 'index.html', context=data)

# Создаем блок условных выражений который в зависимости от полученных данных выведет информацию на экран

# Тег if

# {% if n > 0 %}
#         <p>Число положительное</p>
# {% elif n < -10 %}
#     <p>Число меньше -10</p>
# {% else %}
#     <p>Число в диапазоне от 0 до -10</p>
# {% endif %} закрытие блока

# Блоки - if, for, with обязательно нужно закрывать
# if - endif
# for - endfor
# with - endwith

# Тег for

# Создаем view с данными

# def index(request):
#     country = ['Ukraine', 'Franch', 'England', 'USA', 'Germany', 'China']
#     return render(request, 'index.html', context={'test': country})

# Для того чтобы в context передать итерируемый обьект(не словарь) создаем словарь и передаем  в него в качестве значения переменную

# Создаем блок for который в зависимости от полученных данных выведет информацию на экран

# <!--    <ul>-->
# <!--        {% for i in test %}-->
# <!--        <li>{{ i }}</li>-->
# <!--        {% empty %}-->
# <!--        <li>Нет значения</li>-->
# <!--        {% endfor %}-->
# <!--    </ul>-->

# В for в качесте переменной передаем ключ словаря который создаем в context, но с помощью метода Get цикл проходит по значению
# этого ключа
# Для того что бы не было ошибки необходимо в цикле использовать тег empty на случай если переменная будет пустая

# тег with - используется для создания переменных в HTML

# { % with name='Nina' age=29 %}
# < div >
# < p > Name: {{name}} < / p >
# < p > Age: {{age}} < / p >
# < / div >
# { % endwith %}


