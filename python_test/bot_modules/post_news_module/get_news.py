
import random
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from dateutil.parser import parse


def secure_lab_news ():
    today = datetime.today().date()

    secur_lab_news_url = 'https://www.securitylab.ru/_services/export/rss/news/'
    secur_lab_vul_url = 'https://www.securitylab.ru/_services/export/rss/vulnerabilities/'

    news_resp = requests.get(secur_lab_news_url) 
    vul_resp = requests.get(secur_lab_vul_url) 

    news_msgs = BeautifulSoup (news_resp.content ,  'lxml').find_all('item')
    vul_msgs = BeautifulSoup (vul_resp.content ,  'lxml').find_all('item')
    

    todays_news_post = [[msg.title.text,msg.guid.text]  for msg in news_msgs 
                            if parse(msg.pubdate.text).date() == today ]
    todays_vul_post = [[msg.title.text,msg.link.next_sibling]  for msg in vul_msgs 
                            if parse(msg.pubdate.text).date() == today ]
    
    # print(vul_msgs.link.next_sibling)
    # msg = [msg.find ('title') for msg in msges]
    return [random.choice(todays_news_post), random.choice(todays_vul_post)]



if __name__ == '__main__':
    print(secure_lab_news())