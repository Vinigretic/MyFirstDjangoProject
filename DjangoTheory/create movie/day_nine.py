# Вывод информации о режисере или актере
# Создадим html файл который будет выводить информацию об актерах и режисерах - actor.html
# Опишем view которая будет обрабатывать этот файл
#
# class ActorView(DetailView): # создали класс который наследуется от DetailView
#     model = ActorsDirectors  # определяем модель которая будет обрабатываться
#     template_name = 'movies/actor.html' # указываем путь к файлу который будет обрабатываться
#     slug_field = 'name'  # указываем поле по которому будет осуществляться поиск в модели ActorsDirectors это поле name

# Опишем url

# path('actor/<str:slug>/', views.ActorView.as_view(), name='actor_detail')

# Добавим в модель ActorsDirectors, метод get_absolute_url. Этот метод вернет нам работу метода reverse, в который мы передаем
# нужный html файл, в нашем случае это actor_detail и в kwargs передаем словарь в котором указываем какое поле будет url
# Далее эту информацию передаем в actor_detail.html
#
# def get_absolute_url(self):
#     return reverse('actor_detail', kwargs={"slug": self.name})
