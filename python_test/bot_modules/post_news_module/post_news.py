import numpy as np
import asyncio
import time

from . import get_news
from datetime import datetime,timedelta



async def post_news(client):
    """ Function that calculate random time to post news and post it"""
    await client.wait_until_ready()
    today_date = None
    channels_to_post = (566337001167519756,566340765656154132,567017783515283496,
                        567313449361735681,571290970906165249,570631337443328000,571255135284625428)
    news_to_send = (get_news.secure_lab_news,get_news.habr_news,get_news.tproger_news)
    while (True):
        today_time = datetime.today().replace(second = 0)

        if today_date != datetime.today().date(): 
            today = datetime.today()
            today_date = today.date()
            today_start = today.replace(hour = 15, minute = 00)
            unixtime_start = time.mktime(today_start.timetuple()) # convert to unix for add random shift

            random_time_shift = np.random.randint(25200, size = 3)  #shift for calculate random times since today_start time

            unix_time_to_post = random_time_shift+unixtime_start  
            times_to_post = [datetime.fromtimestamp(time_.item()).replace(second = 0) for time_ in unix_time_to_post] #convert times with shifts to datetime
        
        if today_time in times_to_post:
            i=0
            client.get_channel(random.chois(channels_to_post)).send(news_to_send[i])
            i+=1
        
        

        await asyncio.sleep(10)
    
    #return datetime.datetime.now()
    

if __name__ == '__main__':
    pass