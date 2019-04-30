import discord
import my_token
import asyncio
import aiohttp
import aio_pika
from bot_modules.serv_struct import my_background_task,channels_to_MQ
import bot_modules.make_api as api
import json

initialized=0
received=['___no']
send=['___no']
channel_to_send=None
connection=None
client=discord.Client()
initialized=0


# async def work_with_msg(message):
#     global connection
#     while True:
#         await send_in_rebbit(connection,channels_to_MQ)
#         await asyncio.sleep(3)



@client.event
async def on_message (message):
    global channel_to_send
    global received
    print (message.content,message.id)
    if message.content.startswith('hello'):
        await message.channel.send('Hello')
        await message.channel.send(received)
        

    if message.content=='!':
        print('=======',message.channel.id)
        channel_to_send= message.channel

    if message.content.startswith('msg'):
        print(received)
        await message.channel.send(received.pop() if received[-1]!='___no' else 'no massege in que')
        
    
@client.event
async def on_ready():
    global initialized
    
    print('Connected!')
    print('Username: {0.name}\nID: {0.id}'.format(client.user))
    if initialized == 0:
        loop = asyncio.get_event_loop()
        loop.create_task(main(loop))
        loop.create_task(loading())
        #loop.create_task(send_in_rebbit(connection))
        initialized = 1


async def main(loop):
    #start rabbitMQ
    global received
    global connection
    connection = await aio_pika.connect(    "amqp://root:toor@157.230.108.47/",loop=loop)
    print("rabbitMQ connected :)")
    recieve_channel = await connection.channel()
    send_channel = await connection.channel()
    recieve_queue = await recieve_channel.declare_queue("in_MLP_bot")
    send_queue = await send_channel.declare_queue("out_MLP_bot")
    while True: 
            await send_channel.default_exchange.publish(aio_pika.Message( body = 'test send'.encode()),routing_key='out_MLP_bot')
            print(my_background_task(client).next)
            await asyncio.sleep(10)   
    async with recieve_queue.iterator() as queue_iter:
        async for message in queue_iter:
            async with message.process():
                received.append(message.body)
    
    
async def send_in_rebbit(connection):
    async with connection:
        routing_key = "out_MLP_bot"
        channel = await connection.channel()
        while True: 
            await channel.default_exchange.publish(aio_pika.Message( body='Test send'),routing_key=routing_key)
            print('in send ')
            await asyncio.sleet(10)    

async def loading():
    global channel_to_send
    await client.wait_until_ready()
    channel_to_send = client.get_channel(568791671764942868) # test 568791671764942868  auto 571991415350099972
    msg = await channel_to_send.send('starting...')
    #msg = await channel_to_send.fetch_message(572041231857614858)
    msg_id=msg.id
    while True:
        if channel_to_send!=msg.channel:
            await msg.delete()  
            msg = await channel_to_send.send('\n\nstarting...')
            msg_id=msg.id
        msg = await channel_to_send.fetch_message(msg_id)
        await msg.edit(content='\n\nMLP Bot v 0.0.1\n│')
        await msg.edit(content='\n\nMLP Bot v 0.0.1\n╱')
        await msg.edit(content='\n\nMLP Bot v 0.0.1\n━')
        await msg.edit(content='\n\nMLP Bot v 0.0.1\n╲')
       



#bg_task = client.loop.ensure_furure(my_background_task())
#asyncio.ensure_future(my_background_task(client))
#asyncio.ensure_future(loading())
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
    