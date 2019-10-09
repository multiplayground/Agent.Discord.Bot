"""Module to connect and get data from trello using trello module"""
from datetime import datetime
import trello
import os

# Set propriate variables to connect to trello
TRELLO_TOKEN = os.environ["MLP_TRELLO_TOKEN"]
TRELLP_API_KEY = os.environ["MLP_TRELLO_KEY"]
board_id = "5d20bcbae31b1447ce242dd4"

def get_cards_from_list(list_):
    '''
        Get all card from given list
    '''
    return (list_['name'],trello.Lists(TRELLP_API_KEY,token=TRELLO_TOKEN).get_card(list_['id']))

def get_member_name(ids):
    '''
    Estemate the members of the card by id'''
    members = trello.Cards(TRELLP_API_KEY,token=TRELLO_TOKEN).get_member(ids)
    return [dic['fullName'] for dic in members] if members else None

def get_card_actions(card):
    '''
    Check if card was transfered to 'Done' list with last action'''

    actions = trello.Cards(TRELLP_API_KEY,token=TRELLO_TOKEN).get_action(card)
    if actions and actions[0]['data']['listAfter']['name'] == 'Done':
        return actions[0]['date']
    return None

def time_from_card_id(card_id:str):
    '''
    Get timve when card was created'''

    # to find the created time (in Unix epoch) it's need to convert first 8 digits of card id to integer
    return datetime.fromtimestamp(int(card_id[0:8],16))


def extract_label(card):
    '''
    Check if card has a lebal and return string with it'''

    if card['labels']:
        return card['labels'][0]['name']


def get_trello_data():
    '''
    Request to trello to get nedeed data'''

    # At firs get lists of cards
    lists = trello.Boards(TRELLP_API_KEY,token=TRELLO_TOKEN).get_list(board_id)
    # Form list of cards w.r.t list ignoring Accets list
    cards_by_list = [get_cards_from_list(list_) for list_ in lists if list_['name']!='Assets']

    # print(cards_by_list[-1][1][0]['labels'][0]['name'])

    cards = [(lis[0],
            car['name'],
                {'time_start':str(time_from_card_id(car['id'])),
                'time_close':get_card_actions(car['id']),
                'who':get_member_name( car['id']),
                'label':extract_label(car)}) 
                    for lis in cards_by_list 
                    for car in lis[1]]



    return cards
    
if __name__ == "__main__":
    print(get_trello_data())
    # get_trello_data()