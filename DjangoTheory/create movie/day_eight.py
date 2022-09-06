# Действия для админ панели

# Создадим действия для модели Films
# Опишем метод unpublish который будет снимать публикацию с сайта и метод publish который наоборот будет их выводит
#
# в переменной queryset находится вся информация класса(модели) Films(передавали во view) метод update будет передавать в переменную row_update количество измененных публикаций
# row_update = queryset.update(draft=True)
# self.message_user(request, f'{message_bit}') - будет выводить для пользователя переменную message_bit на экран
#
# def unpublish(self, request, queryset):
#     # Снять с публикации
#     row_update = queryset.update(draft=True)
#     if row_update == 1:
#         message_bit = '1 запись обновлена'
#     else:
#         message_bit = f'{row_update} записей обновлено'
#     self.message_user(request, f'{message_bit}')
#
# def publish(self, request, queryset):
#     # Опубликовать
#     row_update = queryset.update(draft=False)
#     if row_update == 1:
#         message_bit = '1 запись обновлена'
#     else:
#         message_bit = f'{row_update} записей обновлено'
#     self.message_user(request, f'{message_bit}')


# publish.short_description = 'Опубликовать' будет выводить название в выпадающем списке действий, без этой строки кода будет
# выводится название метода(publish)

# publish.allowed_permissions = ('change',) - разрешение для пользователя на внесение изменений(пока не работает необходимо дописывать код)

# Далее в класс FilmsAdmin необходимо добавить переменную actions и передать в нее два новых метода
#
# actions = ['publish', 'unpublish']


# Добавление категорий на страницу

# Изменим view class FilmsViews
#
# Добавим метод get_context_data

# метод get_context_data - может использоваться для передачи содержимого или параметров вне модели в шаблон html
# Через super вызываем get_context_data непосредственного предка(class FilmsViews) для получения базовой реализации контекста

# две аналогичные строчки кода
# context = super().get_context_data( * args, ** kwargs)
# context = super(FilmsViews, self).get_context_data(*args, **kwargs)

# Добавляем новую переменную к контексту и передаем ей все обьекты модели  Category
#
# context['categories'] = Category.objects.all()

# def get_context_data(self, *args, **kwargs):
#     context = super().get_context_data(*args, **kwargs)
#     # context = super(FilmsViews, self).get_context_data(*args, **kwargs)
#     context['categories'] = Category.objects.all()
#     return context

# Далее передаем новую переменную categories в цикл for в шаблон html header в участок кода который отвечает за вывод списка
# категорий

# <ul>
#     {% for category in categories %}
#         <li><a href="/">{{ category.name }}</a></li>
#     {% endfor %}
# </ul>


# Так как наш сайт может содержать много страниц для отображения списка категорий необходимо будет добавить метод get_context_data
# в каждую view, для того что бы этого избежать можно использовать несколько способов
#
# 1. Создать класс mixin который будет наследоваться от класса  ContextMixin. Все остальные классы будут наследовать новый класс
# Класс ContextMixin - Миксин контекста по умолчанию, который передает ключевые аргументы, полученные функцией get_context_data
# как контекст шаблона

# class Proba(ContextMixin):
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.all()
#         return context
#
# class FilmsViews(ListView, Proba):
#     """Список фильмов"""
#     model = Films
#     queryset = Films.objects.filter(draft=False)
#     template_name = 'movies/movies.html'
#     context_object_name = 'movie_list

# 2. Создать templatetags
# В папке movies создать папку templatetags
# Далее в папке templatetags создать файл __init__.py который будет говорить что эта папка модуль python
# Далее создадим файл movie_tag в котором будем писать template tags
# В файле movie_tag делаем импорты
#
# from django import template
# from movies.models import Category
#
# подключаем файлы папки templatetags
#
# register = template.Library()

# Описываем метод который выведет все категории
# def get_categories():
#     """Вывод всех категорий"""
#     return Category.objects.all()

# Оборачиваем в декоратор в register.simple_tag() который зарегистрирует функцию get_categories() как template tag
#
# @register.simple_tag()
# def get_categories():
#     """Вывод всех категорий"""
#     return Category.objects.all()

# После этого обзательно перезапускаем сервер что бы тег зарегестрировался

# Далее в файле header.html подключаем template tag
#
# {% load movie_tag %}
# вызовем template tag get_categories и данные которые он вернет заносим в переменную categories
#
# {% get_categories as categories %}

# Реализация вывода последних добавленных фильмов
# В django есть два типа template tag:
# simple_tag
# inclusion_tag
# Отличие в том что inclusion_tag умеет рендерить шаблон

# Описываем метод который выведет последние фильмы
# Из sidebar.html перенесем блок кода отвечающий за вывод последних фильмов в отдельный файл - last_movie.html
# В папке tamplates - папка movies создадим папку tags и в ней файл last_movie.html

# from movies.models import Category, Films импортируем модель Films

# В файле movie_tag опишем функцию get_last_movies

# в переменную movies передаем список фильмов отсортированных по id с помощью параметра order_by(сортировка от меньшего к большему)
# далее разворачиваем полученный список и с помощью среза выводим определенное кол-во фильмов, которое по умолчанию равно 5
#
# def get_last_movies(count=5):
#     movies = Films.objects.order_by("id")[::-1][:count]
#     return {"last_movies": movies}

# Оборачиваем в декоратор в register.inclusion_tag который зарегистрирует функцию get_last_movies как template tag и передаем в
# него путь к шаблону который он будет рендерить
#
# @register.inclusion_tag('movies/tags/last_movie.html')
# def get_last_movies(count=5):
#     movies = Films.objects.order_by("id")[::-1][:count]
#     return {"last_movies": movies}

# далее в файле last_movie.html проходим циклом for по ключу last_movies
#
# <div class="deal-leftmk left-side">
#     <h3 class="sear-head editContent">Последние добавленные</h3>
#     {% for movie in last_movies %}
#         <div class="special-sec1 row mt-3 editContent">
#             <div class="img-deals col-md-4">
#                 <img src="{{ movie.poster.url }}" class="img-fluid" alt="">
#             </div>
#             <div class="img-deal1 col-md-4">
#                 <h3 class="editContent">{{ movie.title }}</h3>
#                 <a href="{{ movie.get_absolute_url }}" class="editContent"></a>
#             </div>
#         </div>
#     {% endfor %}
# </div>

# после этого перезапустим сервер что бы зарегестрировать template tag
# после в sidebar.html подключим template tag
#
# {% load movie_tag %}
#
# далее вызовем функцию template tag - get_last_movies и передадим в нее count
#
# {% get_last_movies count=2 %}