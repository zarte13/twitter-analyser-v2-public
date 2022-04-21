import tweepy
import time
from textblob import TextBlob
import pandas as pd
import numpy as np
import tweets

tweets.search_tweets("apple", 10, "AAAAAAAAAAAAAAAAAAAAAF53aAEAAAAAMK2lMWsNnCylxLEs%2BofhwxOMXDw%3D8cUv4aDoALTRfp5n8XUpp4QBySI7nQVR1S3BVsEOPHneAMgi1j")

# import data from csv file called 'data.csv' and store it in a dataframe
df = pd.read_csv('data.csv')

# print dataframe df
print(df)

# import the tweet.py file

wordlist = pd.DataFrame()

# loop through each tweet to analyse the text in the text column to find the sentiment
for index, row in df.iterrows():
    # print the text of the tweet
    
    # create a TextBlob object of the tweet's text
    analysis = TextBlob(row['text'])
    # set the sentiment of the tweet to the TextBlob's sentiment
    df.at[index, 'sentiment'] = analysis.sentiment.polarity
    # create a list of all the words in the tweet
    words = row['text'].split()
    # loop through each word in the tweet
    for word in words:
        # count each word in the tweet
        wordlist.at[word] = wordlist.at[word] + 1
    # print the word list
    print(wordlist)

    
    # print the polarity of the tweet
    print(analysis.sentiment.polarity)
    # wait for 15 seconds
    time.sleep(5)
# find the most common words in all the tweets

