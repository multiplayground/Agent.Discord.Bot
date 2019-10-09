import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import json
import os

from .get_trelo_score import get_trello_data
from mpl_toolkits.mplot3d import Axes3D

# path to safe drawn dashbord
static=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),'static/')

def make_dataframe_by(value:str=None):
    '''
    Function that get data from trello and for a Data frame of required data
    first 3 columns contain that required data such:    '0' name of card
                                                        '1' data when card have been started
                                                        '2' data when card finished if so
                                                        '3' label of the card
    all other columns contain data by with we can choose them:
                                                        4-(-1) member that assigned to card
                                                        -1 name of list to which card belon
    you can pass string with interesting value of feature as an argument and gen whole spectre of rows
    where that feature is present: for expample you can pass neme list of cards 'Backlog'                                                    
                                                                                                            
                        '''
    trello_data = get_trello_data()

                # with open ('trello_data.txt','w') as file:
                #     file.write(json.dumps(trello_data))


    # Find maximum members per card for set index dataframe dimension
    max_len = max([len(i[2]['who']) if i[2]['who'] else 0 for i in trello_data])    
                                                                                    
    # Indeces by list taht contain the card
    indeces1 = [el[0] for el in trello_data]

    # Semple of Dataframe that will be filled with propriate data                                       
    indeces2 = pd.DataFrame(index =range(len(indeces1)),columns = range(max_len+1)).fillna(0)   

    # Fill resulting DataFrame with members
    #  one column for eache member with respect of card where they participate
    for i in range(max_len):                                                      
        indeces2.iloc[:,i] = [  el[2]['who'][i] 
                                if el[2]['who'] and len(el[2]['who']) > i 
                                else None 
                                for el in trello_data]

    #  Fille last column with list name to which each card belong
    indeces2.iloc[:,-1]= indeces1

    # Collect interesting data: 1) card name 2) card start time 3) card finish time if it is
    data = [  (el[1],t(el[2]['time_start']),t(el[2]['time_close']),el[2]['label']) 
                for el in trello_data]

    
    # Accemble result dataframe
    indeces3 = pd.DataFrame(data) 
    result = pd.concat([indeces3,indeces2],axis = 1,ignore_index = True)
    result.index=result[1]
    if value:
        result = select_from_dataframe(result,value)
       
    return result
    
    # print(frame[0][(frame=='Wombat(Олег)').any(axis=1)])

def draw_dashbord():
    '''
        Actualy draw desiered dashbord 
    '''
    data = make_dataframe_by()

    # Set some pretty style to plot
    with plt.style.context('bmh'):

        fig = plt.figure(figsize=(16,8))
        fig.autofmt_xdate()

        # Brake figure to grid of axis
        grid = plt.GridSpec(4,4,hspace = 0.1,wspace = 0.1)

        # Setup places to eachi axes
        main_ax = fig.add_subplot(grid[:-2,1:])
        hist_ax = fig.add_subplot(grid[:-2,0])
        forth_ax = fig.add_subplot(grid[3,:-1])
        third_ax = fig.add_subplot(grid[2,:-1],sharex=forth_ax)
        plt.setp(third_ax.get_xticklabels(), visible=False)
        with plt.style.context('seaborn-white'):
            fifth = fig.add_subplot(grid[-2:,-1:],projection = '3d')
        
        # Pass needed data to first axes
        hist_ax.hist(data[6],label = 'Колличество задач')
        hist_ax.legend(loc = 'best')
        
        # Pass needed data to second axes
        data[1].hist(ax=main_ax,color = 'orange',alpha = 0.5,width = 0.8,label = 'добавлены')
        data[2].hist(ax=main_ax,width = 0.9,label = 'выполнены')
        main_ax.set_xlim(data[1].min(),)
        main_ax.legend(title='Всего задач по времени',loc  = 'upper left')
        main_ax.locator_params(axis = 'y',nbins = 10)

        # Pass needed data to therd axes
        # get data to plot frontend statistick
        open_b,close_b = sub_culc_for_rate_graph(data,'backend')
        # get data to plot backend statistick
        open_f,close_f = sub_culc_for_rate_graph(data,'frontend')
        
        # plot backend statisticn 
        
        third_ax.plot(open_b.index,open_b,color = 'orange',label='добавлены')
        third_ax.fill_between(open_b.index,open_b,0,alpha=0.3,color = 'orange')

        third_ax.plot(close_b.index,close_b,label='выполнены')
        third_ax.fill_between(close_b.index,close_b,0,alpha=0.5)

        third_ax.set_ylim(0,open_b.max()+10)

        # plot frontend statisticn
        forth_ax.plot(open_f.index,open_f,color = 'orange',label='добавлены')
        forth_ax.fill_between(open_f.index,open_f,0,alpha=0.3,color = 'orange')

        forth_ax.plot(close_f.index,close_f,label='выполнены')
        forth_ax.fill_between(close_f.index,close_f,0,alpha=0.5)
        
        forth_ax.set_ylim(0,open_f.max()+10)

        # place legends for back and frontend graphs
        third_ax.legend(title = 'Задания Backend',loc = 'upper left')
        forth_ax.legend(title = 'Задания Frontend',loc = 'upper left')

        fig.subplots_adjust(left=0.02, right=0.99, bottom=0.03, top=0.99)


        plt.savefig(static+'ceres_dashbord_pre.png')
        # plt.show()

def t(time:str=None):
    '''
       Conver string with time to pandas timestamp object
    '''
    if time:
        return pd.Timestamp(time)
    return None

def select_from_dataframe(data:pd.DataFrame=None,value:str=None):
    '''
      Returns row with passed value from dataframe
    '''
    if value:
        return data[(data==value).any(axis=1)]
    return data

def sub_culc_for_rate_graph(data:pd.DataFrame,label:str):
    '''
        Function that calculat quantity of 
        open and close tasks in backend and frontend.
    
    '''
    back = select_from_dataframe(data,label).sort_index()
    x:list = list()
    y:list = list()
    for i in back.index:
        x.append(back[back.index<=i][back==label][3].value_counts().values[0])
    back_ = back.dropna(subset=[2]).copy().sort_values([2])
    back_ = back_
    for i in back_[2]:
        y.append(back[back[2]<=i][back==label][3].value_counts().values[0])

    back['sub']=x
    back = back['sub']
    back.loc[pd.to_datetime('today')] = back.max()

    back_['sub']=y
    back_.set_index(pd.to_datetime(back_[2]).dt.tz_localize(None),inplace=True)
    back_ = back_['sub']
    back_.loc[pd.to_datetime('today')] = back_.max()
    
    return back,back_


if __name__ == '__main__':
    from get_trelo_score import get_trello_data
    with open('trello_data.txt','r') as file:
        trello_data = json.load(file)
    draw_dashbord()    
    
    