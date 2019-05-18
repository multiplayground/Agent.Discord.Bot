from itertools import repeat
from  .manage_with_db import *
score ='100001321'
medals ={':scientist:':'100000000',':devops:':'10000000' ,':master:' :'1000000',
        ':diamond:':'100000' ,':platinum:':'10000' ,':gold:':'1000', 
        ':silver:':'100', ':bronze:':'10' ,':unranked:':'1' }
medals_id= {':scientist:':'573572727357702164',':devops:':'573572730763345930' ,':master:' :'573572725352824832',
        ':diamond:':'573572724476215320' ,':platinum:':'573572730516144129' ,':gold:':'573572730956283925', 
        ':silver:':'573572727445913600', ':bronze:':'573572730482327556' ,':unranked:':'573572724560101415' }

#unranc 573572724560101415   bronz 573572730482327556    silver 573572727445913600
# gold 573572730956283925  plat 573572730516144129   diamond 573572724476215320
# master 573572725352824832    devops 573572730763345930    scient 573572727357702164


def get_medals(score=0):
    q_score=to_quaternary(get_score())
    res=[]
    for i,j in zip(q_score,medals):
        res.extend(repeat(f'<{j}{medals_id[j]}>',int(i)))
    top,*other=res
    return res
        

def add_medal(score,medal):
    if len(score)==9:
        dec_sum=int(score,4)+int(medals[medal],4)
        if dec_sum > 262143:
            return to_quaternary(262143)
        return to_quaternary(dec_sum)

def subtracct_medal(score,medal):
    if len(score)==9:
        dec_sum=int(score,4)-int(medals[medal],4)
        if dec_sum < 0:
            return to_quaternary(0)        
        return to_quaternary(dec_sum)

def to_quaternary(number):
    e = number//4
    q = number%4
    if number == 0:
        return '0'
    elif e == 0:
        return str(q)
    else:
        return to_quaternary(e) + str(q)

if __name__=='__main__':
    print(get_medals(score))