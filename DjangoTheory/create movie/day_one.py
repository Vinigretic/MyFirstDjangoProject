# 1. Создаем новый проект Movie
# 2. Создаем виртуальное окружение для него
# 3. Устанавливаем django в проект
# 4. Делаем миграции для подключения SQLite
# 5. Создаем приложение проета Movies
# 6. В приложении проета создаем файл urls и forms
# 7. Подключим наше приложение в насройках проекта

#
#
# 8. Создание моделей
#
# Создадим модель Category
#
# class Category(models.Model):
#     name = models.CharField('Категории', max_length=150)
#     description = models.TextField('Описание')
#     urls = models.SlugField(max_length=160, unique=True)

# Поле для urls будет иметь тип SlugField(обычно используется для полей urls , содержит два параметра, max_length, unique
# параметр unique - Если указано True, это поле должно быть уникальным во всей таблице.
# поля name и desctiption принимают необязательный аргумент 'Категории' и 'Описание' если его не будет django сгенерирует имя
# автоматически преобразовав пробелы в подчеркивания

# ПОСЛЕ ЗАПУСКА ПОСМОТЕТЬ КАК РАБОТАЕТ БЕЗ ЭТИХ ПАРАМЕТРОВ СТРОКОВАЯ ФУНКЦИЯ И МЕТА!!!!!!!!!!!!!!!!!!!

# Создадим функцию которая возвращает строковое представление нашей модели
#     def __str__(self):
#         return self.name

# Создадим метакласс Мета(контейнер данных со своими доп опциями)
# с помощью параметра  verbose_name мы можем указать имя модели во множественном и единственном числе. Будет отображаться
# название указанное в Meta в админке
#
#
# class Meta:
#     verbose_name = 'Категория'
#     verbose_name_plural = 'Категории'

# Создадим модель Актеров и Режисеров

# image = models.ImageField("Изображение", upload_to="actors/") это поле проверит является ли обьект допустимым изображением

# параметр upload_to - (указываем каталог куда будем загружать изображения)Этот атрибут обеспечивает способ указания
# каталога загрузки и имени файла и может быть установлен  двумя способами.
# upload_to также может быть вызываемым объектом, например, функцией. Он будет вызван для получения пути загрузки, включая
# имя файла. Этот вызываемый объект должен принимать два аргумента и возвращать путь в стиле Unix (с косой чертой) для
# передачи в систему хранения


# class ActorsDirectors(models.Model):
#     name = models.CharField("Имя", max_length=100)
#     age = models.PositiveSmallIntegerField("Возраст", default=0)
#     description = models.TextField("Описание")
#     image = models.ImageField("Изображение", upload_to="actors/")
#
# Создадим функцию которая возвращает строковое представление нашей модели
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse('actor_detail', kwargs={"slug": self.name})
#
# Создадим метакласс Мета(контейнер данных со своими доп опциями)
# с помощью параметра  verbose_name мы можем указать имя модели во множественном и единственном числе
#
#     class Meta:
#         verbose_name = "Актеры и режиссеры"
#         verbose_name_plural = "Актеры и режиссеры"

# Создадим модель Жанр
#
# class Genre(models.Model):
#     name = models.CharField("Имя", max_length=100)
#     description = models.TextField("Описание")
#     url = models.SlugField(max_length=160, unique=True)
#
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = "Жанр"
#         verbose_name_plural = "Жанры"

# Создадим модель Фильмы

# director = models.ManyToManyField(ActorsDirectors, verbose_name="режиссер", related_name="film_director")
# Атрибут related_name указывает имя обратного отношения от модели ActorsDirectors к модели Films
#
# Если вы не укажете related_name, Django автоматически создает имя, используя имя вашей модели с суффиксом _set,
# например ActorsDirectors.films_set.all().

# premiere_in_world = models.DateField("Примьера в мире", default=date.today)
# default=date.today - если дата не установлена по умолчанию передастся текущая дата

# budget = models.PositiveIntegerField("Бюджет", default=0,
#                                          help_text="указывать сумму в долларах")

# параметр help_text - передаем дополнительный текс для отображения в виджетах формы(создаст подпись возле поля ввода)

