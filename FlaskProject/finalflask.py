#import required libraries
import pandas as import pd
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, TfidVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import pipeline
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split

#read the dataset
data=pd.read_csv('dataset/twitter_sentiments.csv')
#view the top rows
data.head()
 #dataset having tweet, id and label

 #train test splot, 20% for testing
 train,test=train_test_split(data,test_size=0.2,stratify=data['label'],random_state=21)
 #get the shape of train and test train_test_split
 train.shape,test.shape

 #create a TF_IDF vectorizer object
 tfidf_vectorizer = TfidVectorizer(lowercase=True, max_features=1000,stop_words=ENGLISH_STOP_WORDS)
 #fit the object with the training data tweets
 tfidf_vectorizer.fit(train.tweet)

 #transform the train and test data
 train_idf = tfidf_vectorizer.transform(train.tweet)
 test_idf = tfidf_vectorizer.transform(test.tweet)

 #create object of linear regression model
 model_LR = LogisticRegression()
 #fit the model with training data
 model_LR.fit(train_idf,train.label) #dataset has label as column heading
 #predict the label on the training data
 predict_train = model_LR.predict(train_idf)
 #predict the model on the test data
 predict_test = model_LR.predict(test_idf)
 #f1 score on train data
 f1_score(y_true=train.label,y_pred=predict_train)
 #f1 score on test data
 f1_score(y_true = test.label, y_pred=predict_test)


 #define the stages of the pipeline
 pipeline = Pipeline(steps=[('tfidf',TfidVectorizer(lowercase=True,max_features=1000,stop_words=ENGLISH_STOP_WORDS)),('model',LogisticRegression())])
 #fit the pipeline model with the training data
 pipeline.fit(train.tweet,train.label)

 #sample tweet
 text=["Jumbo is a bitchy movie"]
 #predict the label using the pipeline
 pipeline.predict(text)


 #saving pipeline using joblib library
 from joblib import dump
 #dump the pipeline model
 dump(pipeline, filename="text_classification.joblib")

 #using the saved model
 from joblib import load
 #sample tweet text
 text = ["Jumbo is a bitchy movie"]
 #load the saved pipeline mode
 pipeline = load("text_classification.joblib")
 #predict on the sample tweet text
 pipeline.predict(text)

 #scraping tweets from twitter
 import tweepy
 import time
 import pandas as pd
 pd.set_option('display.max_colwidth',1000)

 #keys
 api_key = ''
 api_secret_key = ''
 access_token = ''
 access_token_secret = ''
#authorize the API key
authentication = tweepy.OAuthHandler(api_key,api_secret_key)
#authorization to user's access token and access token secret
authentication.set_access_token(access_token,access_token_secret)
#call the API
api = tweepy.API(authentication,wait_on_rate_limit=True)

#scraping the tweets related to the keyword
def get_related_tweets() 
