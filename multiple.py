from time import sleep
import tweets
import tweepy
import json
import pandas as pd
import re
import os, os.path
from os import path







def search_multiple(query,token, start, end):
    daydates = pd.date_range(start=start, end=end, freq="1D")
    for j in range(len(daydates)-1):
        df1 = pd.DataFrame()
        if path.exists("datafull.csv"):
            df1 = pd.read_csv(r'datafull.csv')
        
        dates = pd.date_range(start=daydates[j], periods=6, freq="4h")
        if path.exists("data4h.csv"):
            os.remove("data4h.csv")

        for i in range(len(dates)):
            df2 = pd.DataFrame()
            if path.exists("data4h.csv"):
                df2 = pd.read_csv(r'data4h.csv')
            
            datestart=dates[i].isoformat('T')+"Z"
            dateend=dates[i+1].isoformat('T')+"Z"
            print(datestart)
            tweets.search_tweets(query, 100, token, datestart, dateend)
            #sleep(1)
            
            rawdata = pd.read_csv(r'data.csv')
            
            if not df2.empty:
                df2 = pd.concat([rawdata,df2])
            else:
                df2 = rawdata
            df2 = df2.loc[:, ~df2.columns.str.contains('^Unnamed')]
            df2.to_csv(r'data4h.csv', index=False)
        df2.to_csv("daytweets/date-day-%s.csv"%j, index=False)
        fourhourdata = pd.read_csv(r'data4h.csv')
        if not df1.empty:
            df1 = pd.concat([fourhourdata,df1])
        else:
            df1 = fourhourdata
        df1 = df1.loc[:, ~df1.columns.str.contains('^Unnamed')]
        df1.to_csv(r'datafull.csv', index=False)

# token = ""
#token = r""
#search_multiple("gold",token,"2022-05-15 00:00:00", "2022-05-19")




