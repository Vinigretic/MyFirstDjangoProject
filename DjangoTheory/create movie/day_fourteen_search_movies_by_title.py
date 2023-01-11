# Поиск фильмов по названию
# Внесем корректировки в файл sidebar.html
# Откорректируем форму поиска
# Опишием новую view для поиска Search которая будет наследоваться от ListView
# ListView - Страница, представляющая список объектов.Пока это представление выполняется, оно self.object_list
# будет содержать список объектов (обычно, но не обязательно набор запросов), над которыми работает представление.
# DetailView, ListView - два общих представления на основе классов предназначены для отображения данных. Во многих проектах
# они обычно являются наиболее часто используемыми представлениями.
# paginate_by = 2 - добавим пагинацию
# в методе def get_queryset(self) фильтруем фильмы по полю title и применяем доп параметр icontains для того что бы не учитывался
# регистр и сравниваем с теми данными которые пришли в get запросе
# в методе def get_context_data(self, *args, **kwargs) в словарь добавляем то значение которое пришло в get запросе, это нужно
# для пагинации
#
# class Search(ListView):
#     # поиск фильмов
#
#     paginate_by = 2
#
#     def get_queryset(self):
#         return Films.objects.filter(title__icontains=self.request.GET.get('q').capitalize())
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['q'] = f'q=self.request.GET.get("q")&'
#         return context
#
#     template_name = 'movies/movies.html'
#     context_object_name = 'movie_list'

# Добавим новый url
#
# path('search/', views.Search.as_view(), name='search'),

# Добавим url  в форму в sidebar, установим метод get
# < form action = "{% url 'search' %}" method = "get" class ="d-flex editContent" >

# в файл pagination.html добавим q во все ссылки
# <a href="?{{q}}{{ genre }}{{ year }}page=1">1</a>
# <a href="?{{q}}{{ genre }}{{ year }}page={{ page_obj.previous_page_number|add:'-3' }}">
# <a class="pagination__link" href="?{{q}}{{ genre }}{{ year }}page={{ i }}">{{ i }}</a>
#
# <a href = "?{{q}}{{ genre }}{{ year }}page={{ page_obj.next_page_number|add:'3' }}" >
# <a class="pagination__link" href="?{{q}}{{ genre }}{{ year }}page={{ page_obj.paginator.num_pages }}">