# Создание подписки на рассылку на email, настройка почты и отправка рассылки
# https://www.hostinger.com.ua/rukovodstva/kak-ispolzovat-smtp-server - Как использовать бесплатный SMTP Сервер от Google

# 1. Создаем новое app - contact
# python manage.py startapp contact
#
# 2. Описываем модель для БД с двумя полями, email поьзовавателя и дата занесения в БД
# auto_now_add=True - будет заносить текущую дату
#
# from django.db import models
#
#
# class Contact(models.Model):
#     """Подписка по email"""
#     email = models.EmailField()
#     date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.email
#
# 3. Регестрируем модель в admin.py
#
# from django.contrib import admin
#
# from .models import Contact
#
#
# @admin.register(Contact)
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ("email", "date")
#
# 4. Создаем файл forms.py
# Создадим в нем форму
# в Meta указываем нужную нам модель и поля
# в widgets указываем class формы из html
#
# from django import forms
# from .models import Contact
#
#
# class ContactForm(forms.ModelForm):
#     """Форма подписки по email"""
#
#     class Meta:
#         model = Contact
#         fields = ("email",)
#         widgets = {
#             "email": forms.TextInput(attrs={"class": "editContent", "placeholder": "Your Email..."})
#         }
#         labels = {
#             "email": ''
#         }
# 5. В папке contact создадим папку(python пакет) templatetag. В этой папке создадим файл contact_tags.py
# который будет обрабатывать форму ContactForm на всех страницах сайта т.е. в footer.html
# Создадим templatetag - contact_form, который будет возвращать форму контакта return {"contact_form": ContactForm()}
# Регестрируем templatetag указав путь к шаблону формы
# @register.inclusion_tag("contact/tags/form.html")
#
# from django import template
# from contact.forms import ContactForm
#
# register = template.Library()
#
#
# @register.inclusion_tag("contact/tags/form.html")
# def contact_form():
#     return {"contact_form": ContactForm()}
#
# 6. Для этого в папке проекта templates создадим папку сontact в ней папку tags и в ней файл form.html
# Опишем файл form.html и добавим в него форму которая является значением словаря по ключу contact_form(создали
# в contact_tags.py)
#
# <h3 class="footer-title text-uppercase editContent mb-lg-4 mb-3">
#     Newsletter</h3>
#
# <p class="editContent">By subscribing to our mailing list you will always
#     get latest news and updates from us.</p>
# <form action="{% url 'contact' %}" method="post" class="w3layouts-newsletter">
#     {% csrf_token %}
#     {{ contact_form }}
#     <button class="btn1 btn"><span class="fa fa-paper-plane-o" aria-hidden="true"></span>
#     </button>
# </form>
#
# 7. Во views app contact опишем view которая позволит сохранять форму
# Создадим класс ContactView который наследуетя от класса CreateView
# Опишем нужную модель и название класса формы
# model = Contact
# form_class = ContactForm
# Далее нужно перенаправить пользователя на главную страницу после отправки формы
# success_url = "/"
#
# from django.views.generic import CreateView
#
# from .models import Contact
# from .forms import ContactForm
#
#
# class ContactView(CreateView):
#     model = Contact
#     form_class = ContactForm
#     success_url = "/"
#
# 8. В папке app contact создадим файл urls и пропишем в нем путь для отправки формы
#
# from django.urls import path
# from .views import ContactView
#
#
# urlpatterns = [
#     path("", ContactView.as_view(), name="contact")
# ]
# 9. В файле form.html в action пропишем путь к нужной url
# <form action="{% url 'contact' %}"
#
# 10.В файле settings зарегестрируем приложение contact
#
# INSTALLED_APPS = [
#     'contact'
# ]
#
# 11. В urls проекта добавим новый url
#
# path('contact/', include('contact.urls'))
#
# 12. В footer.html подключим файл contact_tags.py
#
# {% load contact_tags %}
#
# и вместе вывода формы подключим ее передав ключ словаря в котором она находится
#
# {% contact_form %}
#
# 13. Сделаем миграции
# python manage.py makemigrations
# python manage.py migrate
#
#
# 14. Дополним view ContactView
# Создадим проверку формы  на валидность, если форма валидна мы ее сохраняем
# form.save()
# и вызываем функцию send которая будет отправлять письмо пользователю с уведомлением что он подписан на рассылку.
# Функция send описана в другом файле который нужно импортировать в файл view
# from .service import send
#
# возвращаем метод form_valid
# return super().form_valid(form)
#
# def form_valid(self, form):
#     form.save()
#     send(form.instance.email)
#
#     return super().form_valid(form)
#
# 15.Напишем функцию send, для этого создаим файл service.py и в нем функцию которая принимает email пользователя и с
# помощью метода send_mail отправляет письмо пользователю
# В метод send_mail передаем текс письма который увидит пользователь, почту с которой происходит рассылка и список ящиков на
# которые нужно сделать рассылку
#
# from django.core.mail import send_mail
#
#
# def send(user_email):
#     send_mail(
#         'Вы подписались на рассылку',
#         [user_email],
#         fail_silently=False,
#     )
# 16. В settings пропишем данные для отправки писем через gmail
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'v.bakatina@gmail.com'
# EMAIL_HOST_PASSWORD = '12345'
# EMAIL_PORT = 587
# После этого необходимо поменять настройки в почте
# Настройки - Пересылать POP IMAP - включить IMAP
# Отправку необходимо делать с помощью celery