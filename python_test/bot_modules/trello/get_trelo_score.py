"""Module to connect and get data from trello"""
from datetime import datetime
import trello
import os

TRELLO_TOKEN = os.environ["MLP_TRELLO_TOKEN"]
TRELLP_API_KEY = os.environ["MLP_TRELLO_KEY"]
board_id = "5d20bcbae31b1447ce242dd4"

def get_cards_from_list(list_):
    return (list_['name'],trello.Lists(TRELLP_API_KEY,token=TRELLO_TOKEN).get_card(list_['id']))

def get_member_name(ids):
    members = trello.Cards(TRELLP_API_KEY,token=TRELLO_TOKEN).get_member(ids)
    return [dic['fullName'] for dic in members] if members else None

def get_card_actions(card):
    actions = trello.Cards(TRELLP_API_KEY,token=TRELLO_TOKEN).get_action(card)
    return actions

def time_from_card_id(card_id:str):
    return datetime.fromtimestamp(int(card_id[0:8],16))

def get_trello_data():
    lists = trello.Boards(TRELLP_API_KEY,token=TRELLO_TOKEN).get_list(board_id)
    cards_by_list = [get_cards_from_list(list_) for list_ in lists if list_['name']!='Assets']
    cards = [(lis[0],car['name'],{'time_start':str(time_from_card_id(car['id'])),'time_close':car['due'],'who':get_member_name( car['id'])}) 
                    for lis in cards_by_list for car in lis[1]]

    # for i in  cards_by_list[-1][1][0].items():
    #     print(i)

    # print(cards_by_list[-1][1][0]['id'])
    
    # for i in get_card_actions(cards_by_list[-1][1][0]['id'])[0].items():
    #     print(i,'\n')
    # print(type(cards_by_list[-1][1]))
    return cards
# for lisn lis

    
# print(trello.TrelloApi(TRELLP_API_KEY).get_token_url('MLP', expires='30days', write_access=False))
if __name__ == "__main__":
    print(get_trello_data())
    # get_trello_data()