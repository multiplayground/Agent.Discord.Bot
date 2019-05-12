from itertools import repeat
score ='100001321'
medals ={':scientist:':'100000000',':devops:':'10000000' ,':master:' :'1000000',
        ':diamond:':'100000' ,':platinum:':'10000' ,':gold:':'1000', 
        ':silver:':'100', ':bronze:':'10' ,':unranked:':'1' }



def get_medals(score='111111111'):
    if len(score)==9:
        res=[]
        for i,j in zip(score,medals):
            res.extend(repeat(j,int(i)))
    return res
        

def add_medal(score,medal):
    if len(score)==9:
        dec_sum=int(score,4)+int(medals[medal],4)
        if dec_sum > 262143
            return to_quaternary(262143)
        return to_quaternary(dec_sum)

def subtracct_medal(score,medal):
    if len(score)==9:
        dec_sum=int(score,4)-int(medals[medal],4)
        if dec_sum < 0
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