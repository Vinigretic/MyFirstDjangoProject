# Установка текстового редактора для админ панели
# 1. Установим Django CKEditor в проект
# pip install django-ckeditor
#
# 2. Добавим ckeditor в INSTALLED_APPS
#
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'movies',
#     'ckeditor'
# ]
#
# 3. В settings пропишем путь к папке static
#
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#
# Закоментируем строку
#
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]
#
# 4. Выключаем DEBUG
#
# DEBUG = False
#
# 5. Выполним команду python manage.py collectstatic - которая перезапишет static файлы
#
# 6. Включим DEBUG
#
# DEBUG = True
#
# 7. Раскоментируем строку
#
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]
# Закоментрируем строку
#
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# 8. Для загрузки изображений через редактор необходимо добавить в INSTALLED_APPS ckeditor_uploader
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'movies',
#     'ckeditor',
#     'ckeditor_uploader'
# ]
# 9. Пропишем в settings настройку  пути куда загружать изображения
#
# CKEDITOR_UPLOAD_PATH = "uploads/"
#
# 10. Пропишем url ckeditor в корневой url проекта
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('ckeditor/', include('ckeditor_uploader.urls')),
#     path("", include("movies.urls")),
# ]

# 11 Добавим виджет к нашей форме которая отображается в админ панели в файл admin.py. Редактор встроим туда где описание
# фильма(модель Films)
#
# импортируем формы
# from django import forms
#
# Для поддержки загрузки файлов импортируем
# from ckeditor_uploader.widgets import CKEditorUploadingWidget
#
# Создадим класс который наследует forms.ModelForm

# переменная description отвечает за описание фильма, добавим в нее - widget=CKEditorUploadingWidget()
# Это поле добавит редактор в админ панель

# class FilmsAdminForm(forms.ModelForm):
#     description = forms.CharField(widget=CKEditorUploadingWidget())
#     class Meta:
#         model = Films
#         fields = '__all__'

# 12. Форму FilmsAdminForm необходимо подключить к классу FilmsAdmin
# Для этого в классе FilmsAdmin добавим атрибут form и передадим в него FilmsAdminForm
# form = FilmsAdminForm

# 13. Изменим отображение названия поля description с английского на русский
# для этого добавим в FilmsAdminForm в поле description - label='Описание'
#
# class FilmsAdminForm(forms.ModelForm):
#     description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
#     class Meta:
#         model = Films
#         fields = '__all__'

# 14. Расширим панель настроект в ckeditor
# Для этого скопируем настройки из докуметации и добавим их в settings
#
# CKEDITOR_CONFIGS = {
#     'default': {
#         'skin': 'moono',
#         # 'skin': 'office2013',
#         'toolbar_Basic': [
#             ['Source', '-', 'Bold', 'Italic']
#         ],
#         'toolbar_YourCustomToolbarConfig': [
#             {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
#             {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
#             {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
#             {'name': 'forms',
#              'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
#                        'HiddenField']},
#             '/',
#             {'name': 'basicstyles',
#              'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
#             {'name': 'paragraph',
#              'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
#                        'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
#                        'Language']},
#             {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
#             {'name': 'insert',
#              'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
#             '/',
#             {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
#             {'name': 'colors', 'items': ['TextColor', 'BGColor']},
#             {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
#             {'name': 'about', 'items': ['About']},
#             '/',  # put this to force next toolbar on new line
#             {'name': 'yourcustomtools', 'items': [
#                 # put the name of your editor.ui.addButton here
#                 'Preview',
#                 'Maximize',
#
#             ]},
#         ],
#         'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
#         # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
#         # 'height': 291,
#         # 'width': '100%',
#         # 'filebrowserWindowHeight': 725,
#         # 'filebrowserWindowWidth': 940,
#         # 'toolbarCanCollapse': True,
#         # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
#         'tabSpaces': 4,
#         'extraPlugins': ','.join([
#             'uploadimage', # the upload image feature
#             # your extra plugins here
#             'div',
#             'autolink',
#             'autoembed',
#             'embedsemantic',
#             'autogrow',
#             # 'devtools',
#             'widget',
#             'lineutils',
#             'clipboard',
#             'dialog',
#             'dialogui',
#             'elementspath'
#         ]),
#     }
# }

# 15. Добавление youtubе в редактор
# Для этого скачаем Youtube Plugin и добавим его в
# C:\Users\VIka\PycharmProjects\DjangoProject\Movie\static\ckeditor\ckeditor\plugins\youtube
# предварительно разархивировав
# Далее в настройкак редактора в settings необходимо прописать плагин youtubе

# 'extraPlugins': ','.join([
#             'uploadimage', # the upload image feature
#             # your extra plugins here
#             'div',
#             'autolink',
#             'autoembed',
#             'embedsemantic',
#             'autogrow',
#             # 'devtools',
#             'widget',
#             'lineutils',
#             'clipboard',
#             'dialog',
#             'dialogui',
#             'elementspath',
#             'youtubе'

# Далее нам нужно добавить его в настройки к той панели где бы мы хотели видеть его в редакторе
# Добавим в конец

# 'toolbar_YourCustomToolbarConfig': {'name': 'yourcustomtools', 'items': [
#                 # put the name of your editor.ui.addButton here
#                 'Preview',
#                 'Maximize',
#                 'Youtube'
#
#             ]}

# 16. Для того что бы изменения в админ странице отображались на сайте необходимо внести изменения в html
# В movie_detail.html в участе кода который отвечает за вывод описания фильма добавим safe
#
# <p class="editContent">
#     {{ movie.description|safe }}
# </p>

# 17. Добавим видео с Youtube через админ панель
# Закоментируем абзац в movie_detail.html который ранее отображал ролик