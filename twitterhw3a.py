# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

print("""No output necessary although you 
	can print out a success/failure message if you want to.""")
import tweepy
import sys

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):

    enc = file.encoding

    if enc == 'UTF-8':

        print(*objects, sep=sep, end=end, file=file)

    else:

        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)

        print(*map(f, objects), sep=sep, end=end, file=file)

# Unique code from Twitter


# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

post_image_status = api.update_with_media('BSI.PNG', status = '#UMSI206 #Proj3')
# public_tweets = api.search('Trump')


# for tweet in public_tweets:
# 	uprint(tweet.text)
	