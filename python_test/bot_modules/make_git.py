import numpy as np
import manage_with_git as git
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import cm
from datetime import datetime
from collections import defaultdict
from mpl_toolkits.mplot3d import Axes3D 


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
        
def make_all_users_plot(users_iseue):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    nbins = 50
    
    for z in range(len(users_iseue)):
        ys = np.random.normal(loc=10, scale=10, size=2000)

        hist, bins = np.histogram(ys)
        xs = (bins[:-1] + bins[1:])/2

        ax.bar(xs, hist, zs=z, zdir='y', alpha=0.8)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

if __name__ == '__main__':
    
    users_iseue =git.get_users_isues()
    make_all_users_plot(users_iseue)
    # for user in users_iseue:
    #     if users_iseue[user]:
    #         make_user_plot(users_iseue[user],user).show()