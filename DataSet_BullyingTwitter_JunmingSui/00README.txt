Bullying Traces v3.0
Visit bullying research project at http://research.cs.wisc.edu/bullying/

*****************************************************************************
What's new in v3.0 (Released June 2015)

1. We annotated more tweets collected during August 7-31, 2011. Together with the 1,732
annotated tweets collected on August 6, 2011 in previous versions, we have 7,321 annotated 
tweets in total.

2. We added more annotated categories. Besides the NLP tasks A-C (bullying 
trace or not, author's role, teasing) in our NAACL'12 paper, if a tweet is annotated 
as a bullying trace, we also included the annotations for its type, form, and emotion.

3. The vocabulary and Bag-of-Words vectors are different from previous version, 
as we have significantly more tweets in this version of the data set.

4. A python script getTweets.py is provided to download the tweet JSON objects 
(including tweet texts and meta-data) from Twitter API. You have to sign up for a Twitter account 
and apply for access tokens from Twitter.  Alternatively, a quick way to inspect a tweet is 
via the URL https://twitter.com/statuses/TweetID.  Due to the nature of Twitter, one should 
expect that some tweets are no longer retrievable because the tweet authors may have deleted them.

*****************************************************************************
Original notes

This dataset contains data collected from Twitter stream API and labeled by 
experienced annotators for the study of bullying in social media.  We 
collected tweets using the public Twitter stream API, such that each tweet 
contains at least one of the following keywords: "bully, bullied, bullying". 
We further removed re-tweets by excluding tweets containing the acronym "RT." 
The tweets are cased-folded and tokenized, but without any stemming or stopword removal. 
Any user mentions preceded by a ``@'' were replaced by the anonymized user name ``@USERNAME''. 
Any URLs starting with ``http'' were replaced by the token ``HTTPLINK''. 
Hashtags (compound words following ``#'') were not split and were treated as 
a single token. Emoticons, such as ``:)'' or ``:D'', were also included as 
tokens. Our features include both unigrams and bigrams that appear at least 
twice in the tweets. 


----------------------------------Content----------------------------------

data.csv
	This contains the tweet ids, which is useful to retrieve tweets from 
	Twitter APIs. Each line corresponds to one tweet and has seven fields 
	separated by commas:
	Tweet ID, User ID, Bullying_Traces?, Type, Form, Teasing?, Author_Role, Emotion

	The possible values for Bullying_Traces?: 
		y (bullying trace) 
		n (not a bullying trace)
	The possible values for Type: 
		accusation
		cyberbullying
		denial
		report
		self-disclosure
		NA - The tweet is not a bullying trace and we didn't annotate its type
	The possible values for Form: 
		cyberbullying
		other
		physical
		property damage
		relational
		verbal
		NA - The tweet is not a bullying trace and we didn't annotate its form
	The possible values for Teasing?
		y - Teasing
		n - Not teasing
		NA - The tweet is not a bullying trace and we didn't annotate if it is teasing
	The possible values for Author_Role
		accuser
		assistant
		bully
		defender
		reinforcer
		reporter
		victim
		other
		NA - The tweet is not a bullying trace and we didn't annotate its author role
	The possible values for Emotion
		anger
		embarrassment
		empathy
		fear
		none
		other
		pride
		relief
		sadness
		NA - The tweet is not a bullying trace and we didn't annotate its emotion
		
vocabulary
	The vocabulary file for all features. Each line is a token and the 
	index is the line number, starting from 1.
	
featureVector
	
	The feature vectors are written in a sparse vector format as commonly used 
	in SVM-light.  Each line corresponds to one tweet and has the format:

	featureIndex:value featureIndex:value featureIndex:value ...

	Only features with a nonzero value are listed.  Each vector is normalized
	to have norm 1.  You will need to attach a target label before training SVM.


-----------------------------Reference -----------------------------------------

[1] Learning from bullying traces in social media.
Jun-Ming Xu, Kwang-Sung Jun, Xiaojin Zhu, and Amy Bellmore.
In North American Chapter of the Association for Computational Linguistics - Human Language Technologies (NAACL-HLT).
Montreal, Canada, 2012.

[2] Understanding and Fighting Bullying with Machine Learning.
Jun-Ming Xu.
Phd Thesis, University of Wisconsin-Madison, June 2015.

Contact: Jun-Ming Xu (xujm@cs.wisc.edu), Xiaojin Zhu (jerryzhu@cs.wisc.edu)
