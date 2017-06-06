#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import asyncio

async def hello(x):
    print(x)
    print('Hello world! (%s)' % threading.currentThread())
    await asyncio.sleep(3)
    print(x)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(2), hello(3)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
