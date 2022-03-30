import tweepy
import time
from textblob import TextBlob
import pandas as pd
import numpy as np
import tweets

tweets.search_tweets("apple", 10, "")

# import data from csv file called 'data.csv' and store it in a dataframe
df = pd.read_csv('data.csv')

# print dataframe df
print(df)

# import the tweet.py file


# loop through each tweet to analyse the text in the text column to find the sentiment
for index, row in df.iterrows():
    # print the text of the tweet
    
    # create a TextBlob object of the tweet's text
    analysis = TextBlob(row['text'])
    # set the sentiment of the tweet to the TextBlob's sentiment
    df.at[index, 'sentiment'] = analysis.sentiment.polarity
    # print the polarity of the tweet
    print(analysis.sentiment.polarity)
    # wait for 15 seconds
    time.sleep(5)