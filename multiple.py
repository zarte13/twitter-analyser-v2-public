from time import sleep
import tweets
import tweepy
import json
import pandas as pd
import re






def search_multiple(query,token, start, end):
    dates = pd.date_range(start=start, end=end, freq="8h")
    for i in range(len(dates)-1):
        datestart=dates[i].isoformat('T')+"Z"
        dateend=dates[i+1].isoformat('T')+"Z"
        print(datestart)
        tweets.search_tweets(query, 100, token, datestart, dateend)
        sleep(1)



