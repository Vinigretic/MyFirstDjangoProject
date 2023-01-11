# Добавление простых страниц(статических)
# Простые страницы нужны для того чтобы администратор сайта мог сам поменять текст на страничке через админку,
# без внесения изменения в код
#
# В файл settings внесем дополнения
# Добавляем в INSTALLED_APPS
# 'django.contrib.sites',
# 'django.contrib.flatpages',
#
# Установим переменную
# SITE_ID = 1
#
# Добавим url в главную url проекта
# path('pages/', include('django.contrib.flatpages.urls')),
#
# В файл settings внесем дополнения
# Добавляем в MIDDLEWARE
# 'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
#
# Делаем миграции
# python manage.py migrate
#
# Через админ панель добавим страницу about
#
# В папке templates создадим папку pages в ней файл about.html

