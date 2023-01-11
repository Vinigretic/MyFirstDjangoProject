# Создание API для POST
# В blog/api/models.py создаем модель Post, которая наследуется от класса Model из Django и определим ее поля:

# from django.db import models - импортируем класс моделс

# Создаем модель для БД
#
# class Post(models.Model): # создаем класс который наследует класс Model

# created = models.DateTimeField(auto_now_add=True) - создаем поле которое будет автоматически генерировать
# дату создания поста
# Для работы со временем в моделях Django есть несколько полей. Одно из применений таких полей - это создание меток
# (timestamp), которые указывают либо на дату созданию строки в базе либо на дату ее изменения.
#
# В Django предусмотрено два параметра, которые могут сделать это:
#
# auto_now- обновляет метку каждый раз при изменении (сохранении) строки в базе;
# auto_now_add- создает метку при создании строки в базе.
# Эти параметры можно указать в двух полях, которые указываются при создании модели:
#
# DateField - хранит только дату;
# DateTimeField - хранит дату и время;

# body = models.TextField(default='') - создаем поле которое отвечает за создание текста блога
# аргумент default - устанавливает значение по умолчанию для поля. Это может быть значение или вызываемый объект,
# и в этом случае объект будет вызываться каждый раз, когда создаётся новая запись.

# title = models.CharField(max_length=100, blank=True, default='') - создаем поле которое отвечает за создание
# заголовка
# аргуенты:
# max_length - устанавливает максимальную длину заголовка
# blank = Если True, поле может быть пустым. По умолчанию установлено значение False.
# Обратите внимание, что это отличается от null. null связана исключительно с базой данных, тогда как blank
# связана с проверкой. Если поле имеет blank=True, проверка формы позволит ввести пустое значение. Если поле
# имеет blank=False, поле будет обязательным для заполнения
# Его часто используют с null = True, потому что если нужно разрешить пустые значения, нужно, чтобы база данных
# могла представлять их соответствующим образом.

# Общих аргументов поля существует достаточно много и они могут использоваться при объявлении многих / разных типов
# полей их можно посмотреть сдесь - https://django.fun/docs/django/ru/4.0/ref/models/fields/

# owner = models.ForeignKey('auth.user', related_name='posts', on_delete=models.CASCADE) - создаем внешний ключ
# который будет связывать модель Post и User связью один ко многим
# аргументы:
# 'auth.user' - передаем название модели с которой создаем связь. С помощью auth идет обращение к встроенным моделям
# related_name='posts' - этот атрибут указывает имя обратного отношения от модели User к модели Post(в эту переменную
# будет попадать id модели Post, в БД эти данные не попадают, они отображаются только в endpointe)
# Если вы не укажете related_name, Django автоматически создает имя, используя имя вашей модели с
# суффиксом _set, например post_set. Далее это имя мы передаем сериалайзер модели User
# on_delete - обязательный аргумент см прошлый день

# class Meta: - Обьявляем  метаданные на уровне модели для модели Post, объявив класс Meta

# Одной из наиболее полезных функций этих метаданных является управление сортировкой записей, возвращаемых при
# запросе типа модели. Создание этого класса не является обязательным(все зависит от поставленных задач)

# ordering = принимает кортеж или список строк и/или выражений запроса

# Каждая строка переданная в ordering представляет собой имя поля с необязательным префиксом «-»,
# который указывает сортировку в порядке убывания. Поля без начального «-» будут упорядочены по возрастанию.
# Используйте знак «?» для случайной сортировки.

# ordering = ['created'] - передаем поле 'created' которое будет отсортировано по возрастанию

# class Post(models.Model): # создаем класс который наследует класс Model
#     created = models.DateTimeField(auto_now_add=True) -
#     body = models.TextField(default='')
#     title = models.CharField(max_length=100, blank=True, default='')
#     owner = models.ForeignKey('auth.user', related_name='posts', on_delete=models.CASCADE)
#
#
#     class Meta:
#         ordering = ['created']

# Так как мы работаем с моделями Django, таким как User, посты можно изменить из административной панели Django,
# зарегистрировав ее в blog/api/admin.py:

# from django.contrib import admin
# from .models import Post - # импортируем нужную модель
#
#
# admin.site.register(Post) - # подключаем модель


# Описываем сериализатор

# from rest_framework import serializers
# from django.contrib.auth.models import User
# дополнительно импортируем модель Post
# from .models import Post


# class PostSerializer(serializers.ModelSerializer): - создаем новый класс

# owner - поле внешний ключ, вызываем для него класс ReadOnlyField
# ReadOnlyField — Класс поля, который просто возвращает значение поля без модификации.
# атрибут source - имя атрибута, который будет использоваться для заполнения поля
# source='owner.username' -  В этом случае он используется для возвращения
# поля username вместо стандартного id.

# Эта строчка кода применяется для получения nick name - user вместо id, если этот код не прописывать будет просто
# передаваться id user
# owner = serializers.ReadOnlyField(source='owner.username') - выведет нам вместо id - username

# class PostSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#
#     class Meta:
#         model = Post
#         fields = ['id', 'title', 'body', 'owner']

# Далее нам нужно отредактировать сериализатор UserSerializer

# Передадим в него аргумент posts
# который был определен в модели Post во внешнем ключе owner, в аргументе related_name
# далее говорим сериализатору UserSerializer, что переменная posts равна первичному ключу модели Post
# аргумент many=True - указывает что постов может быть много
# аргумент read_only=True(аргумент поумолчанию) - указываем что список статей нельзя отредактировать в ручную,
# если его не задать  поле posts будет иметь права записи по умолчанию.

# posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

# передадим переменную posts в обработку сериалайзера UserSerializer
#
# fields = ['id', 'username', 'first_name', 'last_name', 'posts']
#
# class UserSerializer(serializers.ModelSerializer):
#     posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'first_name', 'last_name', 'posts']

# Создание views для Post

# from .models import Post - импортируем нашу модель

# Создаем view которая будет выводить общий список постов, и создавать новые

# class PostList(generics.ListCreateAPIView): создаем класс PostList который наследует generics.ListCreateAPIView
# ListCreateAPIView -  это общий APIView, который позволяет выполнять запросы GET (список) и POST (создание).
# queryset (переменная по стандарту)
# queryset = Post.objects.all() - забираем набор данных из модели Post
# serializer_class (переменная по стандарту)
# serializer_class = serializers.PostSerializer - передаем serializer который обрабатывает модель Post

# Так как у нас есть две таблицы которые связаны между собой по колонке owner(внешний ключ) мы должны в эту переменную
# передавать id user который создал пост. Для этого  создаем доп функцию которая будет это осуществлять
# Функция должна принимать вторым аргументом serializer. Далее с помощью метода save сохраняем во внешний ключ(owner)
# нужный id.
#
# def perform_create(self, serializer):
#     serializer.save(owner=self.request.user)

# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = serializers.PostSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

# Создаем view которая будет выводить посты по одному, с возможностью редактирования и удаления
# class PostDetail(generics.RetrieveUpdateDestroyAPIView)- создаем класс PostDetail который наследует generics.RetrieveUpdateDestroyAPIView
# RetrieveUpdateDestroyAPIView - используется для конечных точек чтение-запись-удаление для представления
# одного экземпляра модели.
# Предоставляет обработчики методов get , put , patch и delete.

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = serializers.PostSerializer