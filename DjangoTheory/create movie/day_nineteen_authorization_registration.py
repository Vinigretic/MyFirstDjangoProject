# Авторизация и регистрация

# 1. Установить расширение django-allauth
#
# pip install django-allauth
#
# 2. Дополним url проекта
# Добавим path('accounts/', include('allauth.urls')),
#
# 3. Дополним settings.py
# Проверить подключение в INSTALLED_APPS, должны быть подключены
# 'django.contrib.auth'
# 'django.contrib.sites'
# должен быть установлен SITE_ID = 1
# Добавить подключение в INSTALLED_APPS
# 'allauth',
# 'allauth.account'
#
# Прописать аутентификацию
#
# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# )
# 4. Сделать миграции
# python manage.py migrate
#
# allauth - добавит две таблицы для пользователей
#
# 5. Скопировать папку account в templates проекта
# Данная регистрация не возможна через соц сети так как расширение socialaccount закоментировано в файле
# login.html, подключение через соц сети нужно делать отдельно
#
# 6. Для того что бы после входа в акаунт пользователь перекидывало на главную страницу дополним settings.py
# LOGIN_REDIRECT_URL = "/"
#
# 7. Опишем кнопку входа и выхода в акаунт
# Отредактируем файл header.html
# {% if user.is_authenticated %}
#     <span>{{ user.username }}</span>
#     <a href="{% url 'account_logout' %}"
#        style="color: rgb(255, 255, 255); font-weight: 700; text-transform: uppercase;">
#         Выход
#     </a>
# {% else %}
#     <a href="{% url 'account_login' %}"
#        style="color: rgb(255, 255, 255); font-weight: 700; text-transform: uppercase;">
#         Вход
#     </a>
#      <a href="{% url 'account_signup' %}"
#        style="color: rgb(255, 255, 255); font-weight: 700; text-transform: uppercase;">
#         Регистрация
#     </a>
# {% endif %}
# Этот код будет отображать следующее
# если пользователь зарегестрирован и вошел в акаунт будет отображаться его логин и кнопка выхода
# в противном случае будет отображаться кнопка входа и регистрации
#
# 8. Регистрация нового пользователя
# Для регистрации нового пользователя необходимо иметь подтверждение от него по email(пока не работает, как
# это сделать есть в описании)
# Реализуем отправку email на back ende(отправка email будет крутиться в консоли и подтверждаться автоматически)
# Для этого дополним файл settings.py
#
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1 (кол-во дней до подтверждения email)
# ACCOUNT_USERNAME_MIN_LENGTH = 4 (мин длинна логина)
#
#
# EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend' установка отправки email на сервере
# для тожо что бы отправка была на email вместо dummy указываем smtp
#
#
# ВХОД ЧЕРЕЗ СОЦ СЕТЬ (Фасбук)
#
# 1. В файл settings.py добавить
# INSTALLED_APPS -
# 'allauth.socialaccount',
# 'allauth.socialaccount.providers.facebook',
#
# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# )
#
# ACCOUNT_EMAIL_REQUIRED=True
# ACCOUNT_USERNAME_REQURIED=True
#
# SOCIALACCOUNT_PROVIDERS = \
#     {'facebook':
#        {'METHOD': 'oauth2',
#         'SCOPE': ['email','public_profile', 'user_friends'],
#         'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
#         'FIELDS': [
#             'id',
#             'email',
#             'name',
#             'first_name',
#             'last_name',
#             'verified',
#             'locale',
#             'timezone',
#             'link',
#             'gender',
#             'updated_time'],
#         'EXCHANGE_TOKEN': True,
#         'LOCALE_FUNC': lambda request: 'kr_KR',
#         'VERIFIED_EMAIL': False,
#         'VERSION': 'v2.4'}}
#
# Добавить переход пользователя на главнуюстарницу после регистрации
#
# LOGIN_REDIRECT_URL = "/"
#
# 2. Перейти на https://developers.facebook.com/ создать приложения для входа
# получить ключи
#
# 3. Добавить в основную urls проекта путь
# path('accounts/', include('allauth.urls')),
#
# 4. Сделать миграции
# python manage.py migrate
#
# 5.Зарегистрировать идентификатор нашего сайта и социальное приложение в нашей админке django.
# Во вкладке site внести ключи и измените example.com на http://localhost:8000
#
# 6.Добавить кнопку регистрации в файл login.html(несколько примеров кода)
#
# <a href="{% provider_login_url "facebook" method="js_sdk" %}">Изображение кнопки входа</a>
# или
# <a href="{% provider_login_url "facebook" method="js_sdk" %}" class="btn btn-block btn-social btn-facebook" style="background-color:#3b5998;text-align:center">
#   <span class="fa fa-facebook"></span>
#                Войдите через Facebook
# </a>