# import asyncio
#
#
# async def msg(text):
#     # эмитируем короткую
#     # задержку в выполнении
#     await asyncio.sleep(0.1)
#     print(text)
#
#
# async def long_operation():
#     # эмитируем долгую
#     # задержку в выполнении
#     print('long_operation started')
#     await asyncio.sleep(3)
#     print('long_operation complete')
#
#
# # основной цикл программы
# async def main():
#     # легкая сопрограмма
#     await msg('1 msg complete')
#
#     # Здесь запустим `long_operation()`, но ждать, пока она
#     # выполнится не хотим, т.к. необходимо получить второе
#     # сообщение как можно раньше. Для этого создаем для нее задачу...
#     task = asyncio.create_task(long_operation())
#     # await long_operation()
#
#     # легкая сопрограмма
#     await msg('2 msg complete')
#
#     # Теперь можно дождаться завершения
#     # задачи или отменить ее
#     await task
#
#
# if __name__ == "__main__":
#     # запускаем ВСЕ на выполнение
#     asyncio.run(main())
#
# # 1 msg complete
# # long_operation started
# # 2 msg complete
# # long_operation complete

# def my_range(start=0, stop=None, step=1):
#     if stop is None:
#         stop = start
#         start = 0
#     while start < stop:
#         yield start
#         start += step
#
#
# def something():
#     # yield from my_range(10, 15)
#     yield from my_range(5)
#     # for i in my_range(5):
#     #     yield i
#
#
# print([n for n in something()])
#
# for i in range(5):
#     print(i)

import asyncio


# Позаимствовано отсюда http://curio.readthedocs.org/en/latest/tutorial.html.

async def countdown(number, n):
    while n > 0:
        print('T-minus', n, '({})'.format(number))
        await asyncio.sleep(1)
        n -= 1


loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(countdown("A", 2)),
    asyncio.ensure_future(countdown("B", 3))]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
