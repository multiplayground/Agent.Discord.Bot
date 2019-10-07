import asyncio
import discord
import os.path


class Send_img:
    def __init__ (self):
        self.path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'static/')
        self.img=None


    async def send_img(self,channel,image):
        self.img = await channel.send(file=discord.File(self.path+image))

    async def del_img (self):
        if self.img != None:
            await self.img.delete()

    async def maintain_img (self,channel,image):
        if self.img == None:
            await self.send_img(channel,image)
            break
        await self.del_img()
        await self.send_img(channel,image)
        

'''
static=os.path.join(os.path.dirname(os.path.dirname(__file__)),'static/')

img=None
async def send_img(channel,image):
    global call
    global img
    
    
    print(static+image)
    img = await channel.send(file=discord.File(static+image))

'''

