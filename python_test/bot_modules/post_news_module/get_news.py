
import random
import requests
from datetime import datetime,timedelta
from bs4 import BeautifulSoup
from dateutil.parser import parse


def secure_lab_news ():
    """Get posts from Security Lab and return two random news in a discored message format"""
    today = datetime.today().date()

    secur_lab_news_url = 'https://www.securitylab.ru/_services/export/rss/news/'
    secur_lab_vul_url = 'https://www.securitylab.ru/_services/export/rss/vulnerabilities/'

    news_resp = requests.get(secur_lab_news_url) 
    vul_resp = requests.get(secur_lab_vul_url) 

    news_msgs = BeautifulSoup (news_resp.content ,  'lxml').find_all('item')
    vul_msgs = BeautifulSoup (vul_resp.content ,  'lxml').find_all('item')
    

    todays_news_post = [[msg.title.text,msg.guid.text] for msg in news_msgs 
                            if parse(msg.pubdate.text).date() == today  ]
    todays_vul_post = [[msg.title.text,msg.link.next_sibling ] for msg in vul_msgs 
                            if parse(msg.pubdate.text).date() == today ]
    #print(todays_news_post,todays_vul_post)
    one_news = [random.choice(i) for i in [todays_news_post,todays_vul_post] if i  ]
    if one_news:
        line  =['\n'.join(i) for i in one_news]
        res = 'Пара новостей Security lab на сегодня\n'+'\n'.join (line) 
    else:
        res = 'Похоже на сегодня новостей еще не набралось'
    
    return res

def habr_news ():
    """Get today's top posts from Habr and return two random news in a discored message format"""
    habr_top_daily_post = 'https://habr.com/ru/rss/best/daily/?fl=ru'
    resp = requests.get(habr_top_daily_post)
    all_posts = BeautifulSoup (resp.content , 'lxml').find_all('item')
    random_post = random.choice(all_posts)
    mes = random_post.link.next_sibling

    return 'Одна из интересных статей Хабра на сегодня\n' + mes

def tproger_news():
    today = datetime.today().date()

    tprog_news_link = 'https://tproger.ru/feed/'
    resp = requests.get(tprog_news_link)
    tprog_news = BeautifulSoup(resp.content , 'lxml').find_all('item')
    
    tprog_todays_news = [[msg.title.text,msg.guid.text] for msg in tprog_news 
                            if parse(msg.pubdate.text).date() == today  ]
    
    if tprog_todays_news:
        msg = 'Новости с Tproger за сегодня\n'+ '\n'.join(random.choice(tprog_todays_news))
    else:
        msg = 'Похоже на сегодня нет достойных новостей'
    return msg

if __name__ == '__main__':
    print(tproger_news())