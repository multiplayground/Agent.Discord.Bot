import psycopg2

class User_Reward:
    cur= None
    def __init__ (self):
        global cur 
        self.connect = psycopg2.connect(host="157.230.108.47",database="base_datos", user="admin", password="secret")
        cur = self.connect.cursor()
        print("i'm created")
    

    def get_all_medals(self):
        self.cur.execute('''select * from test_reward_tbl''')
        self.all_tabl = cur.fetchall()
        self.cur.close()
        return self.all_tabl

if __name__ == '__main__':
    base=User_Reward()
    print(base.get_all_medals())
