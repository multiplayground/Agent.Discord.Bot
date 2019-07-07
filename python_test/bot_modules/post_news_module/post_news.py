import numpy as np
import asyncio
import random
import time

from . import get_news
from datetime import datetime,timedelta



async def post_news(client):
    """ Function that calculate random time to post news and post it"""
    await client.wait_until_ready()
    today_date = None
    channels_to_post = (566337001167519756,566340765656154132,567017783515283496,566322218213048331,
                        567313449361735681,571290970906165249,570631337443328000,571255135284625428)
    
    while (True):
        today_time = datetime.today().replace(second = 0,microsecond = 0)  # time to compare with set of random times to post

        if today_date != datetime.today().date():  # one time per day reset the set of random times to post and renew set of posts
            
            news_to_send = [get_news.secure_lab_news(), get_news.habr_news(), get_news.tproger_news()]  #set of post to be poped to post
            
            today = datetime.today()
            today_date = today.date()
            today_start = today.replace(hour = 12, minute = 0) # have been replace to 15 00
            unixtime_start = time.mktime(today_start.timetuple()) # convert to unix for add random shift
            
            random_time_shift = np.random.randint(25200, size = 3) #25200 #shift for calculate random times since today_start time

            unix_time_to_post = random_time_shift+unixtime_start  
            times_to_post = [datetime.fromtimestamp(time_.item()).replace(second = 0) for time_ in unix_time_to_post] #convert times with shifts to datetime
            await client.get_user(306146990440579084).send([i for i in times_to_post])
        if today_time in times_to_post:
            times_to_post.remove(today_time)
            send_news(client,random.choice(channels_to_post),news_to_send.pop())
            #await client.get_channel(random.choice(channels_to_post)).send(news_to_send.pop()) # pop out message to random channel
        
        await asyncio.sleep(10)
    
async def more_news (client,channel):
    news_to_send = [get_news.secure_lab_news(), get_news.habr_news(), get_news.tproger_news()]
    await send_news(client,channel,random.choice(news_to_send))

    
async def send_news (client,channel,news):
    await client.get_channel(channel).send(news)


if __name__ == '__main__':
    pass