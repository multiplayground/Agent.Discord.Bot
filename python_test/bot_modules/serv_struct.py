import asyncio
import os.path
import pickle
import base64
import json
from  .tree import *
from .send_img import Send_img
from .Rpc_Client import RpcClient




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
    
    channel_to_send = client.get_channel(568791671764942868) # 568791671764942868 -noisy tests 571991415350099972 - automaton
    channels_str=None
    channel_tipes_1=None
    
    str_img = Send_img()
    while True:
        chan_per={}
        channel_tipes=[]
        channel_type={'text':'TextChannel','voice':'VoiceChannel','category':'Category'}
        tree = Node()
        tree.Data = DiscordNode("MLP Discord","root")
        channels= client.get_all_channels()
        
        for channel in sorted(channels,key=lambda x:x.position):
                
                try: 
                    chan_per[str(channel.category)].append(DiscordNode(channel.name,channel_type[str(channel.type)],(channel.topic if str(channel.type) == 'text' else '')))
                except KeyError:
                    chan_per.setdefault(str(channel.category),[]).append(DiscordNode(channel.name,channel_type[str(channel.type)],(channel.topic if str(channel.type) == 'text' else '')))
                channel_tipes.append(channel.name)
                channel_tipes.append(channel.topic if str(channel.type) == 'text' else '')
        

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
                print('sended')
                print(static)
                resp = rpcClient.call(message)
                if resp == 'None':
                    await str_img.del_img()
                    await str_img.send_img(client.get_channel(568791671764942868),'serv_sturct.1.png')
                else:
                    response = bytes(resp,'utf-8')
                    fh = open(static+"/serv_sturct.png", "wb")
                    fh.write(base64.decodestring(response))
                    fh.close()
                    await str_img.del_img()
                    await str_img.send_img(client.get_channel(568791671764942868),'serv_sturct.png')
            
            
        await asyncio.sleep(1)



        