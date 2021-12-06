"""
we use async when we want to execute code in parallel, so that a second process 
can start even tough the first one is still unfinished
"""

import asyncio

async def fetch_data():
    print("start fetching")
    await asyncio.sleep(0.1)
    print("fetching done")
    return {"data": 1}

async def print_numbers():
    for i in range(10):
        print(i)
    await asyncio.sleep(2)

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())
    value = await task1
    print(value)
    task2

asyncio.run(main())
