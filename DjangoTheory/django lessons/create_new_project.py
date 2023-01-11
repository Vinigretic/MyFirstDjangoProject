# При создании нового приложения в проекте делаем следующее
#
# 1. python manage.py startapp firstapp - создаем приложение для Django проекта
# 2. В главной папке проекта в файле setting необходимо добавить новое приложение

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'firstapp.apps.FirstappConfig',  # добавили новое
#     'shops.apps.ShopsConfig',  # добавили новое
# ]

# 3. URL проекта необходимо импортировать views всех создаваемых приложений
# При импорте лучше сразу создавать псевдонимы так как файлы могут называться одинаково

# from firstapp import views as views_firstapp
# from shops import views as views_shops


# 4. Views описываем отдельно, в каждом приложении своя
