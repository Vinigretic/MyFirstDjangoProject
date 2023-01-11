# Создание модели Categories
#
# У каждого поста должна быть тема к которой он относиться
# 1. Создадим модель Categories со связями один ко многим с моделями User и Post
#
# class Categories(models.Model):
#     category_title = models.CharField(max_length=250)
#     owner = models.ForeignKey('auth.User', related_name='category', on_delete=models.CASCADE)
#     post = models.ForeignKey('Post', related_name='category', on_delete=models.CASCADE)

# 2. Опишем связи в сериалайзере
#
# from .models import Post, Comments, Categories импортируем модель Categories

# Связываем нашу модель Categories с UserSerializer
#
# category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#
# Передаем эту переменную в обработку полей сериалайзера
#
# fields = ['id', 'username', 'first_name', 'last_name', 'posts', 'comments', 'category']

# class UserSerializer(serializers.ModelSerializer):
#     posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'first_name', 'last_name', 'posts', 'comments', 'category']


# Связываем нашу модель Categories с PostSerializer

# class PostSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#     comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#
#
#     class Meta:
#         model = Post
#         fields = ['id', 'title', 'body', 'owner', 'comments', 'category']


# 3. Описываем views

# from .models import Post, Comments, Categories - импортируем модель Categories

# 1. Первая - выводит общий список тем пользователю и возможность выбора новой темы для поста зарегестрированным
# пользователям. У остальных разрешение только для чтения

# permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class CategoriesList(generics.ListCreateAPIView):
#     queryset = Categories.objects.all()
#     serializer_class = serializers.CategoriesSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

# 2. Вторая - дает доступ к каждому обьекту

# Даем разрешение на корректировку постов только зарегестрированным пользователям, остальным только для чтения
# Для этого передаем в permission_classes класс CheckOwner который описывает разрешение и создавался для endpoint Post

# class CategoriesDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Categories.objects.all()
#     serializer_class = serializers.CategoriesSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckOwner]


# 4. Описываем url для Categories

# urlpatterns = [
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
#     path('posts/', views.PostList.as_view()),
#     path('posts/<int:pk>/', views.PostDetail.as_view()),
#     path('comments/', views.CommentsList.as_view()),
#     path('comments/<int:pk>/', views.CommentsDetail.as_view()),
#     path('categories/', views.CategoriesList.as_view()),
#     path('categories/<int:pk>/', views.CategoriesDetail.as_view()),
# ]

# 5. Подключение Postgresql

# pip install psycopg2 - устанавливаем в виртуальное окружение
# В pgadmin создаем бд
# прописываем в settings
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'test-postgres',
#         'USER': 'postgres',
#         'PASSWORD': '1234',
#         'HOST': '127.0.0.1',
#         'PORT': '5432'
#     }
# }
#
# делаем миграции