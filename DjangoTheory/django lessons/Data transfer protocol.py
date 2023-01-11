# Протокол сети - это набор правил, который позволяет обмен данными между устройствами, это основа для обеспечения
# доставки пакета, определенные действия для реализации конкретного процесса.
#
# MAC (Media Access Control)
# Протокол MAC - это протокол низкого уровня, уникальный идентификатор устройства. Его применяют в качестве идентификации
# устройств в локальной сети. Каждое устройство, которое подключено к Интернету имеет свой уникальный MAC адрес. Этот адрес
# задан производителем. Это протокол уровня соединения, с которым довольно часто приходится сталкиваться каждому пользователю.
# Это физический адрес  оборудования или интерфейса некоторых сетей.
# Данный адрес выдается бесплатно на каждое устройство. Основная часть сетевых протоколов используют одно из 3-х пространств
# MAC, под управлением IEEE: MAC-48, EUI-48, EUI-64. Пример написания МАС адреса: 00-50-B6-5B-CA-6A. Первые 6 знаков обозначают
# производителя, а вторая часть адреса - это серийный номер интерфейса.
# Зачем нужен МАС адрес? Данный протокол используется для идентификации узла сети и соответственно доставки информации именно в
# этот узел.
#
# IP (Internet Protocol)
# IP (Internet Protocol) - по сравнению с MAC, располагается на уровень выше. IP адреса  уникальны для каждого устройства и дают
# возможность компьютерам находить и определять друг друга в сети. IP принадлежит сетевому уровню модели TCP/IP, стандартный
# протокол сети интернет.
# Сети связываются в сложные структуры, а с помощью данного протокола машины определяют возможные пути к целевому устройству
# (эти пути могут меняться во время работы). Протокол реализуется с помощью известных видов IPv4 и IPv6,
# IP адрес может быть как динамическим (временным), так и статическим, который прикрепляется на компьютер при подключении
# к интернету. Например, на VPS вы получите статический IP адрес, а при использовании некоторых VPN  - динамический IP адрес.
#
# Понятие IP адреса (выделенного адреса) очень часто используется в сфере хостинга и аренды серверов, ведь у каждого сервера
# есть свой уникальный выделенный IP адрес или даже своя подсеть адресов.

