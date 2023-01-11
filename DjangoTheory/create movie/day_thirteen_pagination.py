# Пагинация (Pagination) – это порядковая нумерация страниц, которая в основном размещается вверху либо внизу страниц сайта.
# Добавили файл pagination.html в папку include
# отредактировали стили css
# Во view FilmsViews добавим параметр paginate_by который отвечает за количество фильмов которые будут отображаться на странице
# paginate_by = 2 - будет отображать по два фильма  на странице
# В файл movies.html добавили след код  с помощью которого передаем ссылку на файл pagination.html
# Include позваляет нам вставить любой html из любого шаблона в нужное нам место в коде
#
# <div class="grid-img-right mt-4 text-right bg bg1" >
#         {% include 'include/pagination.html' %}
# </div>

# Во view FilterFilmsView так же добавим параметр paginate_by и метод get_context_data для того что бы правильно работали
# фильтры по годам и жанрам
# Для этого в context передаем словарь с годами и жанрами
# и формируем правильные ссылки
# def get_context_data(self, *args, **kwargs):
#     context = super().get_context_data(*args, **kwargs)
#     context["year"] = ''.join([f"year={x}&" for x in self.request.GET.getlist("year")])
#     context["genre"] = ''.join([f"genre={x}&" for x in self.request.GET.getlist("genre")])
#     return context
