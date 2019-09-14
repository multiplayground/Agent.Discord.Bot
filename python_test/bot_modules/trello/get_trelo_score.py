"""Module to connect and get data from trello"""
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


def get_trello_data():
    lists = trello.Boards(TRELLP_API_KEY,token=TRELLO_TOKEN).get_list(board_id)
    cards_by_list = [get_cards_from_list(list_) for list_ in lists if list_['name']!='Assets']
    cards = [(lis[0],car['name'],{'time_start':car['dateLastActivity'],'time_close':car['due'],'who':get_member_name( car['id'])}) 
                    for lis in cards_by_list for car in lis[1]]
    return cards
# for lisn lis

    
# print(trello.TrelloApi(TRELLP_API_KEY).get_token_url('MLP', expires='30days', write_access=False))
 