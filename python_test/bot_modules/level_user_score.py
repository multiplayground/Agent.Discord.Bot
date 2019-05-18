from  .manage_with_db import *

def get_user_level (name):
    level = get_score(name)
    if level == 'something wrong':
        return 'Похоже такого пользователя еще нет в нашем списке'
    if level < 1:
        return 0
    elif level < 6:
        return 1
    elif level < 16:
        return 2
    elif level < 31:
        return 3
    elif level < 51:
        return 4
    elif level < 76:
        return 5
    elif level < 106:
        return 6
    elif level < 141:
        return 7
    elif level < 191:
        return 8
    else:
        return 'more than 8'