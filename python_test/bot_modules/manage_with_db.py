import psycopg2

class User_Reward:
    cur= None
    def __init__ (self):
        global cur 
        self.connect = psycopg2.connect(host="157.230.108.47",database="AlTheOne", user="AlTheOne", password="pgpass")
        cur = self.connect.cursor()
        print("i'm created")
    

    def get_all_medals(self):
        self.cur.execute('''select * from test_reward_tbl''')
        self.all_tabl = cur.fetchall()
        self.cur.close()
        return self.all_tabl

