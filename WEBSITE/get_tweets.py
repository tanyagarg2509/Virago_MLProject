import tweepy
import time
import pandas as pd
pd.set_option('display.max_colwidth', 1000)

# api key
consumer_key = 'Tan0zgQRjQxjyubOPCbERip1p'
consumer_secret = 'Rcjd0sID7brrcH682RVDFNjc8yxBuEHI6Kq5PQlhVPiskVi6ri'
access_token = '261123310-nhpBB26oASCDw2HdQA7Hoxui7f0jpMaPOr068b9W'
access_token_secret = 'gWQ41E4bfc4EalWnnWv147NeoCDkwo2cadKJFtIbTVy0z'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
def get_related_tweets(text_query):
    # list to store tweets
    tweets_list = []
    # no of tweets
    count = 30
    try:
        # Pulling individual tweets from query
        for tweet in api.search(q=text_query, count=count):
            print(tweet.text)
            # Adding to list that contains all tweets
            tweets_list.append({'tweet_text': tweet.text})
        return pd.DataFrame.from_dict(tweets_list)

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)