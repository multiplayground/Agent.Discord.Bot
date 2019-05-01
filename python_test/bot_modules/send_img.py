import asyncio
import discord


call=False
img=None
async def send_img(channel,image):
    global call
    global img
    if call:
        await img.delete()
    call=True
    img = await channel.send(file=discord.File(f'D:/Python/MLP/Agent.Discord.Bot/python_test/bot_modules/{image}'))

    
    


