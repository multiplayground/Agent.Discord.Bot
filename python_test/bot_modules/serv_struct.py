import asyncio
import json
from .Rpc_Client import RpcClient
import pickle
from  .tree import *
import dill
import weakref


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

def make_dict(dict_,elem):
    return dict_.setdefault(str(channel.category),[]).append(channel.name)

def return_struct ():
    return channels_to_MQ

async def my_background_task(client):
    global channels_to_MQ
    await client.wait_until_ready()
    
    channel_to_send = client.get_channel(568791671764942868) # channel ID goes here
    #msg = await channel_to_send.send('starting...')
    #msg = await channel_to_send.fetch_message(572039983196536851)
    channels_str=None

    while True:
        chan_per={}
        channels_dict={}
        channel_type={0:'TextChannel',2:'VoiceChannel',4:'Category'}
        
        

        if channels_str != sorted(client.get_all_channels(),key=lambda x:x.position):
            channels= client.get_all_channels()
            channels_str=sorted(client.get_all_channels(),key=lambda x:x.position)
            
            print('==Trigered==')
            tree = Node()
            tree.Data = DiscordNode("MLP Discord","root")
            for channel in sorted(channels,key=lambda x:x.position):
                
                try: 
                    chan_per[str(channel.category)].append(DiscordNode(channel.name,channel_type[channel._type],str(channel.category)))
                except KeyError:
                    chan_per.setdefault(str(channel.category),[]).append(DiscordNode(channel.name,channel_type[channel._type],str(channel.category)))
            
            i=0
            for chan in chan_per["None"]:
                globals()[f'chan{i}'] = tree.AddChild(chan)
                i+=1
            i=0
            for key,chans in chan_per.items():
                if key != 'None':
                    for chan in chans:
                        globals()[f'chan{i}'].AddChild(chan)
                    i+=1

            j = tree.toJSON()
            
            
            with RpcClient(aHostName='157.230.108.47',aQueueName='Step.Convert.DiscordTree2PlantUml') as rpcClient:
                message = j
                print(channels_to_MQ)
                print(" [x] Requesting")
                response = rpcClient.call(message)
                print(" [.] Got %r"% response)
         
        
        await asyncio.sleep(10) # task runs every 60 seconds
        