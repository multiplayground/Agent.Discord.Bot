import discord
import my_token
import asyncio
import aiohttp
import aio_pika
from bot_modules.serv_struct import my_background_task,channels_to_MQ,return_struct
import bot_modules.make_api as api
import json
import bot_modules.send_img as send_img
import bot_modules.manage_with_db as m_db 


initialized=0
received=['___no']
send=['___no']
channel_to_send=None
connection=None
client=discord.Client()
initialized=0
switch=True
start_rebbit=False

# async def work_with_msg(message):
#     global connection
#     while True:
#         await send_in_rebbit(connection,channels_to_MQ)
#         await asyncio.sleep(3)

# @client.event
# async def on_raw_reaction_add(pyload):
#     global client
#     print (dir(pyload),pyload.user_id,pyload.emoji)
#     await client.get_channel(pyload.channel_id).send(f'you have got {pyload.emoji} emoji')

@client.event
async def on_message (message):
    global channel_to_send
    global received
    global switch
    global start_rebbit
    print (message.content,message.id,message.channel)
    if message.content.startswith('hello'):
        await message.channel.send('Hello')
        await message.channel.send(received)
        

    if message.content=='!':
        print('=======',message.channel.id)
        channel_to_send= message.channel
        await message.delete()

    if message.content.startswith('msg'):
        print(received)
        await message.channel.send(received.pop() if received[-1]!='___no' else 'no massege in que')

    if message.content=='img':
    
        await send_img.send_img(message.channel,'serv_sturct.png')
        switch=False
        
        await message.delete()

    if message.content=='start rabbit':
        start_rebbit=True
        await message.delete()
    
    if message.content =='stop rabbit':
        start_rebbit=False
        await message.delete()

    if message.content == 'write':
        print (message.author)
        #await message.autor.send(message.autor,'hi')    
        await message.author.send('hi')

    if message.content.startswith('!show'):
        example=m_db.User_Reward()
        #await message.autor.send(message.autor,'hi')    
        await message.channel.send(example.get_all_medals())
        
@client.event
async def on_ready():
    global initialized
    
    print('Connected!')
    print('Username: {0.name}\nID: {0.id}'.format(client.user))
    if initialized == 0:
        loop = asyncio.get_event_loop()
        #loop.create_task(main(loop))
        #loop.create_task(loading())
        loop.create_task(my_background_task(client))
        
        initialized = 1



    
   

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
       


