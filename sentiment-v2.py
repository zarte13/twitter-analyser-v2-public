import tweepy
import time
from textblob import TextBlob, WordList
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


import multiple
#multiple.search_multiple("economy crash", "", "2022-05-14", "2022-05-15" )

# import data from csv file called 'data.csv' and store it in a dataframe
df = pd.read_csv('data.csv')

ps = PorterStemmer()
# print dataframe df
# print(df)
def isNaN(string):
    return string != string

# import the tweet.py file

wordlistz = pd.DataFrame()

# loop through each tweet to analyse the text in the text column to find the sentiment
for index, row in df.iterrows():
    # print the text of the tweet
    
    # create a TextBlob object of the tweet's text
    
    # set the sentiment of the tweet to the TextBlob's sentiment
    
    # create a list of all the words in the tweet

    if not isNaN(row['text']):
        analysis = TextBlob(row['text'])
        df.at[index, 'sentiment'] = analysis.sentiment.polarity
        words = word_tokenize(row['text'])
        print(row['text'])
        print(words)
        break
        for word in words:
            analysis = TextBlob(word)
            
            word = ps.stem(word)
            
            if word in wordlistz.index:
                wordlistz.at[word, "wordcount"] += 1
            else:
                wordlistz.at[word, "wordcount" ] = 1
            wordlistz.at[word, 'sentiment'] = analysis.sentiment.polarity
            
        

           
           
print(wordlistz)
print(df)

df.to_csv(r'tweetsentiment.csv')
wordlistz.to_csv(r'wordsentiment.csv')
    
    
    # loop through each word in the tweet
    
    # print the word list
    # print(row["text"])

    
    # print the polarity of the tweet
    # print(analysis.sentiment.polarity)
    # wait for 15 seconds
    # time.sleep(5)
# find the most common words in all the tweets

