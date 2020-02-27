
logs = [
    {
        "client_id": "user15",
        "User-Agent": "Firefox 59",
        "document.location": "https://shop.com/products/?id=2",
        "document.referer": "https://yandex.ru/search/?q=купить+котика",
        "date": "2018-04-03T07:59:13.286000Z"
    },

    {
        "client_id": "user7",
        "User-Agent": "Chrome 65",
        "document.location": "https://shop.com/products/id?=25",
        "document.referer": "https://shop.com/products/id?=10",
        "date": "2018-05-23T19:04:20.119000Z"
    },

    {
        "client_id": "user7",
        "User-Agent": "Chrome 65",
        "document.location": "https://shop.com/cart",
        "document.referer": "https://shop.com/products/id?=25",
        "date": "2018-05-23T19:05:13.123000Z"
    },

    {
        "client_id": "user7",
        "User-Agent": "Chrome 65",
        "document.location": "https://shop.com/checkout",
        "document.referer": "https://shop.com/cart",
        "date": "2018-05-23T19:05:59.224000Z"
    }

]

# будем хранить клиентов перешедших по нашей ссылке в кэше
cache = {}

# лист клиентов совершивших покупку
winners = []

# программа обрабатывает каждый увиденный лог
for l in logs:
    client_id = l['client_id']
    referer = l['document.referer']
    location = l['document.location']


    # проверяем находится ли клиент в кэше
    if client_id in cache:
        # клиент в кэше
        # проверяем что наш сервис является последним реферером
        if 'ad.theirs1' not in referer:
            # проверяем дошел ли клиент до оплаты
            if 'https://shop.com/checkout' == location:
                # клиент перешел по нашей ссылке
                winners.append(client_id)

                # очищаем кэш
                del cache[client_id]
            else:
                # внутреннее перемещение по сайту
                # игнорируем
                pass
        else:
            # клиент перешел с чужого сервиса
            # стираем из кэша
            # клиент нам больше не интересен
            del cache[client_id]
    else:
        # клиента нет в кэше
        # проверяем document.referer.
        if 'referal.ours' in referer:
            # клиент перешел с нашей ссылки
            # добовляем в кэш
            cache[client_id] = 1
        else:
            # Если клиент перешел не с нашей ссылки, он нам не интересен
            pass












