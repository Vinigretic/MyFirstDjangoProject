# HTTP протоколы бывают двух видов
# HTTP незащищенный
# HTTPS защищенный(security)
# Методы HTTP запросов:
# 1.GET запрос на получение данных
# 2.POST запрос на создание данных
# 3.PUT запрос на обновление данных
# 4.DELETE запрос на удаление данных

# Request - делает запрос на сервер
# Respons - дает ответ от сервера

# Статусные коды(HTTP)
# код состояния(ответа) показывает был ли успешно выполнен HTTP запрос
# Коды сгрупированны на 5 групп:
# 1. Информационные - от 100 до 199
# 2. Успешные - от 200 до 299
# 3. Перенаправление - от 300 до 399
# 4. Клиентские ошибки - от 400 до 499
# 5. Серверные ошибки - от 500 до 599

# Если мы получаем код которого нет в списке то этот ответ кастомный(кастомный ответ это ошибка сервера,тип ошибки
# нужно смотреть в документации по работе с сервером)

# Код 100 - continue
# При таком ответе клиент может продолжать отправлять запросы на сервер или игнорировать его если запрос уже завершен

# Код 101 - switching protocol(переключение протокола)
# С помощью этого кода мы можем переходить на другие протоколы
# Результатом ответа на этот код будет переменная Upgrade: в которую мы можем поместить протокол на который
# хотим переключится

# Код 102 - processing(в обработке)
# Такой ответ показывает что сервер получил запрос и он находится в обработке

# Код 103 - early hints(ранние подсказки)
# В ответе этого кода распологаются ресурсы которые можно загрузить заранее, пока готовится основной ответ

# Код 200 - ОК(успешно)
# Запрос успешно отработал
#
# Код 201 - created(создано)
# Запрос успешно выполнен и создан ресурс

# Код 202 - accepted(принято)
# Запрос принят, но не отработан. Нет способа с помощью HTTP отправить асинхронный(выполнение процессов паралельно)
# ответ позже, который будет показывать итог обработки запроса. Предназначено для случаев когда запрос обрабатывается
# другим процессом или сервисом либо для пакетной(библиотеки) обработки

# Код 203 - Non-Authoritative Information(информация неавторитетна)
# Такой ответ означает что информация получена от сомнительного источника.

# Код 204 - not content(нет содержимого)
# Нет содержимого для ответа на запрос, но необходимые данные для работы присылаются

# Код 205 - reset content(сброс содержимого)
# Такой ответ присылается когда запрос обработан и сообщает клиенту что необходимо сбросить документ который прислал
# этот запрос(нужно разбираться с кодом документа который прислал запрос)

# Код 301 Moved Permanently(перемещен на постоянной основе)
# Код значит что url ресурса был постоянно перемещен, возможно в ответе будет указан новый ресурс

# Код 302 found(найдено)
# Этот код ответа значит что запрошенный ресурс временно изменен, новые изменения в url могут быть доступны в будущем

# Код 303 see other(просмотр других ресурсов)
# Этот код отправляет клиента в другой url c запросом GET

# Код 304 Not Modified(не модефицировано)
# Код значит что ресурс который мы запрашиваем не был изменен(страница загружается из кеш, без новых изменениий)

# Код 305 - Use Proxy, код 306 - Switch Proxy
# 305 говорит что ресурс работает через прокси, 306 говорит что прокси больше использовать нельзя

# Код 308 - permament redirect(перенаправление на постоянной основе)
# Код значит что url ресурса был постоянно перемещен, разница с 301 в том, что нужно делать однотипный запрос на новый
# url адрес(такой же как был у старой url)

# Код 400 - bad request(плохой запрос)
# Означает что сервер не понимает запрос из-за неверного синтаксиса

# Код 401 - unauthorized(не авторизовано)
# для получения запрашивоемого ответа нужна аутентификация, стату похож на статус 403 но в этом случае аутентификация возможна

# Код 402 - Payment Required(необходимая оплата)
# зарезервирован для будущего использования, был создан для использования в цифровых платежных системах(на данный момент почти
# не используется

# Код 403 - Forbidden(запрещено)
# У клиента нет права доступа к содержимому

# Код 404 - not found(не найдено)
# сервер не может найти запрашиваемый ресурс

# Код 405 - Method Not Allowed(метод не разрешен)
# сервер знает о запрашивамом методе но он был деактивирован и не может быть использован(метод Get не должен возвращать код 405)

# Код 406 - Not Acceptable(запрет по user agent)
# когда сервер не нашел контект который соответсвует user agent
# user agent - конктретный браузер, устройство

# Код 407 - Proxy Authentication Required(провалена авторизация по прокси)
# этот код аналогичен коду 401 только аутентификация требуется для прокси-сервера

# Код 409 - Conflict(конфликт)
# этот ответ появляется когда возникает конфликт с текущим состоянием сервера

# Код 410 - Gone(удалено)
# ответ возникает когда контент удален с сервера

# Код 413 - Request Entity Too Large(превышение запроса)
# Размер запроса превышает лимит заявленый сервером и сервер может закрыть свое соеденение

# Код 415 - Unsupported Media Type(не поддерживаемый медиа формат)
# медиа формат не поддерживается сервером и поэтому запрос откланяется

# Код 500 - Internal Server Error(внутренняя ошибка сервера)
# сервер столкнулся с запросом который он не знает как обработать

# Код 501 - Not Implemented(не выполнено)
# метод запроса не поддерживается серевером и не может быть обработан, метод GET никогда не возвращает этот код

# Код 502 - Bad Gateway(плохой шлюз)
# сервер во время работы в качестве шлюза для получения ответа нужного для обработки запроса получил недействительный(недоступный)
# ответ(смотреть return в случае этого кода)

# Код 503 - Service Unavailable(сервис недоступен)
# сервер не готов обрабатывать запрос, причины - перегрузка сервера, отключение

# Код 505 - HTTP Version Not Supported(HTTP версия не поддерживается)
# HTTP версия которая в запросе не поддерживается сервером