# category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
# устанавливаем связь один ко многим
# в параметр on_delete передаем SET_NULL- значит что при удалении категории поле останется пустым
# обязательно в это случае указываем параметр null=True, так как эта  связь требует, чтобы поле объекта, на которое
# указывает ссылка, допускало значение NULL.

# class Films(models.Model):
#     title = models.CharField("Название", max_length=100)
#     slogan = models.CharField("Слоган", max_length=100, default='')
#     description = models.TextField("Описание")
#     poster = models.ImageField("Постер", upload_to="movies/")
#     year = models.PositiveSmallIntegerField("Дата выхода", default=2019)
#     country = models.CharField("Страна", max_length=30)
#     director = models.ManyToManyField(ActorsDirectors, verbose_name="режиссер", related_name="film_director")
#     actor = models.ManyToManyField(ActorsDirectors, verbose_name="актеры", related_name="film_actor")
#     genre = models.ManyToManyField(Genres, verbose_name="жанры")
#     premiere_in_world = models.DateField("Примьера в мире", default=date.today)
#     budget = models.PositiveIntegerField("Бюджет", default=0,
#                                          help_text="указывать сумму в долларах")
#     fees_in_usa = models.PositiveIntegerField(
#         "Сборы в США", default=0, help_text="указывать сумму в долларах"
#     )
#     fess_in_world = models.PositiveIntegerField(
#         "Сборы в мире", default=0, help_text="указывать сумму в долларах"
#     )
#     category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
#     url = models.SlugField(max_length=160, unique=True)
#     draft = models.BooleanField("Черновик", default=False)
#
#
#     def __str__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         return reverse("movie_detail", kwargs={"slug": self.url})
#
#     def get_review(self):
#         return self.reviews_set.filter(parent__isnull=True)
#
#     class Meta:
#         verbose_name = "Фильм"
#         verbose_name_plural = "Фильмы"

# Создадим модель Кадры из фильма

# film = models.ForeignKey(Films, verbose_name='Фильм', on_delete=models.CASCADE)
# в параметр on_delete передаем каскадное удаление, это значит что если удалить фильм удаляться и кадры
#
# class MovieShots(models.Model):
#     title = models.CharField("Заголовок", max_length=100)
#     description = models.TextField("Описание")
#     image = models.ImageField("Изображение", upload_to="movie_shots/")
#     film = models.ForeignKey(Films, verbose_name='Фильм', on_delete=models.CASCADE)
#
#
#     def __str__(self):
#         return self.title
#
#
#     class Meta:
#         verbose_name = "Кадр из фильма"
#         verbose_name_plural = "Кадры из фильма"

# Создадим модель звезды рейтинга
#
# ordering = ["-value"] - сортируем по переменной value по убыванию
#
# class RatingStar(models.Model):
#     value = models.SmallIntegerField("Значение", default=0)
#
#
#     def __str__(self):
#         return f'{self.value}'
#
#
#     class Meta:
#         verbose_name = "Звезда рейтинга"
#         verbose_name_plural = "Звезды рейтинга"
#         ordering = ["-value"]

# Создадим модель Рейтинг
#
# class Rating(models.Model):
#     ip = models.CharField("IP адрес", max_length=15)
#     star = models.ForeignKey(RatingStar, verbose_name='звезда', on_delete=models.CASCADE)
#     film = models.ForeignKey(Films, verbose_name='Фильм', related_name="ratings", on_delete=models.CASCADE)
#
#
#     def __str__(self):
#         return f"{self.star} - {self.movie}"
#
#     class Meta:
#         verbose_name = "Рейтинг"
#         verbose_name_plural = "Рейтинги"

# Создадим модель Отзывы
#
# parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
# 'self' - запись будет ссылаться на запись в этой же таблице
# blank=True - поле необязательно для заполнения
#
#
# class Reviews(models.Model):
#     email = models.EmailField()
#     name = models.CharField("Имя", max_length=100)
#     text = models.TextField("Сообщение", max_length=5000)
#     parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
#     film = models.ForeignKey(Films, verbose_name='Фильм', on_delete=models.CASCADE)
#
#
#     def __str__(self):
#         return f"{self.name} - {self.film}"
#
#
#     class Meta:
#         verbose_name = "Отзыв"
#         verbose_name_plural = "Отзывы"

# После создания моделей делаем необходимые миграции и регистрируем модели в admin


