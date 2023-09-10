import requests
import json
import pandas as pd
import pymysql as ps
from datetime import datetime

response_API = requests.get('https://www.dota2.com/webapi/IDOTA2Guild/FindGuildByTag/v0001/?tag=DTGS')
print(response_API.status_code)
data = response_API.text
parse_json = json.loads(data)

guild_summary = []

guild_info = pd.json_normalize(parse_json['found_guild']['guild_summary']['guild_info'],max_level=2)
guild_id = parse_json['found_guild']['guild_id']
guild_member_count = parse_json['found_guild']['guild_summary']['member_count']
# guild_info = guild_info.drop(columns="event_points")
guild_event_points = pd.json_normalize(parse_json['found_guild']['guild_summary']['event_points'],max_level=1)

guild_summary = pd.concat([ guild_info, guild_event_points], axis=1)
guild_summary['guild_id'] = guild_id
guild_summary['guild_member_count'] = guild_member_count


timestamp = guild_summary['created_timestamp'][0]
dt_object = datetime.fromtimestamp(timestamp)
guild_summary['created_timestamp'][0] = dt_object
print(guild_summary)
# exit()

try:
    cn=ps.connect(host='localhost',port=3306,user='root',password='2023',db='dota2')
    cmd=cn.cursor()
    for i,row in guild_summary.iterrows():
        #here %S means string values 
        sql = "INSERT INTO dota2.guild_info(guild_name, guild_tag, created_timestamp  , guild_language, guild_flags, guild_logo, guild_region, guild_chat_group_id , guild_description , default_chat_channel_id , guild_primary_color , guild_secondary_color  , guild_pattern, guild_refresh_time_offset, guild_required_rank_tier, guild_motd_timestamp, guild_motd, event_id, guild_points, guild_weekly_rank, guild_weekly_percentile, guild_current_percentile, guild_id, guild_member_count) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
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



# guild_id
# guild_member_count
# guild_name
# guild_tag
# created_timestamp        
# guild_language
# guild_flags
# guild_logo
# guild_region
# guild_chat_group_id      
# guild_description        
# default_chat_channel_id  
# guild_primary_color      
# guild_secondary_color    
# guild_pattern
# guild_refresh_time_offset
# guild_required_rank_tier 
# guild_motd_timestamp     
# guild_motd
# event_id
# guild_points
# guild_weekly_rank
# guild_weekly_percentile
# guild_current_percentile