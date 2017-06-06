import time
import asyncio

start = time.time()

async def do_some_work(x):
    print('Waiting: ', x)

loop = asyncio.get_event_loop()
loop.run_until_complete(do_some_work(2))

print('TIME: ', time.time() - start)