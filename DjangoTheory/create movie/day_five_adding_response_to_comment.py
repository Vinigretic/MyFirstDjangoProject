# Добавка ответа на комментарий
# Для этого необходимо изменить форму
# Добавим поле для ввода данных
# < input type = "hidden" name = "parent" id = "contactparent" value = "" >
# тип - поле будет спрятано, имя - имя колонки из модели, id = "contactparent" и id="formReview" - даем имена по которым
# в дальнейшем коде будем получать id передавая в код эти имена


# < form action = "{% url 'add_review' movie.id %}" method = "post" class ="mt-4" id="formReview" >
# < input type = "hidden" name = "parent" id = "contactparent" value = "" >

# К отзывам добавим ссылку что бы мы могли оставить наш отзыв
# href="#formReview" - добавляем  id к нашей форме, при нажатии на эту ссылку пользователь будет подниматься к форме отправки
# отзыва
# onclick="addReview('{{ review.name }}', '{{ review.id }}'  - вызываем функцию addReview и передаем в нее имя и id пользователя
# того отзыва на который хотим ответить

# <a href="#formReview" onclick="addReview('{{ review.name }}', '{{ review.id }}' )">Ответить</a>

# Создадим скрипт и опишем функцию addReview
# Эта функция будет принимать name и id
# id - будет подставляться в поле parent
# имя пользователя, в поле самого сообщения -
# < textarea class ="form-control border" rows="5" name="text"id = "contactcomment" required = "" > < / textarea >

# Находим на нашей странице по id поле parent  добавляем в его атрибут value id который к нам пришел
# document.getElementById("contactparent").value = id;

# Далее по id находим наше поле для отзыва и добавляем в него имя пользователя и запятую
# document.getElementById("contactcomment").innerText = `${name},

# < script >
# function addReview(name, id) {
#     document.getElementById("contactparent").value = id;
#     document.getElementById("contactcomment").innerText = `${name}, `
# }
# < / script >

# Добавление родителя в отзыв(отобразит к какому отзыву привязан ответ)
#
# Изменим view AddReview
# в подзапросе ищем ключ parent, ключ parent - имя поля в html. Если оно будет выполнится код ниже, если нет будет None и
# ничего не произойдет
# Если имя есть мы в form.parent_id передаем значение ключа parent(передаем именно число не обьект, поэтому parent_id)
# так как значение будет строкой оборачиваем его в int

# if request.POST.get('parent', None):
#     form.parent_id = int(request.POST.get('parent'))


# class AddReview(View):
#     def post(self, request, pk):
#         form = ReviewForm(request.POST)
#         movie = Films.objects.get(id=pk)
#         if form.is_valid():
#             form = form.save(commit=False)
#             if request.POST.get('parent', None):
#                 form.parent_id = int(request.POST.get('parent'))
#             form.film = movie
#             form.save()
#         return redirect(movie.get_absolute_url())

# Добавим отображение аватарки к отзывам
# Подключим static файлы к movie_detail
# {% load static %}
#
# пропишем правильный путь к ним
#
# {% for review in movie.reviews_set.all %}
#                 <div class="media py-5">
#                     <img src="{% static 'images/te2.jpg' %}" class="mr-3 img-fluid" alt="image">

# Добавим вывод количества отзывов для каждого фильма
# В movie_detail -
# {{ movie.reviews_set.count }} - таблицы Films и Reviews связаны поэтому мы обращаемся к таблице Films через атрибут movie
# получаем id нужного фильма и для этого фильма достаем все отзывы из таблицы reviews, с помощью метода count считаем их
# количество

# div class="contact-single">
#     <h3 class="editContent" style="outline: none; cursor: inherit;">
#                     <span class="sub-tittle editContent"
#                           style="outline: none; cursor: inherit;">{{ movie.reviews_set.count }}</span>Оставить
#         отзыв</h3>


# Изменим отображени отзывов на странице, сделаем вложенность.
# Для этого изменим модель Films добавим метод get_review
# Этот метод будет возвращать список отзывов прикрепленных к фильму, фильтруя по полю parent и выводить те отзывы для
# которых поле parent = Null т.е те отзывы к которым нет отзывов
#
#
# def get_review(self):
#     return self.reviews_set.filter(parent__isnull=True)
#
# В  movie_detail вызовем метод get_review
#
# {% for review in movie.get_review %}
#
# В этом случае у нас будут рендерится только те отзывы у которых нет отзывов(родителя)

# Теперь выведем отзывы к отзывам

# review.reviews_set.all - обращаемся к отзывам и вызываем метод reviews_set.all - получая все отзывы которые завязаны на отзыве
# проходим циклом и выводим имена и текст отзывов

{% for rew in review.reviews_set.all %}
    <div class="media mt-5 editContent">
        <a class="pr-3" href="#">
            <img src="{% static 'images/te2.jpg' %}" class="img-fluid "
                 alt="image">
        </a>
        <div class="media-body">
            <h5 class="mt-0 editContent">{{ rew.name }}</h5>
            <p class="mt-2 editContent">{{ rew.text }}</p>
        </div>
    </div>
{% endfor %}