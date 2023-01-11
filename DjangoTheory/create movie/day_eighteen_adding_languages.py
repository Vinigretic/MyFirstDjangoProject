# # Мультиязычность для сайта
# # pip install django-modeltranslation
# # python manage.py makemigrations
# # python manage.py migrate
# ## python manage.py update_translation_fields
# # django-admin makemessages -l en -e html
# ## django-admin compilemessages
# 1. Добавим  settings.py в MIDDLEWARE - django.middleware.locale.LocaleMiddleware',
#
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.locale.LocaleMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
# ]
#
# Настройки языка должны быть такими
# LANGUAGE_CODE = 'ru'
#
# TIME_ZONE = 'UTC'
#
# USE_I18N = True
#
# USE_L10N = True
#
# USE_TZ = True
#
# 2. Изменим основную url проекта добавив путь для изменения языков - path('i18n/', include('django.conf.urls.i18n'))
# добавим импорт
# from django.conf.urls.i18n import i18n_patterns
#
# отредактируем url
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('ckeditor/', include('ckeditor_uploader.urls')),
#     path('i18n/', include('django.conf.urls.i18n')),
# ]
# здесь добавляем сслыки на приложения которые должны будут переводится
# urlpatterns += i18n_patterns(
#     path('pages/', include('django.contrib.flatpages.urls')),
#     path('contact/', include("contact.urls")),
#     path("", include("movies.urls")),
# )
#
# 3. Установим приложение для перевода моделей
# pip install django-modeltranslation
#
# 4. Добавить приложение в раздел INSTALLED_APPS файла settings.py:
# INSTALLED_APPS = (
#     ...
#     'modeltranslation',
# )
# 5. Добавить в settings.py список языков, переводы на которые будут доступны
# # список доступных языков
# gettext = lambda s: s
# LANGUAGES = (
#     ('ru', gettext('Russian')),
#     ('en', gettext('English')),
# )
#     # ('uk', 'Ukrainian'),
#
# Модуль gettext предоставляет службы интернационализации (I18N) и локализации (L10N) для ваших
# Python модулей и приложений. Мне понадобилось установить этот модуль отдельно и после установки перезагрузить
# комп
#
# 6. Создадим файл translation.py, этот файл обычно один на весь проект и создается в корне проекта.
# В этом файле нужно создать классы в которых указываем те поля нужных моделей, которые будут участвовать
# в переводе. Это приложение добавит к моделям поля для перевода
#
# 7. Делаем миграции
# python manage.py makemigrations
# python manage.py migrate
#
# Если в бд уже есть информация необходимо синхронизировать поля. Для это выполняем след команду
# python manage.py update_translation_fields
#
# 8. Затем в файл admin.py делаем импорт
# from modeltranslation.admin import TranslationAdmin
#
# И для тех моделей которые будут учавствовать в переводе меняем класс наследования на TranslationAdmin
#
# Изменим описание для ckeditor
#
# class FilmsAdminForm(forms.ModelForm):
#     description_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
#     description_en = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
#
# 9. Отредактируем файл header.html добавив в него форму для перевода. Эта форма будет показывать все
# языки которые прописаны в settings.py
# #
# <form action="{% url 'set_language' %}" method="post">{% csrf_token %}
#                         <input name="next" type="hidden" value="{{ redirect_to }}">
#                         <select name="language">
#                             {% get_current_language as LANGUAGE_CODE %}
#                             {% get_available_languages as LANGUAGES %}
#                             {% get_language_info_list for LANGUAGES as languages %}
#                             {% for language in languages %}
#                                 <option value="{{ language.code }}"{% if language.code == LANGUAGE_CODE %}
#                                         selected{% endif %}>
#                                     {{ language.name_local }} ({{ language.code }})
#                                 </option>
#                             {% endfor %}
#                         </select>
#                         <input type="submit" value="Go">
# </form>
#
# и подключим i18n
#
# {% load i18n movie_tag %}
#
# 10. Добавление перевода к статическому контенту
# Отредактируем файл movie_detail.html
#
# Снова подключим i18n
# {% load static i18n %}
#
# и к каждому тексту который нужно перевести добавим темплейт тег trans
# {% trans 'Год' %}, {% trans 'Страна' %} и т.д
#
# 11. Создание файлов для перевода
# В корне проекта создать папку locale
# И сделать следующую команду, которой мы говорим что нам нужно сделать locale для английского языка и искать их
# нужно в html файлах
# django-admin makemessages -l en -e html
# После выполнения этой команды в папке locale должна создаться папка en, в ней папка LC_MESSAGES,а вней
# файл django.po
# В файле django.po указано в каком html файле находится строка которую нужно перевести, так же в этот
# файл нужно вставить перевод
# Переводы из виртуального окружения удаляем за ненадобностью
# После того как мы внесли все изменения в файл django.po необходимо выполнить след команду
# django-admin compilemessages
# После этого должен появится файл django.mo
#
# 12. Добавим в файл settings.py путь к папке locale
#
# LOCALE_PATHS = (
#     os.path.join(BASE_DIR, 'locale'),
# )