import discord

import asyncio
import aiohttp
import requests
from connexion.resolver import RestyResolver


# client=discord.Client()

# @client.event
# async def on_message (message):
#     print (message.content)
#     if message.content.startswith('hello'):
#         msg = await message.channel.send('Hello')
        

#     if message.content.startswith('!'):
#         await before.edit(content='40')
    

# client.run(my_token.token)



class MyClient(discord.Client):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create the background task and run it in the background
        #self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_ready(self):
        print('Connected!')
        print('Username: {0.name}\nID: {0.id}'.format(self.user))


        """
        # channels=self.get_all_channels()
        # categories={}
        # for channel in sorted(channels,key=lambda x:x.position):
        #     categories.setdefault(str(channel.category),[]).append(channel.name)

        # print('\n{}'.join(categories['None']).format(' stest'))     
        #print(categories[categories['None'][1]])
        
            
        #print ( categories)
        #print(type(category))
        #await message.channel.send(''.join(self.get_all_channels()))
        """
    async def on_message(self, message):
        if message.content.endswith('book'):
            print(message.content.rsplit(' ', 1)[0] )
            print(f"http://157.230.108.47:9090/v1.0/Litres/{message.content.rsplit(' ', 1)[0]}")
            await message.channel.send(str  (requests.get(f"http://157.230.108.47:9090/v1.0/Litres/{message.content.rsplit(' ', 1)[0]}").json()  )   )

    async def my_background_task(self):
        await self.wait_until_ready()
        counter = 0
        channel = self.get_channel(568791671764942868) # channel ID goes here
        msg = await channel.send('test')
        while True:
            channels=self.get_all_channels()
            categories={}
            for channel in sorted(channels,key=lambda x:x.position):
                categories.setdefault(str(channel.category),[]).append(channel.name)
                
            await msg.edit(content ='\n'.join('%s\n     %s' %(i,j) for i,j in zip(categories['None'],(categories[i] for i in categories['None']))))

            counter += 1
            print(f'it works {counter} times')
            await asyncio.sleep(30) # task runs every 60 seconds


client = MyClient()   

async def main ():
    await client.login('NTY3MzczMjMxNTk0NTM2OTcx.XLSmfw.N3pI725EZ6UX5stctyE8ccf19so')

if __name__ == '__main':
    asyncio.run(main())