# Создание вывода полного описания фильма

# 1. Описываем view

# Создадим класс который будет обращаться к необходимому обьекту с помощью метода get, в который из url будет
# передаваться аргумент(число) - pk, этот аргумент будет сравниваться с id фильмов и при совпадение выводить нужный фильм
#
# film = Films.objects.get(id=pk)

# Далее с помощье render обрабатываем html страницу и в cловарь передаем переменную film, которую затем передадим
# в html страницу

# class FilmsDetailView(View):
#     """Полное описание фильма"""
#     def get(self, request, pk):
#         film = Films.objects.get(id=pk)
#         return render(request, 'movies/movie_ditail.html', {'movie': film})


# 2. Опишем url

# path('<int:pk>/', views.FilmsDetailView.as_view()) - описываем url которая будет принимать некий аргумент который будет
# передаваться в метод get во view


# urlpatterns = [
#     path('', views.FilmsViews.as_view()),
#     path('<int:pk>/', views.FilmsDetailView.as_view())
# ]

# 3. Создадим html страницу movie_detail

# Добавим необходимые аргументы
#
# Постер
# <div class="desc1-left col-md-6">-->
#       <img src="{{ movie.poster.url }}" class="img-fluid" alt="">-->
# </div>
#
# Название
# <h3 class="editContent" style="outline: none; cursor: inherit;">-->
#       {{ movie.title }}-->
# </h3>-->
#
# Год, страну, слоган
# <ul>-->
# <li style="list-style: none">-->
#    <span><b>Год:</b> {{ movie.year }}</span></li>-->
# <li style="list-style: none">-->
#    <span><b>Страна:</b> {{ movie.country }}</span>-->
# </li>-->
# <li style="list-style: none">-->
#     <span><b>Слоган:</b> {{ movie.slogan }}</span>-->
# </li>-->

# Режисер, актер, жанр. Так как эти поля в модели Films имеют связи многие ко многим с моделями ActorsDirectors и Genres
# Необходимо пройти циклом по всем елементам полей Режисер, актер, жанр

# <li style="list-style: none">-->
#  <span><b>Режиссер:</b>-->
#        {% for director in movie.director.all %}-->
#            {{ director.name }}-->
#       {% endfor %}-->
#    </span>-->
# </li>-->
# <li style="list-style: none"><span><b>Актеры:</b>-->
#    {% for actor in movie.actor.all %}-->
#        {{ actor.name }}-->
#     {% endfor %}-->
# </span>-->
# </li>-->
# <li style="list-style: none"><span><b>Жанр:</b>-->
#    {% for genre in movie.genre.all %}-->
#         {{ genre.name }}-->
#    {% endfor %}-->
#    </span>-->

# Премьера в мире, Бюджет, Сборы в США
# <li style="list-style: none"><span><b>Премьера в мире:</b> {{ movie.premiere_in_world }}</span>-->
# </li>-->
# <li style="list-style: none">-->
#     <span><b>Бюджет:</b> ${{ movie.budget }}</span></li>-->
# <li style="list-style: none">-->
#     <span><b>Сборы в США:</b> ${{ movie.fees_in_usa }}</span></li>-->
# <li style="list-style: none"><span><b>Сборы в мире:</b> ${{ movie.fess_in_world }}</span>-->
# </li>-->

# Создание перехода с главной страницы на определенный фильм нажатием на его название
# 1. Способ
# Изменим view
#
# Вместо аргумента рк передадим аргумент slug, url в модели Films
#
# url = models.SlugField(max_length=160, unique=True)
#
# class FilmsDetailView(View):
#     """Полное описание фильма"""
#     def get(self, request, slug):
#         film = Films.objects.get(url=slug)
#         return render(request, 'movies/movie_detail.html', {'movie': film})
#
# Изменим url
#
# urlpatterns = [
#     path('', views.FilmsViews.as_view()),
#     path('<slug:slug>/', views.FilmsDetailView.as_view())
# ]

# Изменим html главной страницы(movies.html)

# добавим ссылку перехода в название фильма
# <a href="/{{ movie.url }}/" class="editContent" >{{ movie.title }}</a>

