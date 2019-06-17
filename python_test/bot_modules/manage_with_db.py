import psycopg2
import  bot_modules.settings as se


    
def get_score (name):
    try:
        name_=str(name)
        connect = psycopg2.connect( host=se.db_host ,dbname =se.db, user=se.db_log, 
                                    password=se.db_pass, port = '5432')
        cur = connect.cursor()
        cur.execute(f''' select "level" from "userApp_userprogress" where user_id  = 
                        (select id from "userApp_user" where "login" = '{name_}') ''')
        score=cur.fetchone()
        cur.close()
        connect.close()
        
        return score[0]
    except:
        return 'error'

def set_score(name,level):
    name_=str(name)
    if 0 <= level <= 32767:
        
        connect = psycopg2.connect( host=se.db_host ,dbname =se.db, user=se.db_log, 
                                password=se.db_pass, port = '5432')
        cur = connect.cursor()
        print('===works===',level)
        cur.execute(f''' update  "userApp_userprogress" set  "level" = {level} where id = 
                        (select id from "userApp_user" where "login" = '{name_}') ''')
        connect.commit()
        cur.close()
        connect.close()

        

if __name__ == '__main__':
    set_score('AlTheOne',587)
    temp=get_score('AlTheOne')
    print(temp)
    print(type(temp))