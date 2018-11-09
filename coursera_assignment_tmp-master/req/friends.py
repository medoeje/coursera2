import requests
import json
import datetime
import numpy as np
import pandas as pd


ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'
now = datetime.datetime.now()
cur_year = now.year

def calc_age(uid):
    uid = get_user_id(uid)
    if uid:
        get_friends_info_url = 'https://api.vk.com/method/friends.get?v=5.71'
        params = {'user_id': uid, 'access_token': ACCESS_TOKEN, 'fields': 'bdate'}
        r = requests.get(get_friends_info_url, params=params).json()
        friends_list = r.get('response').get('items')
    return friends_list


def get_user_id(user_id):
    get_user_id_url = 'https://api.vk.com/method/users.get?v=5.71'
    params = {'user_ids': user_id, 'access_token': ACCESS_TOKEN}
    r = requests.get(get_user_id_url, params=params).json()
    if r.get('response'):
        uid = r.get('response')[0].get('id')
    else:
        uid = None
    return uid
   # print(r.text)

if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
