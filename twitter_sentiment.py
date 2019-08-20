# pip install tweepy
# pip install textblob
# python
# import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

#quick test on console
# from textblob import TextBlob
# wiki = TextBlob('Roman is resally happy with his wife and son')
# wiki.tags
# wiki.words
# wiki.sentiment.polarity

import tweepy

from textblob import TextBlob

consumer_key = 'FwylcmbAkPps41eNe1bMyVM8O'
consumer_secret = 'UIsWvshSKEd1cxuf0yjBscUmfIZoTrftHR3sLAtkm8Qqw7SikC'

access_token = '374021276-Cevi4EaxSp0VV1tqxgtspRsXuDltBd3GMtXJrjNm'
access_token_secret = 'ojMBhnUkLxcIrPmyLTaciRSHtlkBjlfYJHRqF8PdTSdy6'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)