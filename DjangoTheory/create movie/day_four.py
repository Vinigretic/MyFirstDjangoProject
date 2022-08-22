# Подключение кадров из фильма
# 1.Скачиваем картинки и добавляем через админ-панель
# 2. Добавляем в movie_detail.html

# <p>
#     {% for image in movie.movieshots_set.all %}
#         <img src= {{ image.image.url }} class="img-fluid" alt="{{ image.description }}">
#     {% endfor %}
# </p>

# За кадры из фильма отвечает модель MovieShots которая связывается с моделью Films. Во view переменная которую мы передаем
# в html называется movie(содержит все атрибуты Film).Мы обращаемся к обьекту movie
# далее к модели MovieShots забираем все завязанные на нашей модели movie обьекты, из модели MovieShots с помощью метода set
# и проходим циклом
# {% for image in movie.movieshots_set.all %}
# image - это наш обьект из MovieShots, обращаемся к полю image и url что бы вывести адрес нашего изображения(путь)
# {{ image.image.url }}
# выведем описание - alt="{{ image.description }}

# 2. Отзывы
# Создание формы

# Передадим в movie_detail.html поля модели Reviews

#                    <form action="{% url 'add_review' movie.id %}" method="post" class="mt-4">-->
# <!--                        {% csrf_token %}-->
# <!--                        <div class="form-group editContent">-->
# <!--                            <label for="contactcomment" class="editContent">-->
# <!--                                Ваш комментарий *-->
# <!--                            </label>-->
# <!--                            <textarea class="form-control border" rows="5" name="text"-->
# <!--                                      id="contactcomment" required=""></textarea>-->
# <!--                        </div>-->
# <!--                        <div class="d-sm-flex">-->
# <!--                            <div class="col-sm-6 form-group p-0 editContent">-->
# <!--                                <label for="contactusername" class="editContent">-->
# <!--                                    Имя *-->
# <!--                                </label>-->
# <!--                                <input type="text" class="form-control border" name="name"-->
# <!--                                       id="contactusername" required="">-->
# <!--                            </div>-->
# <!--                            <div class="col-sm-6 form-group ml-sm-3 editContent">-->
# <!--                                <label for="contactemail" class="editContent">-->
# <!--                                    Email *-->
# <!--                                </label>-->
# <!--                                <input type="email" class="form-control border" name="email"-->
# <!--                                       id="contactemail" required="">

# Опишем view AddReview

# class AddReview(View):
#     #отзывы
#     def post(self, request, pk):
#         print(request.POST)
#         return redirect('/')

# В этом классе используем метод post, это будет подзапрос HTTP, который принимает request и рк - id фильма

# def post(self, request, pk):
#
# Смотрим в консоль что нам придет в подзапросе
#
# print(request.POST)
# request - содержит словарь с данными об отзыве

# И после отправки отзыва делаем возврат на главную страницу
#
# return redirect('/')

# 3. Опишем url для AddReview

# urlpatterns = [
#     path('', views.FilmsViews.as_view()),
#     # path('<int:pk>/', views.FilmsDetailView.as_view())
#     path('<slug:slug>/', views.FilmsDetailView.as_view(), name='movie_detail'),
#     path('review/<int:pk>/', views.AddReview.as_view(), name='add_review'),
#
# ]

# В форме в action передадим имя нашей url и id фильма movie.id
#
# <form action="{% url 'add_review' movie.id %}" method="post" class="mt-4">

# 4. Опишем форму для проверки валидности данных  которые приходят со стороны клиента
# В файле form.py сделаем необходимые импорты
#
# from django import forms
# from .models import Reviews


# Опишем форму которая будет наследоваться от модели Reviews
# в класс Мета передадим название модели и необходимые поля
#
# class ReviewForm(forms.ModelForm):
#     """Форма отзывов"""
#     class Meta:
#         model = Reviews
#         fields = ("name", "email", "text")

# Импортируем нашу форму во view
#
# from .forms import ReviewForm

# Изменим view AddReview первый способ
#
# class AddReview(View):
#     """Отзывы"""
#     # первый способ
#     def post(self, request, pk):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.film_id = pk
#             form.save()
#         return redirect('/')

# form = ReviewForm(request.POST) - передаем в форму данные из запроса
# if form.is_valid(): - проверяем форму на валидность данных, если она валидна можем ее сохранить, но так как отзыв
# должен привязываться на определенный фильм, нужно указать на какой фильм привязывать отзыв

# form = form.save(commit=False) - преостанавливаем сохранение нашей формы для того что бы внести какие-либо изменения
# form.film_id = pk - указываем фильм к которому нужно привязаться
# в модели Reviews по полю film осуществляется связь с моделью Film, в это поле попадает id фильма и в БД это поле называется
# film_id, в рк заходит id фильма поэтому мы прописываем что  film_id = pk
# form.save() - сохраняем форму, данные будут записаны в бд


# Второй способ, когда есть обьект фильма

# def post(self, request, pk):
#     form = ReviewForm(request.POST)
#     movie = Films.objects.get(id=pk)
#     if form.is_valid():
#         form = form.save(commit=False)
#         form.film = movie
#         form.save()
#     return redirect('/')

# movie = Films.objects.get(id=pk) - в переменную movie с помощью метода get сохраняем обьект по полученному id, делая
# запрос в БД
# form.film = movie - говорим что поле film равно ранее полученному обьекту

# Отобразим список отзывов под фильмом

# Для этого пройдем циклом по всем обьектам модели reviews - movie.reviews_set.all

# {% for review in movie.reviews_set.all %}
#         <div class="media py-5">
#             <img src="bundles/images/te2.jpg" class="mr-3 img-fluid" alt="image">
#             <div class="media-body mt-4">
#                 <h5 class="mt-0 editContent">
#                     {{ review.name }}
#                 </h5>
#                 <p class="mt-2 editContent">
#                     {{ review.text }}
#                 </p>
#                  </div>
#         </div>
# {% endfor %}

# Для того что бы после отправки отзыва остатьтя на той же странице изменим view
# передадим в redirect результат работы метода get_absolute_url
#
# return redirect(movie.get_absolute_url()) - здесь выстроится адрес нашего фильма и мы будем перенаправлены на туже самую
# страницу
#
# class AddReview(View):
#     def post(self, request, pk):
#         form = ReviewForm(request.POST)
#         movie = Films.objects.get(id=pk)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.film = movie
#             form.save()
#         return redirect(movie.get_absolute_url())