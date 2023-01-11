# Добавление рейтинга к фильму
# Модель для звезд рейтинга
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

# Создадим форму для возможности добавлять рейтинг
# Форму описываем основываясь на модели Rating и RatingStar
# В файл forms импортируем модели Rating и RatingStar

# from .models import Reviews, Rating, RatingStar

# Создаем класс RatingForm со связанной моделью Rating, которую указываем в классе Meta сдесь же указываем необходимое поле star
# Для того чтобы выводить список звезд мы должны переопределить поле star
# Забераем все звезды из модели RatingStar -  RatingStar.objects.all()
# добавляем витжет который генерирует список переключателей(радиокнопок) - widget=forms.RadioSelect()
#
# star = forms.ModelChoiceField(
#         queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
#     )
#
#
# class RatingForm(forms.ModelForm):
#     # форма добавления рейтинга
#     star = forms.ModelChoiceField(
#         queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
#     )


    # class Meta:
    #     model = Rating
    #     fields = ('star',)

# Так как нам необходимо отобразить данную форму на странице полного описания фильма - меняем views

# Импортируем RatingForm
# from .forms import ReviewForm, RatingForm

# редактируем класс FilmsDetailView который отвечает за полное описания фильма
# добавляем ему метод get_context_data который заберет данные от пользователя
# в переменную context создаем словарь - context = super().get_context_data(**kwards)
# добавляем ему новый ключ и забираем форму рейтинга - context['star_form'] = RatingForm()
#
# def get_context_data(self, **kwards):
#     context = super().get_context_data(**kwards)
#     context['star_form'] = RatingForm()
#     return context

# далее переменную context необходимо передать в html - файл создав форму

# <!--                        <form action="{% url 'add_rating' %}" method="post" name="rating">-->
# <!--                            <b>Рейтинг:</b>-->
# <!--                            {% csrf_token %}-->
# <!--                            <input type="hidden" value="{{ movie.id }}" name="movie">-->
# <!--                            <span class="rating">-->
# <!--                                {% for k, v in star_form.fields.star.choices %}-->
# <!--                                    <input id="rating{{ v }}" type="radio" name="star"-->
# <!--                                           value="{{ k }}">-->
# <!--                                    <label for="rating{{ v }}">{{ k }}</label>-->
# <!--                                {% endfor %}-->
# <!--                            </span>-->
# <!--                            <span class="editContent">4.0</span>-->
# <!--                        </form>-->

# в style.css вместо дефолтного изображения радиоелементов отображаем звезды

# .rating > label {
#   position: relative;
#   display: block;
#   float: right;
#   background: url('../images/star-off-big.png');
#   background-size: 30px 30px;
# }

# Меняем script.js
# ищем форму по ее имени - const rating = document.querySelector('form[name=rating]');
#
# далее при ее изменении забираем новые данные из формы let data = new FormData(this);
# с помощью fetch на url из нашей формы мы будем передавать POST запрос -  method: 'POST', и передавать информацию - body: data
#
#
# const rating = document.querySelector('form[name=rating]');
#
# rating.addEventListener("change", function (e) {
#     // Получаем данные из формы
#     let data = new FormData(this);
#     fetch(`${this.action}`, {
#         method: 'POST',
#         body: data
#     })
#         .then(response => alert("Рейтинг установлен"))
#         .catch(error => alert("Ошибка"))
# });

# Создадим новый класс AddStarRating во view который наследуется от класса View.
# Когда к нам придет пост запрос в форму RatingForm мы передадим request.POST и сгенерируем форму
# form = RatingForm(request.POST)
# Далее делаем проверку формы на валидность.
# Необходимо реализовать возможность для пользователя менять рейтинг для этого используем метод update_or_create с помощью которого
# утановленый уже рейтинг будет обновляться
# Что бы получить ip адресс клиента который отправил запрос применим след метод и передадим в него request
# ip=self.get_client_ip(request)
# В поле film_id передаем movie из пост запроса который получаем из скрытого поля в форме
# <input type="hidden" value="{{ movie.id }}" name="movie">
# film_id=int(request.POST.get("movie")),
# в defaults передаем словарь, ключем которого будет поле которое нам нужно изменить, и значение на которое мы меняем
# defaults={'star_id': int(request.POST.get("star"))}
# Если форма пройдет проверку результатом будет либо новый рейтинг либо если пользователь уже оставлял рейтинг будет его замена
# Если форма не валидна возвращаем ошибку
# return HttpResponse(status=400)

# Rating.objects.update_or_create(
#     ip=self.get_client_ip(request),
#     film_id=int(request.POST.get("movie")),
#     defaults={'star_id': int(request.POST.get("star"))}
#     )
#
# class AddStarRating(View):
#     """Добавление рейтинга фильму"""
#     def get_client_ip(self, request):
#         x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#         if x_forwarded_for:
#             ip = x_forwarded_for.split(',')[0]
#         else:
#             ip = request.META.get('REMOTE_ADDR')
#         return ip
#
#     def post(self, request):
#         form = RatingForm(request.POST)
#         if form.is_valid():
#             Rating.objects.update_or_create(
#                 ip=self.get_client_ip(request),
#                 film_id=int(request.POST.get("movie")),
#                 defaults={'star_id': int(request.POST.get("star"))}
#             )
#             return HttpResponse(status=201)
#         else:
#             return HttpResponse(status=400)


# Добавим url для view AddStarRating

# path("add-rating/", views.AddStarRating.as_view(), name='add_rating'),