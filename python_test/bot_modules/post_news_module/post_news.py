import numpy
import datetime



async def time_to_post():
    now = datetime.datetime.now()
    print(now)
    await asyncio.sleep(600)

if __name__ == '__main__':
    await time_to_post()