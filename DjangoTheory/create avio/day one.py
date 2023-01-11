# Создаем модель Aircrafts
#
# Для того что бы название нашей таблицы в бд соответствовало названию тз, переопределяем ее название в классе Мета
# в параметре db_table. Передаем в него название которое должно быть в бд
#
#
# class Aircrafts(models.Model):
#     aircraft_code = models.CharField(max_length=3)
#     model = models.TextField()
#     range = models.IntegerField()
#
#
#     class Meta:
#         db_table = 'aircrafts'

# Создаем модель BoardingPasses
# Посадочным талонам присваиваются последовательные номера (boarding_no) в порядке регистрации пассажиров на рейс
# (этот номер будет уникальным только в пределах данного рейса). В посадочном талоне указывается номер места (seat_no).
# Для того что бы обеспечить эту уникальность используем параметр unique_together

# Уникальная комбинация полей, используемая для установки:
#
# unique_together = (("driver", "restaurant"),)
# Это кортеж кортежей, которые должны быть уникальными при объединении. Он используется в бэкэнде Django для ограничения данных
# на уровне базы данных (например, оператор UNIQUE включен в оператор CREATE TABLE).
#
# Для удобства при работе с набором отдельных полей unique_together может быть одномерным кортежем:
#
# unique_together = ("driver", "restaurant")
# ManyToManyField нельзя включить в unique_together. (Что это означает, не ясно!) Если вам нужно проверить уникальность
# ассоциаций ManyToManyField, попробуйте использовать сигналы или явные через модели.
#
# При нарушении ограничения unique_toght во время проверки модели будет выдано исключение ValidationError.


# class BoardingPasses(models.Model):
#     ticket_no = models.CharField(max_length=13)
#     flight_id = models.IntegerField()
#     boarding_no = models.IntegerField()
#     seat_no = models.CharField(max_length=4)
#
#     class Meta:
#         db_table = 'boardingpasses'
#         unique_together = (('ticket_no', 'flight_id'), ('flight_id', 'boarding_no'), ('flight_id', 'seat_no'))


# oписать классы generic