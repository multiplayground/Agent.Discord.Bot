import asyncio
import json
from .Rpc_Client import RpcClient

channels_to_MQ=None
send=False
def return_struct ():
    return channels_to_MQ

async def my_background_task(client):
    global channels_to_MQ
    await client.wait_until_ready()
    
    channel_to_send = client.get_channel(568791671764942868) # channel ID goes here
    #msg = await channel_to_send.send('starting...')
    #msg = await channel_to_send.fetch_message(572039983196536851)
    while True:
        categories={}
        channels_dict={}
        
        channels=client.get_all_channels()
        
        for channel in sorted(channels,key=lambda x:x.position):
            categories.setdefault(str(channel.category),[]).append(channel.name)
        
        for i in categories['None']:
            try:
                categories[i]
            except:
                categories.setdefault(i,[])
        # for indx,i in enumerate(categories['None']):
            
        #     print(str(channel.category))
        # for indx,i in enumerate(categories['None']):
        #     channels_dict['string_'+str(indx)]=('\t'.join(map(str,categories[i]))  )
        if categories!=channels_to_MQ:
            print('==Trigered==')
            channels_to_MQ=categories
            with RpcClient(aHostName='157.230.108.47') as rpcClient:
                message = json.dumps(channels_to_MQ).encode("utf-8")
                print(" [x] Requesting")
                response = rpcClient.call(message)
                print(f" [.] Got {response}")
         
        #await msg.edit(content ='\n\n**     Структура сервера проекта MLP для ознакомления**\n\n'+'\n\n'.join('%s\n     %s' %(i,j) for i,j in zip(categories['None'],(v for k,v in channels_dict.items()))))

        await asyncio.sleep(10) # task runs every 60 seconds
        