import asyncio


async def get_name():
    TARGETS = [
        ('8.8.8.8', 443),
        ('1.1.1.1', 443),
        ('8.8.4.4', 443),
        ('77.88.8.8', 443),
        ('77.88.8.88', 443),
        ('77.88.8.7', 443)
    ]

    # получаем текущий цикл событий
    loop = asyncio.get_event_loop()

    for target in TARGETS:
        # запускаем асинхронный вариант
        # функции socket.getnameinfo()
        host, port = await loop.getnameinfo(target)
        # выводим результаты
        print(f'{target[0]:15}: {host}')


if __name__ == '__main__':
    asyncio.run(get_name())