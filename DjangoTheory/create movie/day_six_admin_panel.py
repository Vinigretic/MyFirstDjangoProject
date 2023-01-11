# Админка
# В файле admin.py мы можем писать классы с помощью которых мы можем конфигурировать админ панель
# Создадим класс для модели Категории
#
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name','url', 'id')

# Данный класс будет наследоваться от  admin.ModelAdmin
# list_display - позволяет конфигурировать список наших записей
# В него мы передаем поля модели Категории, в том порядке который нам нужен для отображения
#
# Далее наш созданный класс необходимо прописать в регистр
# admin.site.register(Category, CategoryAdmin)
#
# При входе в категории в админке мы мужем увидеть что для того что бы перейти дальше для редактирования, ссылкой всегда будет
# первая колонка которую мы передаем в list_display
# Что бы это изменить и сделать переход по названию добавим в наш класс list_display_links. Принимает название поля которое будет
# переходом
#
# list_display_links = ('name',)

# Регистрировать наши классы и модели мы можем с помощью декоратора

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name','url')
#     list_display_links = ('name',)

# Опишем класс к модели Films

# @admin.register(Films)
# class FilmsAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'url', 'draft')
#
# Добавим фильтрацию по категириям к фильмам
# Для этого используем переменную list_filter и в нее передаем поле по которому хотим фильтровать

# list_filter = ('category',)

# Добавим фильтрацию по году выхода фильма
#
# list_filter = ('category', 'year')

# Добавим поиск по фильмам. В переменную search_fields - передадим поля по которым хотим осуществлять поиск
#
# search_fields = ('title',)
#
# Если мы хотим добавить поле для поиска, которое является внешним ключем нам необходимо будет указать поле по которому
# будет осуществляться поиск
# Добавим поиск по полю категории. Так как в бд в таблице Films в поле category попадает id,
# указываем что поиск будет осуществляться по колонке name

# search_fields = ('title', 'category__name')

# Наша модель Films имеет связь с моделью Reviews, поэтому мы можем добавить отображение отзывов к каждому фильму
# Для это создадим класс ReviewInline который наследуется от класса StackedInline.
# Есть два класса
# 1. Класс StackedInline - разместит добавляемые записи вертикально
# 2. Класс TabularInline - разместит добавляемые записи горизонтально

#  В класс  ReviewInline передаем модель которую хотим связать с Films
#
# class ReviewInline(admin.StackedInline):
#     model = Reviews

# Далее в класс FilmsAdmin необходимо добавить атрибут inlines - работает со связями многие ко многим и один ко многим,
# и в него передать класс ReviewInline
#
# inlines = [ReviewInline]
# По умолчанию в админ панели так же отобразится три пустых отзыва, что бы это изменить необходимо добавить атрибут extra
#  в класс ReviewInline и в него передадим количество доп полей
#
# class ReviewInline(admin.StackedInline):
#     model = Reviews
#     extra = 1

# Сделаем поля name и email только для чтения
# class ReviewInline(admin.StackedInline):
#     model = Reviews
#     extra = 1
#     readonly_fields = ('name', 'email')

# Перенесем панель с кнопками удалить, сохранить и т.д. Для удобства вверх. для этого в класс FilmsAdmin добавим
# атрибут save_on_top и установим его в True
#
# @admin.register(Films)
# class FilmsAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'url', 'draft')
#     list_filter = ('category', 'year')
#     search_fields = ('title', 'category__name')
#     inlines = [ReviewInline]
#     save_on_top = True

# Изменим параметры сохранения.
# Если нам нужно создать новый фильм на базе существующего(что бы не заполнять все поля заново) нам нужно изменить параметры
# кнопки сохранить и добавить другой обьект. Изменим ее на сохранить как новый обьект
# Для этого в класс FilmsAdmin добавим атрибут save_as и устаноим его в True
# save_as = True

# Сделаем поле черновик редактируемым
# Для этого добавим атрибут list_editable и передадим в него название нужного поля
# list_editable = ('draft',)

# Изменим расположение наших полей в админке
# Для этого используем атрибут fieldsets, в который передаем кортеж, первое значение которого это название которое можно дать
# группируемым полям, если название не нужно прописываем None, второе значение это словарь ключем которого выступает
# атрибут fields, в его значения мы передаем поля кортеж в кортеже(обязательно) которые хотим сгруппировать

# fieldsets = (
#         (None, {
#             "fields": (("title", "slogan"),)
#         }),
#         (None, {
#             "fields": ("description", "poster")
#         }),
#         (None, {
#             "fields": (("year", "premiere_in_world", "country"),)
#         }),
#         ("Actors", {
#             "classes": ("collapse",),
#             "fields": (("actor", "director", "genre", "category"),)
#         }),
#         (None, {
#             "fields": (("budget", "fees_in_usa", "fess_in_world"),)
#         }),
#         ("Options", {
#             "fields": (("url", "draft"),)
#         }),
#     )
# Если мы хотим сделать что бы какаю-то группу полей можно было свернуть используем следующее
# В словарь передаем ключ "classes" значение ("collapse",)

# Если мы хотим исключить отображение каких либо полей в админке мы можем использовать атрибут fields и передать ему только
# те поля которые должны отображаться(кортеж в кортеже)

# fields = (('director', 'actor', 'genre'),)

#         ("Actors", {
#             "classes": ("collapse",),
#             "fields": (("actor", "director", "genre", "category"),)
#         }),


# Опишем класс для модели отзывов
#
# @admin.register(Reviews)
# class ReviewsAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'parent', 'film', 'id')
#
# Если нам нужно убрать доступ редактирования каких то полей, используем атрибут readonly_fields и передаем в него поля
# которые нельзя будет отредактировать
#
# readonly_fields = ('name', 'email')

# Опишем класы для остальных моделей
#
# @admin.register(Genres)
# class GenreAdmin(admin.ModelAdmin):
#     """Жанры"""
#     list_display = ("name", "url")
#
#
# @admin.register(ActorsDirectors)
# class ActorAdmin(admin.ModelAdmin):
#     """Актеры"""
#     list_display = ("name", "age")
#
#
# @admin.register(Rating)
# class RatingAdmin(admin.ModelAdmin):
#     """Рейтинг"""
#     list_display = ("film", "ip")
#
#
# @admin.register(MovieShots)
# class MovieShotsAdmin(admin.ModelAdmin):
#     """Кадры из фильма"""
#     list_display = ("title", "film")
#
#
# admin.site.register(RatingStar)