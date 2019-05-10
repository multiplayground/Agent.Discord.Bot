import asyncio
import discord
import os.path



static=os.path.join(os.path.dirname(os.path.dirname(__file__)),'static/')
call=False
img=None
async def send_img(channel,image):
    global call
    global img
    if call:
        await img.delete()
    call=True
    print(static+image)
    img = await channel.send(file=discord.File(static+image))

    
    


