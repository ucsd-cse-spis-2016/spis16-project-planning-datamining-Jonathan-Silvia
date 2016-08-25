import tweepy
import string

auth = tweepy.OAuthHandler('7iEimQyicVavG5uTVxCCR8G1t', 'rK5xYEgyE5bW2tP0LkG9YrGFRAX3peqLXJw48LUvTtCcbuB7fz')
auth.set_access_token('768841306042839040-49QlscNfwnWypo378JH3Euj4LFdxvWK', '0INflrYeTpkdU9hVsoCf5uAbE54AqAGgRof7wf2RLaiBa')

api = tweepy.API(auth)
public_tweets = api.home_timeline()
'''for tweet in public_tweets:
    print tweet.text'''

user = api.get_user('SPISElectionz')

#follows back
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()

#print out followers' screen names
'''def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

for follower in limit_handled(tweepy.Cursor(api.followers).items()):
    if follower.friends_count < 300:
        print follower.screen_name'''
tweepy.Cursor(api.user_timeline, id="ImpWalker")

'''# Iterate through all of the authenticated user's friends
for friend in tweepy.Cursor(api.friends).items():
    # Process the friend here
    process_friend(friend)

# Iterate through the first 200 statuses in the friends timeline
for status in tweepy.Cursor(api.friends_timeline).items(200):
    # Process the status here
    process_status(status)'''

#Prints out users timeline with speciefied count
'''stuff = api.user_timeline(screen_name = 'realDonaldTrump', count = 5)
print stuff'''

#Follow all of the specified users followes. Will lock you out if you do too
#much though :c
'''followers = api.followers_ids('realDonaldTrump')

for f in followers:
    api.create_friendship(f)'''

def getStatus(user):
    '''returns tweet as a string'''
    api.get_user(user)
    return str(scname.status.text)

def listOfWords(user):
    '''returns a list of words (in lower-case) from tweets from a user
        still has punctuation though :-('''
    api.get_user(user)
    words = getStatus(user).split()
    lowerWords = []
    for w in words:
        lowerWords.append(w.lower())
    return lowerWords

#Returns tweets that match a specified query.
#API.search(q[, lang][, locale][, rpp][, page][, since_id][, geocode][, show_user])


'''===================================================================
Useful Things for Sentiment Analysis

import string
string.punctuation => list of punctuation

Splitting words into characters without punctuation:
eg. dchar = (c for c in dchar if c not in string.punctuation)

Putting it back together:
eg. dnopunct = ''.join(dchar)

?linear regression? 

'''
