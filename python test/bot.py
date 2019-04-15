import discord

client=discord.Client()


@client.event
async def on_message (message):
    if message.content.startwith('!hello'):
        msg = 'Hello {O.author.mention}'.format(message)
        await client.send_message(message.channel, msg)


client.run('NTY3MzczMjMxNTk0NTM2OTcx.XLSmfw.N3pI725EZ6UX5stctyE8ccf19so')