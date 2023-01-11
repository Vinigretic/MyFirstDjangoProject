# Добавление фото в admin панель
#
# Изменим класс ActorAdmin
#
# Добавим в него метод который будет выводить изображение, для этого используем метод mark_safe
# метод mark_safe() - в админке есть защита от  HTML-включений и она заранее экранировала все символы так, чтобы теги
# преобразовались в текст. Чтобы всё же добавить именно тег, нужно явно сказать админке, что строка с тегами безопасная.
# Этот метод работает со строкой
#
# def get_image(self, obj):
#     return mark_safe(f'<img src={obj.image.url} width="50" height= "60"')
#
# Добавим метод get_image в list_display
#
# list_display = ("name", "age", 'get_image')
#
# Изменим отображение названия колонки с get_image на Изображение, с помощью метода short_description
#
# get_image.short_description = 'Изображение'
#
# Зафиксируем изображение при переходе на определенное имя
#
# readonly_fields = ('get_image',)


# Добавим тоже самое в класс MovieShotsAdmin
#
# @admin.register(MovieShots)
# class MovieShotsAdmin(admin.ModelAdmin):
#     """Кадры из фильма"""
#     list_display = ("title", "film", 'get_image')
#     readonly_fields = ('get_image',)
#
#     def get_image(self, obj):
#         return mark_safe(f'<img src={obj.image.url} width="50" height= "60"')
#
#     get_image.short_description = 'Изображение'

# Изменим отображение названия приложения в админке с movies на фильмы
# Для этого в файле apps.py добавим параметр verbose_name
#
# class MoviesConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'movies'
#     verbose_name = 'Фильмы'

# Далее добавим в файл __init__.py следующую запись
#
# default_app_config = 'movies.apps.MoviesConfig'

# Перейдем в файл admin
# Изменим название сайта
#
# admin.site.site_title = 'Django Movies'
#
# Изменим его заголовок
#
# admin.site.site_header = 'Django Movies'

# Добавим кадры из фильма в фильмы
# Для этого в файле admin опишем новый класс
#
# class MovieShotsInline(admin.TabularInline):
#     model = MovieShots
#     extra = 0
#
# Используем горизонтальное отображения с помомощью TabularInline
#
# добавим созданный класс в inlines в классе FilmsAdmin
#
# inlines = [MovieShotsInline, ReviewInline]

# Добавим вывод изображений. Отредактируем класс MovieShotsInline добавив
#
# readonly_fields = ('get_image',)
#
#
# def get_image(self, obj):
#     return mark_safe(f'<img src={obj.image.url} width="100" height= "110"')
#
#
# get_image.short_description = 'Изображение'

# Добавим отображение постера
#
# в класс FilmsAdmin добавим метод get_image и изменим url на url к постеру
#
# return mark_safe(f'<img src={obj.poster.url} width="100" height= "110"')
#
# добавим get_image к fieldsets там где хотим его вывести
#
# (None, {
#             "fields": ("description", "poster", 'get_image')
#         }),

# добавим readonly_fields
#
# readonly_fields = ('get_image',)

# Изменим имя отображения постера, отредактируем метод get_image
#
# get_image.short_description = 'Постер'

# Разместим постер и его изображение в одну строку. Для этого возьмем в кортеж поле "poster" и 'get_image'
#
# (None, {
#     "fields": ("description", ("poster", 'get_image'))
# }),