# Создание endpoint для комментариев

# Для безопасности продукта в первую очередь необходимо всегда продумывать какие давать права пользователям.
# Для незарегистрированных пользователей права должны всегда быть минимальными иначе мы никак не сможем проконтролировать
# их действия. Поэтому оставлять комментарии смогут только зарегестрированные пользователи

# 1. Создаем модель. Описываем поля
# Поле created создается очень часто, так как удобно отслеживать и сортировать по дате и времени созднания обьектов
# Модель Comments имеет связи с моделью User и Post один ко многим

# Модель Comments имеет связь с моделями User и Post один ко многим.
# Для создания этой звязи в модели Comments создаем два внешних ключа, в моделях  UserSerializer  и  PostSerializer
# так же создаем связи с id модели Comments.
#
# Опишем два внешних ключа для связи с другими таблицами
# owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
# post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
#
#
# class Comments(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     body = models.TextField()
#     owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
#     post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    # class Meta:
    #     ordering = ['created']

# 2. Создаем сериалайзер. Описываем поля

# from .models import Post, Comments - импортируем модель Comments

# class CommentsSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#
#
#     class Meta:
#         model = Comments
#         fields = ['id', 'body', 'owner', 'post']

# 3. Добавляем связи в необходимые модели в сериалайзере

# from .models import Post, Comments импортируем модель Comments

# Связываем нашу модель Commends с UserSerializer
#
# comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#
# Передаем эту переменную в обработку полей сериалайзера
#
# fields = ['id', 'username', 'first_name', 'last_name', 'posts', 'comments']
#
# class UserSerializer(serializers.ModelSerializer):
#     posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#
#
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'first_name', 'last_name', 'posts', 'comments']
#
# Связываем нашу модель Commends с PostSerializer
#
# class PostSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#     comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#
#
#     class Meta:
#         model = Post
#         fields = ['id', 'title', 'body', 'owner', 'comments']


# 4. Создаем views. Описываем поля.

# from .models import Post, Comments - импортируем модель Comments
#
# 1. Первая - выводит общий список комментариев пользователю и возможность создания нового комментария зарегестрированным
# пользователям. У остальных разрешение только для чтения

# permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
# class CommentsList(generics.ListCreateAPIView):
#     queryset = Comments.objects.all()
#     serializer_class = serializers.CommentsSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

# 2. Вторая - дает доступ к каждому обьекту
#
# Даем разрешение на корректировку постов только зарегестрированным пользователям, остальным только для чтения
# Для этого передаем в permission_classes класс CheckOwner который описывает разрешение и создавался для endpoint Post
#
# permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckOwner]
# class CommentsDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comments.objects.all()
#     serializer_class = serializers.CommentsSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckOwner]


# 4. Описываем url для Comments

# urlpatterns = [
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
#     path('posts/', views.PostList.as_view()),
#     path('posts/<int:pk>/', views.PostDetail.as_view()),
#     path('comments/', views.CommentsList.as_view()),
#     path('comments/<int:pk>/', views.CommentsDetail.as_view()),
# ]

