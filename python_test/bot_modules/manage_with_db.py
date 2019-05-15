import psycopg2


    
def get_score ():
    connect = psycopg2.connect( host='157.230.108.47' ,dbname ="base_datos", user="admin", password="secret", port = '5432')
    cur = connect.cursor()
    cur.execute(''' select "level" from "userApp_userprogress" where user_id = 1 ''')
    score=cur.fetchall()
    cur.close()
    connect.close()
    return score[0][0]


        

if __name__ == '__main__':
    print(type(get_score()))