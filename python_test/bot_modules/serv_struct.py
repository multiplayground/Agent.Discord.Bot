import asyncio
import json
from .Rpc_Client import RpcClient
import pickle
from  .tree import *
import base64
from .send_img import send_img
import os.path




class DiscordNode:
    def __init__(self, 
                aNodePName:str =None, 
                aNodePKind:str =None,
                aNodePDescr:str =None):
        self.NodePName = aNodePName
        self.NodePKind = aNodePKind
        self.NodePDescr = aNodePDescr

    
      
channels_to_MQ=None
send=False
static=os.path.join(os.path.dirname(os.path.dirname(__file__)),'static')
def make_dict(dict_,elem):
    return dict_.setdefault(str(channel.category),[]).append(channel.name)

def return_struct ():
    return channels_to_MQ

async def my_background_task(client):
    global channels_to_MQ
    await client.wait_until_ready()
    
    channel_to_send = client.get_channel(571991415350099972) # 568791671764942868 -noisy tests 571991415350099972 - automaton
    #msg = await channel_to_send.send('starting...')
    #msg = await channel_to_send.fetch_message(572039983196536851)
    channels_str=None
    channel_tipes_1=None
    while True:
        chan_per={}
        channel_tipes=[]
        channel_type={0:'TextChannel',2:'VoiceChannel',4:'Category'}
        tree = Node()
        tree.Data = DiscordNode("MLP Discord","root")
        channels= client.get_all_channels()
        
        for channel in sorted(channels,key=lambda x:x.position):
                try: 
                    chan_per[str(channel.category)].append(DiscordNode(channel.name,channel_type[channel._type],(channel.topic if channel._type == 0 else '')))
                except KeyError:
                    chan_per.setdefault(str(channel.category),[]).append(DiscordNode(channel.name,channel_type[channel._type],(channel.topic if channel._type == 0 else '')))
                channel_tipes.append(channel.name)
                channel_tipes.append(channel.topic if channel._type == 0 else '')
        

        if channel_tipes != channel_tipes_1 :
            channel_tipes_1 = channel_tipes
            
            for chan in chan_per["None"]:
                globals()[f'{chan.NodePName}'] = tree.AddChild(chan)
        
            for key,chans in chan_per.items():
                if key != 'None':
                    for chan in chans:
                        globals()[f'{key}'].AddChild(chan)
                    

            j = tree.toJSON()
            
            

            with RpcClient(aHostName='157.230.108.47',aQueueName='Task.Discord.Tree') as rpcClient:
                message = j
                response = bytes(rpcClient.call(message),'utf-8')
                fh = open(static+"/serv_sturct.png", "wb")
                fh.write(base64.decodestring(response))
                fh.close()
            
            await send_img(client.get_channel(571991415350099972),'serv_sturct.png')
            
            
        await asyncio.sleep(1)
        