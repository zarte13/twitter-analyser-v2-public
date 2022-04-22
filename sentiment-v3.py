import tweepy
import time
from textblob import TextBlob, WordList
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer
from scipy.special import softmax
import urllib.request
import csv


#import tweets
#tweets.search_tweets("economy crash", 10, "AAAAAAAAAAAAAAAAAAAAAF53aAEAAAAAMK2lMWsNnCylxLEs%2BofhwxOMXDw%3D8cUv4aDoALTRfp5n8XUpp4QBySI7nQVR1S3BVsEOPHneAMgi1j")

def preprocess(text):
    new_text = []
 
 
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)



task='sentiment'
MODEL = f"cardiffnlp/twitter-roberta-base-{task}"

tokenizer = AutoTokenizer.from_pretrained(MODEL)

# download label mapping
labels=[]
mapping_link = f"https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/{task}/mapping.txt"
with urllib.request.urlopen(mapping_link) as f:
    html = f.read().decode('utf-8').split("\n")
    csvreader = csv.reader(html, delimiter='\t')
labels = [row[1] for row in csvreader if len(row) > 1]

model = AutoModelForSequenceClassification.from_pretrained(MODEL)
model.save_pretrained(MODEL)

# import data from csv file called 'data.csv' and store it in a dataframe
df = pd.read_csv('data.csv')

ps = PorterStemmer()
# print dataframe df
# print(df)
def isNaN(string):
    return string != string

def stats(arr):
    if arr[0] > arr[2]:
        if arr[0] > arr[1]:
            return -arr[0]
        else:
            return 0    
    elif arr[0] < arr[2]:
        if arr[2] > arr[1]:
            return arr[2]
        else:
            return 0

def stats_no_neutral(arr):
    if arr[0] > arr[2]:
        return -arr[0]
    elif arr[0] < arr[2]:
        return arr[2]
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
         
        text = row['text']
        encoded_input = tokenizer(text, return_tensors='pt')
        output = model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        ranking = np.argsort(scores)
        ranking = ranking[::-1]
        print(scores)
        print(stats(scores))
        df.at[index, 'sentiment'] = stats(scores)
        

        
        # for i in range(scores.shape[0]):
        #     l = labels[ranking[i]]
        #     s = scores[ranking[i]]
        #     
        #     print(f"{i+1}) {l} {np.round(float(s), 4)}")
        words = word_tokenize(row['text'])
        
        for word in words:
            analysis = TextBlob(word)
            
            text = ps.stem(word)
            encoded_input = tokenizer(text, return_tensors='pt')
            output = model(**encoded_input)
            scores = output[0][0].detach().numpy()
            scores = softmax(scores)
            ranking = np.argsort(scores)
            ranking = ranking[::-1]
            wordlistz.at[text, 'sentiment'] = stats_no_neutral(scores)
            # for i in range(scores.shape[0]):
            #     l = labels[ranking[i]]
            #     s = scores[ranking[i]]
            #     wordlistz.at[word, 'sentiment'] = s



        
            
        

           
           

print(wordlistz)
print(df)

df.to_csv(r'v3tweetsentiment.csv')
wordlistz.to_csv(r'v3wordsentiment.csv')

    
    
    # loop through each word in the tweet
    
    # print the word list
    # print(row["text"])

    
    # print the polarity of the tweet
    # print(analysis.sentiment.polarity)
    # wait for 15 seconds
    # time.sleep(5)
# find the most common words in all the tweets

