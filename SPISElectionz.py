import tweepy
import time
import datetime
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
    return (scname.status.text)

def sentimentOfStatus(user):
    '''returns sentiment of user's latest tweet'''
    tweet = TextBlob(getStatus(user))
    return tweet.sentiment

def sentimentOfTweet(string):
    '''returns sentiment of a given string'''
    tweet = TextBlob(string.lower())
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
        listOfTweets.append(s.text.lower())
    '''for l in listOfTweets:
        words.append(listOfWords(l))
    return words'''
    return listOfTweets

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

def sentimentOfStatuses(list):
    '''returns a list of tuples of statuses and their sentiments'''
    #listOfStatuses = search(query, num)
    sentimentList = []
    for s in list:
        sentimentList.append((s, sentimentOfTweet(s)))
    return sentimentList

def avgPolarity(listOfPolarity):
    polarity = []
    for t in listOfPolarity:
        polarity.append(t[0])
    return (sum(polarity))/len(listOfPolarity)

#Returns tweets that match a specified query.
#API.search(q[, lang][, locale][, rpp][, page][, since_id][, geocode][, show_user])

if __name__ == "__main__":

    while True:

        current_time = datetime.datetime.now().time()
        
        hillary = []
        trump = []
        gary = []
        jill = []
        harambe = []

        hashtags = ["#Election2016", "#Trump", "#Clinton", "#Democrats", "#Republicans", "#JillStein", "#GaryJohnson", "GreenParty", "Libertarians", "WeLoveHarambe"\
                    "#Harambe", "harambe"]

        list = []

        for h in hashtags:
            for s in search(h, 50):
                list.append(s)

        j = sentimentOfStatuses(list)
        
        for t in j:
            if ("hillary" in t[0]) or ("clinton" in t[0]) or ("@hillaryclinton" in t[0]):
                if t[1][0] != 0.0 and t[1][1] != 0.0:
                    hillary.append(t[1])
            if ("trump" in t[0]) or ("donald" in t[0]) or ("@realdonaldtrump" in t[0]):
                if t[1][0] != 0.0 and t[1][1] != 0.0:
                    trump.append(t[1])
            if ("gary" in t[0]) or ("johnson" in t[0]) or ("@govgaryjohnson" in t[0]):
                if t[1][0] != 0.0 and t[1][1] != 0.0:
                    gary.append(t[1])
            if ("jill" in t[0]) or ("stein" in t[0]) or ("@drjillstein" in t[0]):
                if t[1][0] != 0.0 and t[1][1] != 0.0:
                    jill.append(t[1])
            if ("harambe" in t[0]):
                if t[1][0] != 0.0 and t[1][1] != 0.0:
                    harambe.append(t[1])

                    
        print "Time:", current_time.isoformat()
        print "Hillary:", avgPolarity(hillary), "\t\tCount:", len(hillary)
        print "Trump:", avgPolarity(trump), "\t\tCount:", len(trump)
        print "Gary:", avgPolarity(gary), "\t\tCount:", len(gary)
        print "Jill:", avgPolarity(jill), "\t\tCount:", len(jill)
        print "Harambe:", avgPolarity(harambe), "\tCount:", len(harambe)
        print "==============================================="

        time.sleep(60)
                         
    
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
