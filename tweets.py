#Import the necessary methods from tweepy library

from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import json
import pandas as pd
import re

#Variables that contains the user credentials to access Twitter API 
#very cool






def search_tweets(query, count, token):



    client = tweepy.Client(bearer_token=token) #initiation du api

    response = client.search_recent_tweets(query="%s -is:retweet"%query, max_results=count, expansions=["author_id"], tweet_fields=["public_metrics","created_at"]) #aller chercher les tweets



    tweets = response.data #transformer les tweets

    author_ids = []
    creation_date = []
    usernames = []
    likes = []
    retweets = []
    replies = []
    text = []


    for tweet in tweets:
        likes.append(tweet.public_metrics["like_count"])
        retweets.append(tweet.public_metrics["retweet_count"]+tweet.public_metrics["quote_count"])
        replies.append(tweet.public_metrics["reply_count"])
        author_ids.append(tweet.author_id)
        creation_date.append(tweet.created_at)
        text.append(tweet.text)

    response_user = client.get_users(ids=author_ids)

    users = response_user.data

    for user in users:
        usernames.append(user.username)



    df = pd.DataFrame()
    df["author_id"] =  author_ids
    df["username"] = usernames
    df["date"] = creation_date
    df["likes"] = likes
    df["retweets"] = retweets
    df["reply count"] = replies
    df["text"] = text


    df.to_csv(r'data.csv')
