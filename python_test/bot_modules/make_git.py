import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import os.path
import random
from matplotlib import cm
from datetime import datetime
from collections import defaultdict
from mpl_toolkits.mplot3d import Axes3D
from .manage_with_git import get_users_isues as u_is

static=os.path.join(os.path.dirname(os.path.dirname(__file__)),'static')

def make_user_plot(users_issue,user_name):
    
    users_iseue =git.get_users_isues()
    print(users_issue)
    dates = [val[3][:10]  if val[3] else str(datetime.now())[:10] 
                for val  in users_issue]
    
    
    datetime_object = [datetime.strptime(date, '%Y-%m-%d') for date in dates]
    mpl_dates = mdates.date2num(datetime_object)
    
    fig, ax = plt.subplots()
    month=mdates.MonthLocator()
    days = mdates.DayLocator()
   
    _,_,patches=ax.hist(mpl_dates , histtype='bar', rwidth = 0.8, color = 'orangered' )
    patches[-1].set_facecolor('c')
    ax.xaxis.set_major_locator(days)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %m %y'))
    
    
    ax.grid(True)
    plt.title(user_name)
    fig.autofmt_xdate()
    return plt

    
    

    # fig =plt.figure()
    # ax=fig.add_subplot(111,projection='3d')
    # x,y,z=[len(val) for val  in users_iseue.values() ],[i for i  in range(11) ],[i for i  in range(11) ]
    # ax.bar(x,y,z,zdir='y')
    # plt.show()   
        
def make_all_users_plot():
    users_iseue =u_is()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    months = mdates.MonthLocator()
    days = mdates.DayLocator()
    colors =('orangered','orange','sienna','gold','royalbue','deepskyblue','blueviolet')
    for i,name in enumerate(users_iseue):                               #  make histograms for users one by one
        color_to_bar=random.choice(colors)
        dates = [val[3][:10]  if val[3] else str(datetime.now())[:10]    #  deteckt dates when isue had finished
                for val  in users_iseue[name]]                           #    and convert it to mpl_dates
        datetime_object = [datetime.strptime(date, '%Y-%m-%d')           #    eache date represent an x value
                for date in set(dates)]
        mpl_dates = sorted(mdates.date2num(datetime_object))


        hight = defaultdict(int)                                    #   calculate hight of bars 
        for date in dates:                                          #   represent an z value
            hight[date]+=1

        color_map = list()                                          #   make color map
        [color_map.append(color_to_bar) for date in mpl_dates ]
        if color_map:
            color_map[-1]='g'
        
        if len(mpl_dates):                                          # add hist only if it has values
            print(mpl_dates,list(hight.values()),name)
            ax.bar(mpl_dates,list(hight.values()),i,zdir='y',color = color_map ,alpha = 0.8)
            ax.text(mpl_dates[-1]+4,i-0.1,0,name,color='maroon',zdir=None)
            #ax.text2D(0.05, 0.95, "2D Text", transform=ax.transAxes)

                                             
    ax.xaxis.set_major_locator(months)                                         # set proper view of axis
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %m %y'))
    ax.xaxis.set_minor_locator(days)
    
    zticks = ax.zaxis.get_major_ticks() 
    zticks[0].label1.set_visible(False)
    plt.setp(ax.get_yticklabels(), visible=False)

    ax.set_xlabel('день')
    ax.set_zlabel('заданий')

    ax.ticklabel_format
    print(static+'/users_git_isues.png')
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.savefig(static+'/users_git_isues.png')
    #plt.show()
    

if __name__ == '__main__':
    
    
    make_all_users_plot()
    # for user in users_iseue:
    #     if users_iseue[user]:
    #         make_user_plot(users_iseue[user],user).show()