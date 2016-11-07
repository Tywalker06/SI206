# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.
import tweepy
import sys
from textblob import TextBlob
import bs4


def uprint(*objects, sep=' ', end='\n', file=sys.stdout):

    enc = file.encoding

    if enc == 'UTF-8':

        print(*objects, sep=sep, end=end, file=file)

    else:

        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)

        print(*map(f, objects), sep=sep, end=end, file=file)

# Unique code from Twitter
access_token = 	"3130902574-U9GqTuof5DAkkp1OyvOllDhajhC6YUVwrc2wVEb"
access_token_secret = 	"p7h3b5MV08o4ZWjy2n2GelVtUb09GLCZeM72ZFoueMPqZ"
consumer_key = 	"N2oxz2amhLPiY60bNiTrgcsIK"
consumer_secret = "tkRZA5FQJuvcE5QUJbxrgjzpIXZh4Y1GUTbeLBdPmsTH3CEtO4"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search('Hillary Clinton')
polarity = []
subjectivity = []
uprint(type(public_tweets))

for tweet in public_tweets:
	uprint(tweet.text)
	analysis = TextBlob(tweet.text)
	uprint(analysis.sentiment)
	polarity.append(analysis.sentiment[0])
	subjectivity.append(analysis.sentiment[1])

average_polarity = sum(polarity)/len(polarity)
average_subjectivity = sum(subjectivity)/len(subjectivity)

	

uprint("Average subjectivity is:", average_subjectivity)
uprint("Average polarity is:", average_polarity)