# ICMP (Internet control message protocol)
# Этот протокол соединения предназначен для того, чтобы устройства могли обмениваться сообщениями. Это к примеру могут
# быть сообщения об ошибках или информационные оповещения. Данные этот протокол не передает информацию. Этот протокол находится
# уровнем выше нежели протокол IP.
#
# TCP (Transmission control protocol)
# Один из основных протоколов сети internet, который находится на одном уровне с предыдущим протоколом ICMP. Он управляет
# передачей данных.
# Бывают ситуации, когда пакеты могут приходить не в том порядке или вообще где-то теряться. Но протокол TCP обеспечивает
# правильный порядок доставки и дает возможность исправить ошибки передачи пакетов. Информация подается в правильном порядке
# для приложения. Соединение осуществляется с помощью специального алгоритма, который предусматривает отправку запроса и
# подтверждение открытия соединения двумя компьютерами. Минус работы данного протокола - низкая скорость, так как для надежной
# передачи данных необходимо больше времени.
# Роль TCP протокола (web протокола): обеспечение надежной доставки сегментов и их упорядочивание, контроль скорости передачи
# данных, работа с сессиями.
#
# UDP (user datagram protocol)
# UDP - известный протокол, чем-то похожий с TCP, который также функционирует на транспортном уровне. Основное отличие -
# ненадежная передача данных: данные не проходят проверку при получении. В некоторых случаях этого вполне достаточно.
# Протокол udp принцип работы: за счет отправки меньшего количества пакетов, UDP работает шустрее чем TCP. Нет необходимости
# устанавливать соединение, и протокол используется для отправки пакетов сразу на несколько устройств или IP телефонии.
# Это более упрощенный протокол за счет того, что некоторые фрагменты при передаче могут быть утеряны.
#
# HTTP (hypertext transfer protocol)
# Протокол приложения HTTP (hypertext transfer protocol)  лежит в основе работы всех сайтов в Сети. HTTP дает возможность
# запрашивать необходимые ресурсы у удаленной системы, например, веб страницы и файлы. HTTPS - это не отдельный протокол сети,
# а тот же HTTP, но со специальной настройкой шифрования.
# HTTPS обеспечивается наличием сертификата защиты SSL, который подключается на стороне хостинг-провайдера.
#
# FTP (file transfer protocol)
# FTP (file transfer protocol) - используется для передачи данных. Функционирует на уровне приложений, чем обеспечивается передача
# файла от одного компьютера к другому. FTP по праву считается небезопасным, его не стоит применять для передачи личных данных.
# Поэтому если есть такая возможность, то лучше вместо FTP использовать SSH протокол как основной тип протоколов передачи данных.
# Для соединения по FTP используются специальные программы, например, Far Manager, Total Commander, FileZilla. Несмотря на свою
# небезопасность ФТП протокол все равно является наиболее популярным среди вебмастеров. На услугах виртуального хостинга ФТП
# предоставляется по умолчанию для соединения с серверов и передачи данных.
# FTP - один из самых старых прикладных протоколов, который используется для доступа к удаленным хостам. Именно благодаря ФТП
# происходит организация обмена файлами.
#
# DNS (domain name system)
# DNS (domain name system) - используется для преобразования понятных и легко читаемых адресов в сложные ip адреса, которые трудно
# запомнить и наоборот. С помощью DNS мы получаем доступ к интернет-ресурсу по его доменному имени.
# Понятие DNS часто можно встретить при работе с доменом. Например,  при смене хостинга или регистратора домена происходит процесс
# обновления DNS зоны, который может длиться от 2 до 72 часов.
# DNS сервер имеет несколько типов записей:
# ✓CNAME - часто используется для привязки субдомена, указывает альтернативный вариант основному домену,
# ✓NS - адрес DNS-сервера (например, dns1.hyperhost.ua),
# ✓А запись - IP-адрес сайта,
# ✓MX запись -  адрес почтового сервера,
# ✓TXT запись - текстовая информация о домене, часто добавляется для прохождения различного рода верификаций домена,
# ✓SPF - список серверов, которые могут отправлять почту от конкретного домена;
# ✓SOA - запись с информацией о сервере.
#
# SSH (secure shell)
# SSH (secure shell) также относится к протоколу уровня приложений. Он разработан для  обеспечения удаленного управления системой
# по защищенному каналу. Этот протокол используется для работы многих дополнительных технологий. SSH - прежде всего безопасный
# протокол передачи данных, поэтому если есть возможность использовать именно его, то не стоит пользоваться другими протоколами
# такими как ФТП.
# В основном ССШ используют для удаленной работы с серверами, а также для надежного переноса большого количества данных. Например,
# при смене хостинг-провайдера и переносе сайта от одного хостера к другому, для быстрой организации процесса вам понадобится
# именно SSH доступ к старому хостингу.
# SSH работает с помощью специальных команд, которые запускаются с командной строки. Это команды могут немного отличатся в
# зависимости от использованной ОС, а также SSH клиента.
#
# POP3 (Post Office Protocol)
# POP3 (Post Office Protocol) - стандартный протокол, который используется для приема сообщений электронной почты. Протокол
# почтового соединения предназначен для обработки запросов на получение почты от клиентских почтовых программ.
# POP3 предназначен для получения почты из любой точки доступа в интернете. POP3 - самый популярный  тип учетной записи
# электронной почты. POP3 позволяет скачивать письма на  устройства, а затем удалять их с сервера.
# Минусы использования POP3: письма на сервере не хранятся, в том числе отправленные. Посмотреть отправленные можно только с
# устройства, с которого пользователь отправил письмо. Все настройки по хранению писем настраиваются отдельно в почтовом клиенте
# пользователя.
#
# SMTP (Simple Mail Transfer Protocol)
# SMTP (Simple Mail Transfer Protocol) - протокол  для передачи почты. Основная задача сервера SMTP: возвращение или подтверждение
# о приеме, или оповещение об ошибке, или запрос на дополнительные данные. С помощью SMTP протокола проверяется корректность
# системы, в которой отправляется исходящее сообщение. За данным протоколом закреплено два порта: 25 и 587. Второй вариант
# протокола с защищенным SSL, хотя 25 на практике используется намного чаще.