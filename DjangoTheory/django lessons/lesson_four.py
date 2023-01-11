# http://localhost/index/?id=3&name=Tom
# http://localhost/index/3/Tom/
# Параметры функции могут передаваться через url и через строку запроса

# def products(request, product_id):  # product_id - параметр переданный через url
#     category = request.GET.get('cat', '')  # category - параметр переданный через строку запроса,
                                             # GET - метод получает параметры из строки запроса
                                             # первый параметр обязательный, определяет имя переменной
                                             # к которой идет обращение
                                             # второй параметр всегда ставим по умолчанию пустую строку
#     output = f'<h2>Product number</h2> <p>id:{product_id}, category:{category}</p>'
#     return HttpResponse(output)

