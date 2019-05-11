import discord
import my_token
import asyncio
import aiohttp
import aio_pika
from bot_modules.serv_struct import my_background_task,channels_to_MQ,return_struct
import bot_modules.make_api as api
import json
import bot_modules.send_img as send_img



initialized=0
received=['___no']
send=['___no']
channel_to_send=None
connection=None
initialized=0
switch=True
start_rebbit=False


client=discord.Client()

@client.event
async def on_message (message):
    global channel_to_send
    global received
    global switch
    global start_rebbit
    #print (message.content,message.id,message.channel)
    if message.content.startswith('hello'):
        await message.channel.send('Hello')
        await message.channel.send(received)
        

    if message.content=='!':
        
        channel_to_send= message.channel
        await message.delete()


    if message.content=='start rabbit':
        start_rebbit=True
        await message.delete()
    
    if message.content =='stop rabbit':
        start_rebbit=False
        await message.delete()

   
        
@client.event
async def on_ready():
    global initialized
    
    print('Connected!')
    print('Username: {0.name}\nID: {0.id}'.format(client.user))
    if initialized == 0:
        loop = asyncio.get_event_loop()
        loop.create_task(loading())
        loop.create_task(my_background_task(client))
        
        initialized = 1


async def loading():
    global channel_to_send
    await client.wait_until_ready()
    channel_to_send = client.get_channel(571991415350099972) 
    msg = await channel_to_send.send('starting...')
    
    msg_id=msg.id
    while True:
        if channel_to_send!=msg.channel:
            await msg.delete()  
            msg = await channel_to_send.send('\n\nstarting...')
            msg_id=msg.id
        msg = await channel_to_send.fetch_message(msg_id)
        await msg.edit(content='MLP Bot v 0.0.2\n│')
        await msg.edit(content='MLP Bot v 0.0.2\n╱')
        await msg.edit(content='MLP Bot v 0.0.2\n━')
        await msg.edit(content='MLP Bot v 0.0.2\n╲')
       


client.run(my_token.token)

