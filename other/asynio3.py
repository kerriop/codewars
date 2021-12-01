import asyncio
from asyncio import sleep
import asyncpg


QUERY = """INSERT INTO some_test_table VALUES ($1, $2, $3)"""


async def make_request(db_pool):
    await db_pool.fetch(QUERY, 1, "some_string", 3)
    await sleep(.1)


async def main():
    chunk = 5000
    tasks = []
    pended = 0

    db_pool = await asyncpg.create_pool("postgresql://postgres:123456@localhost:5432/some_test_database")

    for x in range(10_000):
        tasks.append(asyncio.create_task(make_request(db_pool)))
        pended += 1
        if len(tasks) == chunk or pended == 10_000:
            await asyncio.gather(*tasks)
            tasks = []
            print(pended)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
