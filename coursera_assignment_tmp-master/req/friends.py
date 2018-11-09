import requests
import json
import datetime
import numpy as np
import pandas as pd
from dateutil.relativedelta import relativedelta


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
        friend_df = pd.DataFrame(friends_list)
        BD_column = friend_df.bdate.dropna(axis=0)
        BD_column = pd.to_datetime(BD_column, format='%d.%m.%Y', errors='coerce').dropna(axis=0)
        age = pd.DataFrame({'age': cur_year-BD_column.dt.year})
        fin_df = age.groupby('age').size().reset_index(name='counts').sort_values(by=['counts', 'age'],
                                                                                  ascending=[False, True])
        age_json = fin_df.to_json(orient='records')

    return age_json


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
    res = calc_age('medoeje')
    print(res)
