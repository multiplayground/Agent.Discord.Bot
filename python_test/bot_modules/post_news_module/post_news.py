import numpy
import datetime



async def time_to_post():
    return datetime.datetime.now()
    

if __name__ == '__main__':
    await time_to_post()