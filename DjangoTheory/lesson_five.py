# Миграции
# Создание супер юзера

# Миграции необходимы для создания таблиц для БД

# python manage.py makemigrations - команда которая создает миграции, для каждой новой модели БД(таблица),
# делаем после создания модели

# python manage.py migrate - при создании нового проекта в django уже есть стандартыне модели, для которых
# необходимо сделать миграции

# Очередность выполнения, всегда
# 1. Создание модели
# 2. python manage.py makemigrations - создание миграции
# 3. python manage.py migrate - приминение миграции

# После этого в нашу БД попадает таблица идентичная коду модели

# Создание супер юзера

# Для создания супер юзера необходимо применить стандартные миграции
# python manage.py createsuperuser - команда которая создает супер юзера
# При разработке проекта следует использовать данные по умолчанию
# Username: admin
# Email address: admin@gmail.com
# Password: admin
# Подтверждаем валидацию

# Django ORM - втроенный модуль который работает(управляет) со всеми БД
# Если необходимо работь с другими БД(не SQL lite) их нужно будет подключать в файле Settings