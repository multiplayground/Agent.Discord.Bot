'''
    The module where storing all task-routines that MLP_Bot provide
'''
import channels_module
import asyncio
import os

from bot_modules.trello import check_similar,draw_dashbord
from bot_modules.send_img import Send_img
# from bot_modules.trello.draw_dashbord import draw_dashbord


async def ceres_dashbord (client):
    '''
        Task to post ceres dashbord
        first it call trello.draw_dashbord() to compleat all needed to draw dashbord and safe temporary file
        then compare if new file identical to old one
        if something changes then post new version
    '''
    # path where store posted images
    static_path=os.path.join(os.path.dirname(__file__),'static/')
    ceres_bord = Send_img()
    while True:
        # perform all drawing actions
        draw_dashbord.draw_dashbord()

        # check if new statement different and if so replace an old one
        # after wich post
        if  not check_similar.is_similar('ceres_dashbord.png','ceres_dashbord_pre.png'):
            await ceres_bord.maintain_img(client.get_channel(channels_module.ceres_stats),'ceres_dashbord.png')

        await asyncio.sleep(1800)
    
    
    