import discord
import my_token
import asyncio
import json
from bot_modules.serv_struct import my_background_task,channels_to_MQ,return_struct
import bot_modules.make_api as api
from bot_modules.send_img import send_img
import bot_modules.manage_with_db as m_db
import bot_modules.reaction_hendler as r_hd
import bot_modules.medal_user_score as u_sc
import bot_modules.level_user_score as l_us




channel_to_send=None
connection=None
initialized=0

client=discord.Client()

@client.event
async def on_message (message):
    global channel_to_send
    global received
    global switch
    global start_rebbit
    print (message.content,message.id,message.channel,message.attachments)


    if message.content.startswith('hello'):
        await message.channel.send('Hello')
      
        

    if message.content=='|':
        print('=======',message.channel.id)
        channel_to_send= message.channel
        await message.delete()

    if message.content=='!do':
        await message.channel.send("Список команд на данынй момент:\n\t\
                                    !level    - узнать уровень пользователя в проекте\n\t\
                                    |         - вызвать в чат лоадинг")

    if message.content.startswith('!level'):
        _,*comands=message.content.split()
        if comands:
            level = l_us.get_user_level(comands[0])
            if level=='error':
                msg="**Похоже этого пользователя еще нету в нашем списке**"
            else:
                msg=f'Текущий уровень **{comands[0]}**: **{level}**'
            if '-p' in comands:
                await message.author.send(msg)
            else:
                await message.channel.send(msg)
        else: 
            await message.channel.send('Команда *level* имеет вид: *!level {интересующее имя} {аргументы}*\n\
                                            \tСписок аргументов:\n\
                                                  -p   - Ответ в личном сообщении')


@client.event
async def on_raw_reaction_add(payload):
    user_id=payload.user_id

    guild=client.get_guild(payload.guild_id)
    member=guild.get_member(user_id)    
    roles=[str(role) for role in member.roles]

    emoji=payload.emoji.name
    
    
    print(payload.emoji.id)
    if 'DiscordAdmin' or 'Curator' in roles:
        await r_hd.deal_with_reaciton(payload)
        
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
        await msg.edit(content='\n\nMLP Bot v 0.0.1\n│')
        await msg.edit(content='\n\nMLP Bot v 0.0.1\n╱')
        await msg.edit(content='\n\nMLP Bot v 0.0.1\n━')
        await msg.edit(content='\n\nMLP Bot v 0.0.1\n╲')
       


client.run(my_token.token)

