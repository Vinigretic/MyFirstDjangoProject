from django.contrib import admin
from django.urls import path
from firstapp import views as views_firstapp # импорт из приложения
from shops import views as views_shops
from cars import views as views_cars


from django.views.generic import TemplateView

# urlpatterns = [
#     path('', views.index, name='home'),
#     path('admin/', admin.site.urls),
#     path('about/', views.about),
#     path('users/', views.users),
#     path('contacts/', views.contacts),
#     path('login/', views.login),
#     path('registred/', views.registred),
# ]

# urlpatterns = [
#     path('products/', views.products),
#     path('products/<int:product_id>/', views.products),
#     path('users/', views.users),
#     path('users/<int:id>/<name>/', views.users),
#     path('contacts/', views.contacts),
#     path('contacts/<int:id>/<name>/<phone_number>/', views.contacts),
#     path('admin/', admin.site.urls),
# ]

# urlpatterns = [
#     path('products/<int:product_id>/', views.products),
#     path('users/', views.users)
# ]

# urlpatterns = [
#     path('orders/<int:price>/', views.orders),
#     path('admin/', admin.site.urls)
# ]

# urlpatterns = [
#     path('', views.index),
#     path('about/', views.about),
#     path('contact/', views.contact),
#     path('details/', views.details)
# ]

# urlpatterns = [
#     path('', views_firstapp.index),
#     path('home/', views_firstapp.home),
#     path('about/', views_firstapp.about),
#     path('shops/user/', views_shops.user),
#     path('shops/contacts/', views_shops.contacts),
#     path('shops/products/', views_shops.products),
#
#
# ]

# urlpatterns = [
#     path('', views_firstapp.index),
# ]
#
# urlpatterns = [
#     path('user/', views_shops.user)
# ]

# urlpatterns = [
#     path('', views_firstapp.index)
# ]

# urlpatterns = [
#     path('info/', TemplateView.as_view(template_name='firstapp/info.html', extra_context={'header':'header info'}))
# ]

# urlpatterns = [
#     path('', TemplateView.as_view(template_name='index.html'))
# ]

# urlpatterns = [
#     path('', TemplateView.as_view(template_name='firstapp/about.html'))
# ]

# urlpatterns = [
#     path('user/about', TemplateView.as_view(template_name='user/about_user.html')),
#     path('user/refactor', TemplateView.as_view(template_name='user/refactor_user.html')),
#     path('user/delete', TemplateView.as_view(template_name='user/delete_user.html'))
# ]

# urlpatterns = [
#     path('', views_firstapp.index)
# ]

# urlpatterns = [
#     path('', TemplateView.as_view(template_name='index.html'))
# ]

# urlpatterns = [
#     path('', views_firstapp.index)
# ]

urlpatterns = [
    path('', views_cars.account),
    path('about/', views_cars.about),
    path('model/', views_cars.models),
    path('admin/', admin.site.urls)
]