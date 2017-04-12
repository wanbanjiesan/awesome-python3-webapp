# import asyncio
#
# async def hello(d):
#     print("Hello world! %d" % d)
#     r = await asyncio.sleep(2)
#     print("Hello again! %d" % d)
#
# all_tasks = asyncio.gather(hello(1), hello(2), hello(3))
# loop = asyncio.get_event_loop()
# loop.run_until_complete(all_tasks)
# loop.close()
import asyncio
import aiomysql
import logging

logging.basicConfig(level=logging.INFO)

loop = asyncio.get_event_loop()


@asyncio.coroutine
def go():
    pool = yield from aiomysql.create_pool(host='127.0.0.1', port=3306,
                                           user='fq', password='fq',
                                           db='fq', loop=loop)
    with (yield from pool) as conn:
        cur = yield from conn.cursor()
        yield from cur.execute("SELECT * from user")
        rs = yield from cur.fetchall()
        for r in rs:
            print(r)

        yield from cur.close()
        logging.info('    rows returned: %s' % len(rs))
    pool.close()
    yield from pool.wait_closed()


loop.run_until_complete(go())