# from .models import *
#
#
# admin.site.register(Category)
# admin.site.register(ActorsDirectors)
# admin.site.register(Genres)
# admin.site.register(Films)
# admin.site.register(MovieShots)
# admin.site.register(RatingStar)
# admin.site.register(Rating)
# admin.site.register(Reviews)

# Что бы изменить язык административной панели делаем следующее
# В файле settings меняем параметр LANGUAGE_CODE = 'ru'

# Подключаем в settings медиа файлы. Создадим в главной папке проекта папку Медиа, в которую будем сохранять необходимые
# фото которые прописали в поле image

# MEDIA_URL = 'media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#

# Далее необходимо сделать импорты в основной файл url проекта
# from django.conf import settings - импорт файла settings
#

# DEBUG - Программа-отладчик, которую используют для проверки и отладки выполняемых файлов.

# Пропишем условие при котором Django будет раздавать медиа-файлы при включенном debug режиме
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Опишем первую view которая будет выводить список фильмов
#
# from django.shortcuts import render - импортируем render который будет обрабатывать html-страницы
#
# from django.views.generic.base import View - Базовый вид на основе мастер-класса. Все остальные представления на основе классов
# наследуются от этого базового класса. Это не строго общее представление, поэтому его также можно импортировать из файлов
# django.views. - from django.views import View
#
# from .models import * - импортируем все модели
#
# создадим класс который будет обращаться к нашей модели Films и наследовать View
# Создадим в нем функцию которая вторым параметром принимает request
# переменную films которая получит все атрибуды модели Films
# возращаем нужную страницу, в словарь передаем переменную films
#
# class FilmsViews(View):
#     def get(self, request):
#         films = Films.objects.all()
#         return render(request, 'movies/movies.html', {'movie_list': films})

# Далее необходимо подключить static файлы к проекту
# В корневом каталоге проекта создадим папку static
# Подключим ее в settings проекта
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]
#
# Подключим templates к проекту в settings проекта
#
# TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
#
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [TEMPLATE_DIR],
#
# Создадим в templates html файл movies.htmp
#
# Далее в файле movies.htmp необходимо подключить static файлы
#
# {% load static %}

# Пропишем пути к CSS стилям
#
# <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}">
# <link rel="stylesheet" href="{% static 'css/style.css' %}" type="text/css" media="all">
# <link href="{% static 'css/font-awesome.css' %}" rel="stylesheet">

# Далее блок который отвечает за вывод списка фильмов возьмем в цикл for и передадим необходимые нам атрибуды

# <body>
#     {% for movie in movie_list %}
#         {{ movie.title }}
#     {% endfor %}
# </body>

# {% for movie in movie_list %}
# <div class="col-md-4 product-men">
#     <div class="product-shoe-info editContent text-center mt-lg-4" >
#         <div class="men-thumb-item">
#             <img src="{{ movie.poster.url}}" class="img-fluid" alt="" >
#         </div>
#         <div class="item-info-product">
#             <h4 class="">
#                 <a href="moviesingle.html" class="editContent" >К звездам</a>
#                 {{ movie.title }}
#             </h4>
#
#             <div class="product_price">
#                 <div class="grid-price">
#                     <span class="money editContent" >{{ movie.slogan }}</span>
#                 </div>
#             </div>
#             <ul class="stars">
#                 <li><a href="#"><span class="fa fa-star" aria-hidden="true" ></span></a></li>
#                 <li><a href="#"><span class="fa fa-star" aria-hidden="true" ></span></a></li>
#                 <li><a href="#"><span class="fa fa-star-half-o" aria-hidden="true" ></span></a></li>
#                 <li><a href="#"><span class="fa fa-star-half-o" aria-hidden="true" ></span></a></li>
#                 <li><a href="#"><span class="fa fa-star-o" aria-hidden="true" ></span></a></li>
#             </ul>
#         </div>
#     </div>
# </div>
# {% endfor %}

# Подключаем url

# В основной url проета необходимо подключить url приложений
#
# Для этого импортируем include
#
# подлкючаем url приложения movies
#
# path("", include("movies.urls"))

# Описываем  url для FilmsViews
#
# from django.urls import path
# from . import views
#
#
# urlpatterns = [
#     path('', views.FilmsViews.as_view())
# ]