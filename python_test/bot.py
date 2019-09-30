
import bot_modules.post_news_module.post_news  as p_nw
import bot_modules.reaction_hendler as r_hd
import bot_modules.make_git as m_gi
import bot_modules.make_api as api
import channels_module     
import settings                          #import id of channels exists on server
import logging
import discord
import asyncio
import json
import sys
import os

from bot_modules.trello.draw_dashbord import draw_dashbord
from bot_modules.send_img import Send_img
from bot_modules.post_news_module.post_news import post_news,send_news
from bot_modules.serv_struct import my_background_task,channels_to_MQ,return_struct



client=discord.Client()
@client.event
async def on_message (message):
    global channel_to_send
    global received
    global switch


    if message.content.startswith('hello'):
        await message.channel.send('Hello')
      
    if message.content=='|':
        print('=======',message.channel.id)
        channel_to_send= message.channel
        await message.delete()

    if message.content.startswith('! '):
        await message.channel.send("Список команд на данынй момент:\n\t\
                                    !level    - узнать уровень пользователя в проекте\n\t\
                                    !news     - чтобы узнать побольше интересного\n\t\
                                    !git      - покажет статистику участия в проэкте на остнове git активности\n\t\
                                    !ceres    - список команд для проэкта ceres\n\t\
                                    |         - вызвать в чат лоадинг")

    if message.content=='!do':
        await message.channel.send("Список команд на данынй момент:\n\t\
                                    !level    - узнать уровень пользователя в проекте\n\t\
                                    !news     - чтобы узнать побольше интересного\n\t\
                                    !git      - покажет статистику участия в проэкте на остнове git активности\n\t\
                                    !ceres    - список команд для проэкта ceres\n\t\
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
            await message.channel.send('Команда *level* имеет вид: !level *{интересующее имя} {аргументы}*\n\
                                            \tСписок аргументов:\n\
                                                  -p   - Ответ в личном сообщении')

    if message.content.startswith('!git'):
        git_img = Send_img()
        _,*comands=message.content.split()
        print(comands)
        if '-is' in comands:
            print('git is')
            m_gi.make_all_users_plot()
            await git_img.send_img(message.channel,'users_git_isues.png')
        else:
            await message.channel.send('Команда *git* имеет вид: !git *{аргументы}*\n\
                                                \tСписок аргументов:\n\
                                                    -is   - Колличество выполненых и взятых на выполнение задачь\n\t\
                                                          в графичесском представлении ')
        
    if message.content.startswith('!news'):
        _,*comands=message.content.split()
        if not comands:
             await message.channel.send('Команда *news* имеет вид: !news *{аргументы}*\n\
                                                \tСписок аргументов:\n\
                                                    --more    - Запостить еще одну случайную сегодняшнюю новость')
        if '--more' in comands:
            await message.channel.send('  **Еще одна случайная новость не будет лишней**\n')
            await p_nw.more_news(client,message.channel.id)

    if message.content.startswith('!ceres'):
        _,*comands=message.content.split()
        ceres_img = Send_img()
        if '-b' in comands:
            draw_dashbord()
            await ceres_img.send_img(message.channel,'ceres_dashbord.png')
        else:
            await message.channel.send('Команда *ceres* имеет вид: !ceres *{аргументы}*\n\
                                                \tСписок аргументов:\n\
                                                    -b   - Постит небольшой дашборд проекта с основными показателями')
                                                          
    if message.content == '?':
        chant_id = message.channel.id
        author_id =message.author.id
        channle_ = message.channel
        print(chant_id,channle_)
        # await client.get_user(306146990440579084).send(f'fron chat: {chant_id}\nfrom author:{author_id}')

        
@client.event
async def on_ready():
    global initialized
    print('Connected!')
    print('Username: {0.name}\nID: {0.id}'.format(client.user))

    if initialized == 0:
        
        loop = asyncio.get_event_loop()
        loop.create_task(loading())
        loop.create_task(my_background_task(client))
        loop.create_task(p_nw.post_news(client))
        
        initialized = 1


async def loading():
    global channel_to_send
    await client.wait_until_ready()
    channel_to_send = client.get_channel(settings.main_channel)
    msg = await channel_to_send.send('starting...')
    
    msg_id=msg.id
    while True:
        if channel_to_send!=msg.channel:
            await msg.delete()  
            msg = await channel_to_send.send('\n\nstarting...')
            msg_id=msg.id
        msg = await channel_to_send.fetch_message(msg_id)
        await msg.edit(content='\n\nMLP Bot v 0.0.4\n│')
        await msg.edit(content='\n\nMLP Bot v 0.0.4\n╱')
        await msg.edit(content='\n\nMLP Bot v 0.0.4\n━')
        await msg.edit(content='\n\nMLP Bot v 0.0.4\n╲')
       




if __name__ == '__main__':
    if len(sys.argv)>1:
        if sys.argv[1] == '-d':
            settings.main_channel = channels_module.noisy_tests
        else:
            raise Exception ('''the unknown property, maybe you've wanted to type "-d" for debug mode''')
    else:
        settings.main_channel = channels_module.automaton
    channel_to_send=None
    connection=None
    initialized=0
    
    client.run(os.environ['MLP_BOT'])
