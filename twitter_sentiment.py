import tweepy
from textblob import TextBlob
import csv
import re
import sys
import pandas as pd

consumer_key='K2WHQjH2yCbAWQKXY8IUAQd5T'
consumer_secret='7RvSNposUestR34zV4rAhlKLtml1tlux9ZhGSp3WomIf2Kvpbi'

access_token_key='2259461466-81b4w4XsR9KnvQHulWxPWswbfMMbe8CG2CbtR0U'
access_token_secret='7G8KwAbt2kPoQneG3I4kLMBMTJ8MBftXRCLG1NaQ1MlYK'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token_key,access_token_secret)

api=tweepy.API(auth)
topicname='Soccer'
pubic_tweets=api.search(topicname)
unwanted_words=['@','RT',':','https','http']
symbols=['@','#']
data=[]
for tweet in pubic_tweets:
    text=tweet.text
    textWords=text.split()
    #print (textWords)
    cleanedTweet=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(RT)", " ", text).split())
    print (cleanedTweet)
    #print (TextBlob(cleanedTweet).tags)
    analysis= TextBlob(cleanedTweet)
    print (analysis.sentiment)
    polarity = 'Positive'
    if(analysis.sentiment.polarity < 0):
        polarity = 'Negative'
    if(0<=analysis.sentiment.polarity <=0.2):
        polarity = 'Neutral'
    #print (polarity)
    dic={}
    dic['Sentiment']=polarity
    dic['Tweet']=cleanedTweet
    data.append(dic)
df=pd.DataFrame(data)
df.to_csv('analysis1.csv')
