import tweepy
import string
from collections import defaultdict
from textblob import TextBlob

auth = tweepy.OAuthHandler('7iEimQyicVavG5uTVxCCR8G1t', 'rK5xYEgyE5bW2tP0LkG9YrGFRAX3peqLXJw48LUvTtCcbuB7fz')
auth.set_access_token('768841306042839040-49QlscNfwnWypo378JH3Euj4LFdxvWK', '0INflrYeTpkdU9hVsoCf5uAbE54AqAGgRof7wf2RLaiBa')

api = tweepy.API(auth)
public_tweets = api.home_timeline()
'''for tweet in public_tweets:
    print tweet.text'''

user = api.get_user('SPISElectionz')

'''#follows back
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()'''

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

'''tweepy.Cursor(api.user_timeline, id="ImpWalker")'''

'''# Iterate through all of the authenticated user's friends
for friend in tweepy.Cursor(api.friends).items():
    # Process the friend here
    process_friend(friend)

# Iterate through the first 200 statuses in the friends timeline
for status in tweepy.Cursor(api.friends_timeline).items(200):
    # Process the status here
    process_status(status)'''

#Prints out users timeline with speciefied count
'''stuff = api.user_timeline(screen_name = 'realDonaldTrump', count = 5)'''
#print stuff

#Follow all of the specified users followes. Will lock you out if you do too
#much though :c
'''followers = api.followers_ids('realDonaldTrump')

for f in followers:
    api.create_friendship(f)'''


def getStatus(user):
    '''returns tweet as a string'''
    scname = api.get_user(user)
    return (scname.status.text).encode('utf-8')

def sentimentOfStatus(user):
    '''returns sentiment of user's latest tweet'''
    tweet = TextBlob(getStatus(user))
    return tweet.sentiment

def listOfWords(status):
    '''returns a list of words (in lower-case) from tweets from a user
        without punctuation :-)'''
    #api.get_user(user)
    words = status.split()
    lowerWords = []
    for w in words:
        lowerWords.append(noPunct(w.lower()))
    return lowerWords

def listOfStatuses(user, num):
    '''returns list of statuses from a user'''
    listOfTweets = []
    stuff = api.user_timeline(screen_name = user, count = num)
    for s in stuff:
        listOfTweets.append((s.text).encode('utf-8'))
    return listOfTweets

def noPunct(word):
    '''removes punctuation from a word'''
    chars = [c for c in word if c not in string.punctuation]
    noPunc = ''.join(chars)
    return noPunc

def search(query, num):
    '''returns list of words from tweets that contain query'''
    listOfTweets = []
    words = []
    stuff = api.search(query, count = num)
    for s in stuff:
        listOfTweets.append((s.text).encode('utf-8'))
    for l in listOfTweets:
        words.append(listOfWords(l))
    return words

def countWords(listOfWords):
    '''returns defaultdict counting the occurance of each word'''
    wordCountDict = defaultdict(int)
    for l in listOfWords:
        for w in l:
            if w[0:4] != 'http':
                wordCountDict[w] += 1
    return wordCountDict

def wordCounts(dict):
    '''returns a list of words in ascending order based on how often they
        occur'''
    wordCount = [[dict[w],w] for w in dict]
    wordCount.sort()
    wordCount.reverse()
    return wordCount

def wordList(list):
    '''creates a list of words, pair with wordCounts function'''
    words = [w[1] for w in list[:1000]]
    return words

def feature(datum):
    '''sets up array of word occurences'''
    feat = [0]*len(words)
    r = text_to_wordlist(datum)
    for w in r:
        if w in words:
            feat[wordId[w]] += 1
    feat.append(1) #offset
    return feat
        

#Returns tweets that match a specified query.
#API.search(q[, lang][, locale][, rpp][, page][, since_id][, geocode][, show_user])


'''
======================================================================
Useful Things for Sentiment Analysis!!

import string
string.punctuation => list of punctuation

Splitting words into characters without punctuation:
    eg. dchar = [c for c in dchar if c not in string.punctuation]

Putting it back together:
    eg. dnopunct = ''.join(dchar)

?linear regression?

======================================================================
Scraping from HTML pages:

-Scraper extension for Google Chrome
-select element on webpage and find XPath
-'*' symbol is wildcard and can access elements of some type (ie. all comments,
    all usernames, etc)

'''
