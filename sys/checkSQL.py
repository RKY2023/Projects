import requests
import json
import pandas as pd
import pymysql as ps
from datetime import datetime


def checkFetch():
    try:
        cn=ps.connect(host='localhost',port=3306,user='root',password='2023',db='dota2')
        cmd=cn.cursor()
        # for i,row in guild_summary.iterrows():
        #     #here %S means string values 
        #     sql = "INSERT INTO dota2.guild_info(guild_name, guild_tag, created_timestamp  , guild_language, guild_flags, guild_logo, guild_region, guild_chat_group_id , guild_description , default_chat_channel_id , guild_primary_color , guild_secondary_color  , guild_pattern, guild_refresh_time_offset, guild_required_rank_tier, guild_motd_timestamp, guild_motd, event_id, guild_points, guild_weekly_rank, guild_weekly_percentile, guild_current_percentile, guild_id, guild_member_count) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        #     cmd.execute(sql, tuple(row))
        #     print("Record inserted")
        #     # the connection is not auto committed by default, so we must commit to save our changes
        #     cn.commit()

        #here %S means string values 
        sql = "SELECT * FROM dota2.guild_scrapped"
        tuplescount = cmd.execute(sql)
        tuples = cmd.fetchall()
        print("Record Found:",tuplescount)
        for row in tuples:
            print(row)
        
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
checkFetch()