import time
import asyncio
async def one():
    x=[]
    for i in range (10):
        x.append(i)
        time.sleep(1)
async def two():
    x=[]
    for i in range (100):
        print('in two',i)
        await asyncio.sleep(1)

loop =asyncio.get_event_loop()
one_r=loop.create_task(one())
two_r =loop.create_task(two())

loop.run_forever()