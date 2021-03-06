# отследить разницу между логин и регистрация, логаут, авторизация, аутентификация

# Идентификация — процесс распознавания пользователя по его идентификатору.
# логин - это инструмент с помощью которого происходит идентификация пользователя

# Аутентификация — процедура проверки подлинности, доказательство что пользователь именно тот, за кого себя выдает.
# пароль - это инструмент с помощью которого происходит аутентификация пользователя.
# Это может быть не только пароль, а любая информация присущая или известная только конкретному пользователю
# (сканеры лица, отпечатки пальцев или сетчатки глаза, pin-коды, пароли, графические ключи, секретные слова)

# Авторизация — предоставление определённых прав.
# Если все верно, и пара логин-пароль верны, то система предоставит пользователю доступ к его ресурсам,
# то есть произойдет авторизация.

# Многофакторная аутентификация
# Многофакторная аутентификация представляет собой метод, при котором пользователю для доступа к учетной
# записи или подтверждения операции с денежными средствами необходимо двумя различными факторами доказать,
# что именно он владелец учетной записи или что именно он осуществляет вход.
# Метод, при котором пользователю для получения доступа необходимо предоставить два разных типа аутентификационных
# данных, например, что-то известное только пользователю (пароль) и что-то присущее только пользователю
# (отпечаток пальца).

# Однофакторная двухэтапная аутентификация
# Происходит следующим образом:
# Пользователь вводит логин и пароль, указанные при регистрации. Если данная пара корректна
# (логин есть в базе и соответствует паролю) система высылает одноразовый пароль, имеющий ограниченное
# время действия.
# Пользователь вводит одноразовый пароль и, если он совпадает с тем, что отправила система, то пользователь
# получает доступ к своей учетной записи, денежным средствам или подтверждает денежный перевод.

# Регистрация
# Регистрация — это способ сообщить ресурсу данные о себе и в обмен получить доступ к дополнительным возможностям
# (например, добавление чего-либо в избранное) или ресурсам (к примеру, файлам) на сайте, которые недоступны гостям.
# Регистрация неразделима без авторизации

# Логаут это:
# прекращение сеанса работы в качестве зарегистрированного пользователя