# <div class="item-info-product">
#     <h4 class="">
#         <a href="/{{ movie.url }}/" class="editContent" >{{ movie.title }}</a>
#     </h4>

# 2. Способ
# Воспользуемся тегом url, в который передадим имя нужной url и если нужно значение

# Для этого изменим url, добавив name
# urlpatterns = [
#     path('', views.FilmsViews.as_view()),
#     path('<slug:slug>/', views.FilmsDetailView.as_view(), name='movie_detail')
#
# ]

# Добавим name в html, значением передадим slug нашего фильма
# <a href="{% url 'movie_detail' movie.url %}" class="editContent" >{{ movie.title }}</a>

# 3. Способ - самый правильный

# Изменим нашу модель Films дописав метод get_absolute_url. Этот метод будет возвращать работу метода reverse.
# Метод reverse позволяет по имени view получить её url.

# Атрибуты которые может принимать reverse:
# reverse(viewname, urlconf=None, args=None, kwargs=None, current_app=None)
# kwargs и args не могут быть переданы одновременно

# В метод get_absolute_url мы должны передать name нашего url - "movie_detail", и словарь в который мы передаем параметры
# которые передаем в url. Ключем этого словаря будет выступать slug, а значением поле url


# def get_absolute_url(self):
#     return reverse("movie_detail", kwargs={"slug": self.url})

# Затем в movies.html  в теге а вызовем метод нашей модели

# <a href="{{ movie.get_absolute_url }}" class="editContent" >{{ movie.title }}</a>

# Написание view с помощью классов ListView DetailView

# from django.views.generic import ListView, DetailView

# Затем, определим свой собственный класс представления на базе этого класса ListView
# class FilmsViews(ListView):

# Внутри определим один атрибут model, который будет ссылаться на модель данных Films, связанной с этим списком.
# (Так как нам на главной странице нужно вывести список фильмов из этой модели).
# Фактически, строчка model = Films выберет все записи из таблицы Films и попытается отобразить их в виде списка,
# используя шаблон с именем: <имя приложения>/<имя модели>_list.html

# Чтобы указать в классе представлений нужный шаблон , используется атрибут template_name, которому присваиваем путь к
# нужному шаблону: template_name = 'movies/movies.html'
# переменная queryset присвоит все атрибуты и методы модели Films

# Так же у нас не должны выводится фильмы помеченные как черновик.
# Используем метод filter, который выведет все обьекты для которых поле draft=False
# queryset = Films.objects.filter(draft=False)

# Так же необходимо обратить внимание какую переменную мы передаем в цикле  в movies.html

# Ранее переменная movie_list содержал список всех записей. По умолчанию, данные из модели Films, указанной в классе
# представлений class FilmsViews(ListView), помещаются в коллекцию object_list и если мы ее запишем вместо movie_list,
# то должно все заработать.
#
# Если в шаблоне вместо object_list мы хотим использовать другое обозначение (имя), то в классе class FilmsViews(ListView)
# следует прописать атрибут context_object_name с указанием другого имени переменной:
#
# context_object_name = 'movie_list'
#
#
# class FilmsViews(ListView):
#     """Список фильмов"""
#     model = Films
#     queryset = Films.objects.filter(draft=False)
#     template_name = 'movies/movies.html'
#     context_object_name = 'movie_list'

# Изменим класс class FilmsDetailView
# Создадим класс который наследует от класса DetailView
# class FilmsDetailView(DetailView):

# поле slug_field = 'url'  - отвечает за то по какому полю нужно будет искать нашу запись эти данные будут переданы
# из url и сравнивая с нашим полем django будет искать нужную нам запись


# class FilmsDetailView(DetailView):
#     model = Films
#     slug_field = 'url'
#     queryset = Films.objects.all()
#     template_name = 'movies/movie_detail.html'
#     context_object_name = 'movie'

# Переменную template_name можно не использовать так как django автоматически создает связи, но для этого
# шаблон html должен называться следующим образом:
# первая часть имени должна называться как модель, вторая либо list либо detail

# в моем случае вместо movies.html должен быть films_list
# вместо movie_detail.html' - films_detail