# ajax фильтр в django + hogan.js
# Как отослать ajax запрос
#
# В папке static создадим папку js и в ней файл scripts.js. Далее необходимо подключить этот файл в base.html проекта
# <script src="{% static 'js/scripts.js' %}"></script>
#
# Далее необходимо подключить шаблонизатор на js, в данном случае это будет библиотека hogan
# <script srs="http://twitter.github.com/hogan.js.builds/3.0.1/hogan-3.0.1.js"></script>
#
# Можно подключить любой другой шаблонизатор или использовать фреймворк Vue.js

# Далее в sitebar в форме меняем url для того что бы получать json от сервера и с помощью него построить страницу
# и присваеваем еще один атрибут name
#
# <form action="{% url 'json_filter' %}" method="get" name="filter">

# Напишем файл scrips

# С помощью document.querySelector находим имя нужной нам формы form[name=filter]
#
# const forms = document.querySelector('form[name=filter]');
# Когда у этой формы будет вызван метод submit запускается функция которая принимает аргумент-событие(Event) function (e),
# далее необходимо убрать дефолтное значение при отправке формы т.е при нажатии на submit форма должна отправится и страница
# должна перезагрузится, нужно это действие заблокировать
# e.preventDefault();
# в переменную url заносим информацию из нужной формы, и получаем нужный url из формы
# this - указывает на форму,  action - атрибут этой формы
# let url = this.action;
# С помощью параметра URLSearchParams выстраиваем параметры(в этом случае это жанры, года) которые нужно передать в url
# с помощью FormData передаем форму с помощью параметра this и преобразовываем в строку toString и передаем в URLSearchParams
# let params = new URLSearchParams(new FormData(this)).toString();
# Далее в функцию ajaxSend передаем переменные url и params
# ajaxSend(url, params);
#
# forms.addEventListener('submit', function (e :Event) {
#     // Получаем данные из формы
#     e.preventDefault();
#     let url = this.action;
#     let params = new URLSearchParams(new FormData(this)).toString();
#     ajaxSend(url, params);
# });

# Функция ajaxSend принимает параметры и отправляет запрос на сервер с помощью fetch
# Первым параметром передаем в fetch url и params
# Затем вторым параметром передаем словарь в котором указываем метод отправки и заголовки
# После этого получаем Promise
# в первом Promise response преобразуем в json
# .then(response => response.json()) Promise<any>
# во втором Promise json передаем в функцию render
# .then(json => render(json)) Promise<void>
# Если будет ошибка выводим ее в консоль
# .catch(error => console.error(error))

# function ajaxSend(url, params) {
#     // Отправляем запрос
#     fetch(input: `${url}?${params}`, init: {
#         method: 'GET',
#         headers: {
#             'Content-Type': 'application/x-www-form-urlencoded',
#         },
#     }) Promise<Response>
#         .then(response => response.json()) Promise<any>
#         .then(json => render(json)) Promise<void>
#         .catch(error => console.error(error))
# }

# Функция render принимает json
# в переменую template с помощью библиотеки Hogan компелируем html
# let template = Hogan.compile(html);
# в переменную output передаем json который пришел от сервера, вызывая метод render полученного шаблона data
# let output = template.render(data);
# С помощью document.querySelector находим div в котором выводятся блоки с фильмом
# const div = document.querySelector(selectors: '.left-ads-display>.row');
# Далее передаем в этот div с помощью innerHTML полученный результат всего html
# div.innerHTML = output;
#
# function render(data) {
#     // Рендер шаблона
#     let template = Hogan.compile(html);
#     let output = template.render(data);
#
#     const div = document.querySelector(selectors: '.left-ads-display>.row');
#     div.innerHTML = output;
# }


# html который компелируется в функции render заносим  в переменную html
# Это div из movies там где рендерится один блок фильма
# С помощью синтаксиса шаблонизатора перебирается список movies и выводятся нужные переменные
# После этого закрываем цикл
# let html = '\
# {{#movies}}\
#     <div class="col-md-4 product-men">\
#         <div class="product-shoe-info editContent text-center mt-lg-4">\
#             <div class="men-thumb-item">\
#                 <img src="media/{{ poster }}" class="img-fluid" alt="">\
#             </div>\
#             <div class="item-info-product">\
#                 <h4 class="">\
#                     <a href="/{{ url }}" class="editContent">{{ title }}</a>\
#                 </h4>\
#                 <div class="product_price">\
#                     <div class="grid-price">\
#                         <span class="money editContent">{{ slogan }}</span>\
#                     </div>\
#                 </div>\
#                 <ul class="stars">\
#                     <li><a href="#"><span class="fa fa-star" aria-hidden="true"></span></a></li>\
#                     <li><a href="#"><span class="fa fa-star" aria-hidden="true"></span></a></li>\
#                     <li><a href="#"><span class="fa fa-star-half-o" aria-hidden="true"></span></a></li>\
#                     <li><a href="#"><span class="fa fa-star-half-o" aria-hidden="true"></span></a></li>\
#                     <li><a href="#"><span class="fa fa-star-o" aria-hidden="true"></span></a></li>\
#                 </ul>\
#             </div>\
#         </div>\
#     </div>\
# {{/movies}}'

