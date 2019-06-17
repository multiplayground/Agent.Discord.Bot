from  .manage_with_db import *

def get_user_level (name):
    score = get_score(name)
    if score =='error':
        return score
    return (get_level(score))
    

def get_level(score):
    return 1 + get_level(score-50) if score>140 else l_level(score)


def l_level(score):
    if score ==0:
        return 0
    x=0
    y=1
    level=1
    while x <35:
        x+=5
        y+=x
        if score<y:
            return level
        level+=1