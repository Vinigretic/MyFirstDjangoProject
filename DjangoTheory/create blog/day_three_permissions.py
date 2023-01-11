# Разрешения
#
# Для того что бы можно было заходить под разными аккаунтом добавим кнопку «Log in»
# Это так же позволит нам проверять работу разрешений и изменять посты через интерфейс.
#
# Добавим кнопку «Log in» в графическое представление API с помощью следующего кода в blog/urls.py:
#
# path('api-auth/', include('rest_framework.urls'))
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('api.urls')),
#     path('api-auth/', include('rest_framework.urls'))
# ]

# Чтобы аутентифицировать пользователя и быть уверенным в том, что только владелец поста может обновлять и удалять его,
# нужно добавить разрешения.

# Для этого в приложении api создаем файл permissions.py.

# from rest_framework import permissions - импортируем встроенные разрешения

# class CheckOwner(permissions.BasePermission) - Создаем класс разрешение CheckOwner, который наследует класс BasePermission
# Он проверяет, является ли пользователь владельцем этого объекта. Таким образом только при этом условии можно будет
# обновлять или удалять пост. Не-владельцы смогут получать информацию про посты, потому что это действие только для чтения.

# класс BasePermission - все классы разрешений, настраиваемые или встроенные, являются наследниками этого класса
# Мы можем создать свой собственный класс или использовать один из семи встроенных классов.

# Встроенные классы разрешений DRF - прописываются только во views
# AllowAny - Класс разрешений AllowAny разрешит неограниченный доступ независимо от того, был ли запрос аутентифицирован или
# не аутентифицирован
#
# IsAuthenticated - Класс разрешений IsAuthenticated откажет в разрешении любому неаутентифицированному пользователю и
# разрешит разрешение в противном случае.
#
# IsAdminUser - Класс разрешений IsAdminUser будет отказывать в разрешении любому пользователю, если только user.is_staff
# не равен True, и в этом случае разрешение будет разрешено.
#
# IsAuthenticatedOrReadOnly - позволит аутентифицированным пользователям выполнять любой запрос. Запросы для неавторизованных
# пользователей будут разрешены только в том случае, если метод запроса является одним из «безопасных» методов: GET, HEAD или OPTIONS.
#
# DjangoModelPermissions - Этот класс разрешений связан со стандартным Django django.contrib.auth разрешения модели. Это разрешение
# должно применяться только к представлениям, у которых установлено свойство .queryset. Авторизация будет предоставлена
# олько в том случае, если пользователь аутентифицирован и ему назначены соответствующие разрешения модели.
#
# Запросы POST требуют, чтобы у пользователя было право add на модель.
# Запросы PUT и PATCH требуют, чтобы у пользователя было право change модели.
# Запросы DELETE требуют, чтобы у пользователя было право delete модели.
#
# DjangoModelPermissionsOrAnonReadOnly - Подобно DjangoModelPermissions, но также позволяет неаутентифицированным
# пользователям иметь доступ только для чтения к API.
#
# DjangoObjectPermissions - Этот класс разрешений связан со стандартной структурой разрешений объектов Django, которая разрешает
# разрешения для каждого объекта в моделях. Чтобы использовать этот класс разрешений, вам также необходимо добавить серверную часть
# разрешений, которая поддерживает разрешения на уровне объектов, например django-guardian.
# Как и в случае DjangoModelPermissions, это разрешение должно применяться только к представлениям, имеющим свойство .queryset
# или метод .get_queryset(). Авторизация будет предоставлена только в том случае, если пользователь аутентифицирован и имеет
# соответствующие разрешения для каждого объекта и соответствующие разрешения модели.
# Запросы POST требуют, чтобы у пользователя было право add на объект модели.
# Запросы PUT и PATCH требуют, чтобы у пользователя было право change на объект модели.
# Запросы DELETE требуют, чтобы у пользователя было право delete на объект модели


# BasePermission имеет два метода, has_permission(self, request, view) и has_object_permission(self, request, view, obj),
# (параметры по умолчанию) оба из которых возвращают True по умолчанию. Методы должны возвращать True, если запросу должен
# быть предоставлен доступ, и False в противном случае.

# has_permission
#
# has_permission используется, чтобы решить, разрешен ли запрос и имеет ли пользователь доступ к определенному представлению
#
# Например:
#
# Разрешен ли метод запроса?
# Пользователь аутентифицирован?
# Пользователь — администратор или суперпользователь?
#
# has_permission обладает информацией о запросе, но не об объекте запроса.
#
# has_permission (вызываемый check_permissions) выполняется до выполнения обработчика представления (view), без явного его вызова.
#
# has_object_permission
#
# has_object_permission используется, чтобы решить, разрешено ли конкретному пользователю взаимодействовать с определенным объектом.
#
# Например:
#
# Кто создал объект?
# Когда это было создано?
# К какой группе принадлежит объект?
# Помимо информации о запросе, has_object_permission также обладает данными об объекте запроса. Метод выполняется после
# получения объекта из базы данных.
# has_object_permission никогда не выполняется для представлений списка (list views)что за список???????
# (независимо от того, из какого представления вы расширяетесь) или когда используется метод запроса — POST
# (поскольку объект еще не существует).
# Когда любое разрешение в has_permission возвращает False, has_object_permission не проверяется. Запрос немедленно отклоняется.

# has_permission против has_object_permission

# В представления списков (List views), выполняется только has_permission, и запрос либо предоставляется, либо отклоняется.
# Если в доступе отказано, объекты никогда не будут извлечены.
# В подробных представлениях (Detail views), has_permission выполняется только если разрешение предоставлено,
# has_object_permission выполняется после получения объекта. НУЖНЫ ОБЬЯСНЕНИЯ?????

# Если вам нужно проверить, является ли запрос операцией чтения или записи, вы должны проверить метод запроса на
# соответствие константе SAFE_METHODS, которая представляет собой кортеж, содержащий 'GET', 'OPTIONS' и 'HEAD'.
# Например:
# if request.method in permissions.SAFE_METHODS:
#     # Проверить разрешения для запроса только на чтение
# else:
#     # Проверить разрешения для запросов на запись
# https://ilyachch.gitbook.io/django-rest-framework-russian-documentation/overview/navigaciya-po-api/permissions
# https://webdevblog.ru/razresheniya-v-django-rest-framework/

# def has_object_permission(self, request, view, obj) создаем метод который применяется для каждого обьекта
# if request.method in permissions.SAFE_METHODS - если запрос для чтения предоставляем доступ
#     return True
# return obj.owner == request.user (возвращает True или Falce)

# from rest_framework import permissions
#
#
# class CheckOwner(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.owner == request.user


# Описываем views(корректируем ранее созданные добавляем разрешение)

# from .permissions import CheckOwner импортируем класс разрешение

# Представлению PostList требуется разрешение IsAuthenticatedOrReadOnly, потому что пользователь должен аутентифицироваться,
# чтобы создать пост, а вот просматривать список может любой пользователь.
# Создаем переменную permission_classes(применяется по умолчанию)
# передаем ей список необходимых классов
# permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = serializers.PostSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

# Для PostDetails нужны оба разрешения, поскольку обновлять или удалять пост должен только залогиненный пользователь,
# а также его владелец. Для получения информации о постах прав не нужно.
#
# permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckOwner]
#
#
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = serializers.PostSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckOwner]
