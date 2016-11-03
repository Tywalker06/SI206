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
access_token = 	"3130902574-U9GqTuof5DAkkp1OyvOllDhajhC6YUVwrc2wVEb"
access_token_secret = 	"p7h3b5MV08o4ZWjy2n2GelVtUb09GLCZeM72ZFoueMPqZ"
consumer_key = 	"N2oxz2amhLPiY60bNiTrgcsIK"
consumer_secret = "tkRZA5FQJuvcE5QUJbxrgjzpIXZh4Y1GUTbeLBdPmsTH3CEtO4"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

post_image_status = api.update_with_media('BSI.PNG', status = '#UMSI206 #Proj3')
# public_tweets = api.search('Trump')


# for tweet in public_tweets:
# 	uprint(tweet.text)
	