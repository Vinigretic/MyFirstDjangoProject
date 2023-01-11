# Фильтр для фильмов и года
# Передача данных в шаблон через views
# Опишем view для вывода жанров и годов фильмов
#
# class GenreYear:
#     # жанр и год выхода фильма
#     def get_genres(self):  # выводит все жанры
#         return Genres.objects.all()
#
#     def get_years(self):   # выводит все фильмы не черновики
#         return Films.objects.filter(draft=False).values('year')  #заберем только те фильмы которые не являются черновиком и
                                                                   #заберем только ту колонку которая нам нужна с помощью
                                                                   # параметра values
# параметр values выводит данные в словаре, для того что бы вывести данные кортеджем используем параметр values_list

# Передадим этот класс в классы FilmsViews и FilmsDetailView, для того что бы они наследовали его методы
# class FilmsViews(GenreYear, ListView):
# class FilmsDetailView(GenreYear, DetailView):

# Отредактируем файл sidebar.html
# Обратившись к методу view - get_genres. Выведем все жанры
# {% for genre in view.get_genres %}

#     <ul class="w3layouts-box-list">-->
# <!--        {% for genre in view.get_genres %}-->
# <!--            <li class="editContent">-->
# <!--                <input type="checkbox" class="checked">-->
# <!--                <span class="span editContent">{{ genre.name }}</span>-->
# <!--            </li>-->
# <!--        {% endfor %}-->
# <!--</ul>

# Обратившись к методу view - get_years. Выведем все года

# {% for year in view.get_years %}
#     <li class="editContent">
#         <input type="checkbox" class="checked">
#         <span class="span editContent">{{ year.year }}</span> выводим год по ключу словаря который возвращает метод values
#     </li>
# {% endfor %}

# Создадим класс который будет фильтровать фильмы

# class FilterFilmsView(GenreYear, ListView):
#     #Фильтр фильмов
#     def get_queryset(self):
#         queryset = Films.objects.filter(year__in=self.request.GET.getlist('year'))
#         return queryset
#     template_name = 'movies/movies.html'
#     context_object_name = 'movie_list'

# вызываем встроенный метод get_queryset
# во встроенную переменную queryset передаем список в который будут входить года которые будут возвращаться из frontenda
# year__in
# с помощью метода  getlist извлекаем значения годов из GET запроса
# self.request.GET.getlist('year'))
# и возвращаем queryset
# return queryset

# Так как джанго автоматически генерирует имена шаблонов и переменные которые мы передаем в html и мое имя модели Film не
# совпадает с названиями моих html-шаблонов, мне во view необходимо явно указать какой шаблон обрабатывать и какую переменную
# передавать. Для этого добавим во view код ниже

#     template_name = 'movies/movies.html'
#     context_object_name = 'movie_list'

# Отредактируем файл sidebar.html
# Обернем div который выводит года  в форму
#
# <form action="{% url 'filter' %}" method="get">
#     <div class="left-side">
#         <h3 class="sear-head editContent">Год</h3>
#         <ul class="w3layouts-box-list">
#             {% for year in view.get_years %}
#                 <li class="editContent">
#                     <input type="checkbox" class="checked" name="year" value="{{ year.year }}">
#                     <span class="span editContent">{{ year.year }}</span>
#                 </li>
#             {% endfor %}
#         </ul>
#     </div>
#     <button type="submit">Найти</button>
# </form>

# в action передадим url, метод отправки get
# <form action="{% url 'filter' %}" method="get">
#
# в input добавляем name="year"  и value="{{ year.year }}
# <input type="checkbox" class="checked" name="year" value="{{ year.year }}">
#
# добавляем кнопку отправить
# <button type="submit">Найти</button>

# создадим url которую передаем в action
# path('filter/', views.FilterFilmsView.as_view(), name='filter')
# добавляем ее над остальными url из за slug

