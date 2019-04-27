import discord
import my_token
import asyncio
import aiohttp
import requests
from connexion.resolver import RestyResolver
import connexion
from multiprocessing import Pool
from multiprocessing import Process
import aio_pika


initialized=0
received=''
send=[]

client=discord.Client()



async def work_with_msg(message):
    global client
    global received
    print(received)
    print(message.ack())



@client.event
async def on_message (message):
    print (message.content)
    if message.content.startswith('hello'):
        await message.channel.send('Hello')
        await message.channel.send(received)
        

    if message.content.startswith('!'):
        await before.edit(content='40')
    

@client.event
async def on_ready():
    global initialized
    print('Connected!')
    print('Username: {0.name}\nID: {0.id}'.format(client.user))
    loop = asyncio.get_event_loop()
    loop.create_task(main(loop))




async def main(loop):
    #start rabbitMQ
    global received
    connection = await aio_pika.connect(f"amqp://root:toor@157.230.108.47/",loop=loop)
    print("rabbitMQ connected :)")
    channel = await connection.channel()
    queue = await channel.declare_queue("msg_out")
    async with queue.iterator() as queue_iter:
        async for message in queue_iter:
            async with message.process():
                received= message.body
    await queue.consume(work_with_msg)


async def my_background_task():
    global client
    await client.wait_until_ready()
    counter = 0
    channel = client.get_channel(568791671764942868) # channel ID goes here
    print(client.get_all_channels())
    msg = await channel.send('starts')
    # while True:
    #     channels=client.get_all_channels()
    #     categories={}
    #     for channel in sorted(channels,key=lambda x:x.position):
    #         categories.setdefault(str(channel.category),[]).append(channel.name)
            
    #     await msg.edit(content ='\n'.join('%s\n     %s' %(i,j) for i,j in zip(categories['None'],(categories[i] for i in categories['None']))))

    #     counter += 1
    #     print(f'it works {counter} times')
    #     await asyncio.sleep(30) # task runs every 60 seconds

bg_task = client.loop.create_task(my_background_task())

client.run(my_token.token)



# class MyClient(discord.Client):
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         # create the background task and run it in the background
#         #self.bg_task = self.loop.create_task(self.my_background_task())

    
            


#         """
#         # channels=self.get_all_channels()
#         # categories={}
#         # for channel in sorted(channels,key=lambda x:x.position):
#         #     categories.setdefault(str(channel.category),[]).append(channel.name)

#         # print('\n{}'.join(categories['None']).format(' stest'))     
#         #print(categories[categories['None'][1]])
        
            
#         #print ( categories)
#         #print(type(category))
#         #await message.channel.send(''.join(self.get_all_channels()))
#         """
    
#     async def on_message(self, message):
#         if message.content.endswith('book'):
#             print(message.content.rsplit(' ', 1)[0] )
#             print(f"http://157.230.108.47:9090/v1.0/Litres/{message.content.rsplit(' ', 1)[0]}")
#             await message.channel.send(str  (requests.get(f"http://157.230.108.47:9090/v1.0/Litres/{message.content.rsplit(' ', 1)[0]}").json()  )   )

#     async def my_background_task(self):
#         await self.wait_until_ready()
#         counter = 0
#         channel = self.get_channel(568791671764942868) # channel ID goes here
#         msg = await channel.send('test')
#         while True:
          
            
#             channels=self.get_all_channels()
#             categories={}
#             for channel in sorted(channels,key=lambda x:x.position):
#                 categories.setdefault(str(channel.category),[]).append(channel.name)
                
#             await msg.edit(content ='\n'.join('%s\n     %s' %(i,j) for i,j in zip(categories['None'],(categories[i] for i in categories['None']))))

#             counter += 1
#             print(f'it works {counter} times')
#             await asyncio.sleep(30) # task runs every 60 seconds

#     async def main(loop):
#         #start rabbitMQ
#         global received
#         connection = await connect(f"amqp://root:toor@157.230.108.47/",loop=loop)
#         print("rabbitMQ connected :)")
#         channel = await connection.channel()
#         queue = await channel.declare_queue("msg_out")
#         async with queue.iterator() as queue_iter:
#             async for message in queue_iter:
#                 async with message.process():
#                     received =message.body



#     async def on_ready(self):
#         global initialized
#         print('Connected!')
#         print('Username: {0.name}\nID: {0.id}'.format(self.user))
#         if initialized == 0:
#             loop = asyncio.get_event_loop()
#             loop.create_task(main(loop))
#             initialized = 1
        
# client=MyClient()
# #client.run(my_token.token)
     

# if __name__ == '__main__':
#     client.run(my_token.token)
    