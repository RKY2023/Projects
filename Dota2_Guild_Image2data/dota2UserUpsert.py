import requests
import json
import pandas as pd
import pymysql as ps
from datetime import datetime

response_API = requests.get('https://api.opendota.com/api/players/30535439')
print(response_API.status_code)
data = response_API.text
parse_json = json.loads(data)

user_summary = []

user_profile = pd.json_normalize(parse_json['profile'],max_level=2)
parse_json.pop('profile')
parse_json['mmr_estimate'] = parse_json['mmr_estimate']['estimate']
user_otherInfo = pd.json_normalize(parse_json)
user_all = pd.concat([ user_profile, user_otherInfo], axis=1)
print(user_all)

try:
    cn=ps.connect(host='localhost',port=3306,user='root',password='2023',db='dota2')
    cmd=cn.cursor()
    for i,row in user_all.iterrows():
        #here %S means string values 
        sql = "INSERT INTO dota2.user(account_id, personaname, name, plus, cheese, steamid, avatar,avatarmedium, avatarfull, profileurl, lastlogin, loccountrycode, is_contributor, tracked_until, solo_competitive_rank, competitve_rank, rank_tier, leaderboard_rank, mmr_estimate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cmd.execute(sql, tuple(row))
        print("Record inserted")
        # the connection is not auto committed by default, so we must commit to save our changes
        cn.commit()
    # query="select * from guild_scrapped"
    
    # cmd.execute(query)
    
    # rows=cmd.fetchall()
    
    # # print(rows)
    # for row in rows:
    #     for col in row:
    #         print(col,end=' ')
    #     print()
    
    cn.close()

except Exception as e:
    print(e)
