import discord
import asyncio
import time
import json
import sys
from aio_pika import connect, Message, ExchangeType
from datetime import datetime

start_time = 0
handledMessages = 0
retries = 0


	
#initialize discord client and make the incoming message queue variable global 
client = 0
incoming_msg_channel = ""
incoming_msg_exchange = ""

botKey = 'NTY3MzczMjMxNTk0NTM2OTcx.XLSmfw.N3pI725EZ6UX5stctyE8ccf19so'
rabbitHost = '157.230.108.47'
rabbitUser = 'root'
rabbitPass = 'toor'
initialized = 0




#bot handling down here
client = discord.Client()
#queue message handling
async def on_queue_message(message: Message):
	global client
	#message received from queue
	#decode json
	message.ack()
	message_cont = json.loads(message.body.decode())
	#check the type of message
	if message_cont["type"] == "message":
		print('\n\nIN ON QUE\n\n',message_cont)
	elif message_cont["type"] == "delete":
		print('\n\nIN ON QUE\n\n',message_cont)
	elif message_cont["type"] == "react":
		print('\n\nIN ON QUE\n\n',message_cont)
	

async def main(loop):
	#start rabbitMQ
	global incoming_msg_channel
	global incoming_msg_exchange
	global rabbitHost
	global rabbitUser
	global rabbitPass
	connection = await connect("amqp://"+rabbitUser+":"+rabbitPass+"@"+rabbitHost+"/",loop=loop)
	print("rabbitMQ connected :)")
	channel_out = await connection.channel()
	queue = await channel_out.declare_queue("msg_out")


	incoming_msg_channel = await connection.channel()
	incoming_msg_exchange = await incoming_msg_channel.declare_exchange("msg_in", ExchangeType.FANOUT)


	await queue.consume(on_queue_message)



@client.event
async def on_ready():
	global start_time
	global initialized
	start_time = time.time()
	#when discord bot is ready
	print("bot online")
	print("name: {}".format(client.user.name))
	print("ID: {}".format(client.user.id))

	#await client.change_presence(status=discord.Status.idle, activity=discord.Game('with bits!'))
	if initialized == 0:
		loop = asyncio.get_event_loop()
		loop.create_task(main(loop))
		initialized = 1

# @client.event
# async def on_error(event, *args, **kwargs):
# 	print(event)
# 	print(args)
# 	print(kwargs)
# 	loadCode()
@client.event
async def on_message(message):
	global incoming_msg_channel
	global incoming_msg_exchange
	global handledMessages
	global start_time
	handledMessages = handledMessages+1
	if message.content.startswith("get_msg"):
		await message.channel.send('Try to send messege from que')
		await message.channel.send(str(incoming_msg_exchange))
		print('\n\n==========@client.event=============\n\n',message.content)
	elif message.content.startswith("!!stats"):
		print('\n\n==========@client.event=============\n\n',message.content)
	else:
		print('\n\n==========@client.event=============\n\n',message.content)
		
print("starting...")
client.run(botKey)

