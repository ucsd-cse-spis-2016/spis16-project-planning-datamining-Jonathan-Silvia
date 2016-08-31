import tweepy
import time
import datetime
import numpy
import string
from collections import defaultdict
from textblob import TextBlob
from PieChartAndBarGraph import *

auth = tweepy.OAuthHandler('7iEimQyicVavG5uTVxCCR8G1t', 'rK5xYEgyE5bW2tP0LkG9YrGFRAX3peqLXJw48LUvTtCcbuB7fz')
auth.set_access_token('768841306042839040-49QlscNfwnWypo378JH3Euj4LFdxvWK', '0INflrYeTpkdU9hVsoCf5uAbE54AqAGgRof7wf2RLaiBa')

api = tweepy.API(auth)
public_tweets = api.home_timeline()
'''for tweet in public_tweets:
    print tweet.text'''

#user = api.get_user('SPISElectionz')


#Follow all of the specified users followes. Will lock you out if you do too
#much though :c
'''followers = api.followers_ids('realDonaldTrump')

for f in followers:
    api.create_friendship(f)'''

hashtags = ["#election2016", "#trump", "#clinton", "#democrats", "#republicans", "#jillstein", "#garyjohnson", "greenparty", "libertarians", "weloveharambe"\
                    "#harambe", "harambe"]
commonWords = ["amp", "election2016", "trump", "clinton", "hillary", "hillary", "clinton", "democrats", "republicans", "jillstein", "garyjohnson", "greenparty", "libertarians", "weloveharambe"\
                "harambe", "harambe", "hillaryclinton", "realdonaldtrump", "govgaryjohnson", "drjillstein", "|", "rt", "a", "about", "above", "above", "across", "after", "afterwards", \
               "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an",\
               "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become",\
               "becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "i", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]


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

def isntInt(string):
    try:
        u = int(string)
        return False
    except:
        return True

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
    words = []
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
    '''returns the average polarity'''
    polarity = []
    for t in listOfPolarity:
        polarity.append(t[0])
    return (sum(polarity))/len(listOfPolarity)

def checkWord(list):
    if list[0][1] not in commonWords:
        return list[0][1]
    else:
        checkWord(list[1:len(list)])

def wordID(listOfStatuses):
    '''returns list of top 10 words used that aren't in commonWords'''
    splitList = []
    for s in listOfStatuses:
        splitList.append(s.split())
    l = wordCounts(countWords(splitList))

    topWords = []
    for e in l:
        if len(topWords) == 10:
            break
        if (e[1] not in commonWords) and (len(e[1]) != 1) and (e[1][0] != '@') and (e[1][0] != '#') and (e[1][0] != '\\') and (isntInt(e[1])):
            topWords.append(noPunct(e[1]))
    return topWords

def barGraph(h, t, g, j, hb):
    
##    y = [avgPolarity(h), avgPolarity(t), avgPolarity(g), avgPolarity(j), avgPolarity(hb)] 
##    N = len(y)
##    x = ["Hillary", "Trump", "Gary", "Jill", "Harambe"]
##    width = 1/1.5
##    plt.bar(x, y, width, color="lightcoral")
##    
##    plt.ylabel('Candidates')
##    plt.xlabel('Polarity Rating')
##    plt.title('2016 Election Candidates and Current Ratings')
##
##    #plt.xticklabels(('Hillary Clinton', 'Donald Trump', 'Gary Johnson', 'Jill Stein', 'Harambe the Gorilla'))
##    fig = plt.gcf()
##    plt.show()

    x = xrange(5)
    y = [avgPolarity(h), avgPolarity(t), avgPolarity(g), avgPolarity(j), avgPolarity(hb)]
    plt = plt.figure()
    ax = f.add_axes([0.1, 0.1, 0.8, 0.8])
    ax.bar(x, y, align='center')
    ax.set_xticks(x)
    ax.set_xticklabels(['H', 't', 'Cee', 'Dee', 'h'])
    plt.show()
            

if __name__ == "__main__":

    try:
        while True:

            current_time = datetime.datetime.now().time()

            statusHillary = []
            statusTrump = []
            statusGary = []
            statusJill = []
            statusHarambe = []
            
            hillary = []
            trump = []
            gary = []
            jill = []
            harambe = []

            hashtags = ["#Election2016", "#Trump", "#Clinton", "#Democrats", "#Republicans", "#JillStein", "#GaryJohnson", "GreenParty", "Libertarians", "WeLoveHarambe"\
                        "#Harambe", "harambe"]

            list = []

            for h in hashtags:
                for s in search(h, 75):
                    list.append(s)

            j = sentimentOfStatuses(list)
            
            for t in j:
                if ("hillary" in t[0]) or ("clinton" in t[0]) or ("@hillaryclinton" in t[0]):
                    statusHillary.append(str(TextBlob(t[0])))
                    if t[1][0] != 0.0 and t[1][1] != 0.0:
                        hillary.append(t[1])
                if ("trump" in t[0]) or ("donald" in t[0]) or ("@realdonaldtrump" in t[0]):
                    statusTrump.append(str(TextBlob(t[0])))
                    if t[1][0] != 0.0 and t[1][1] != 0.0:
                        trump.append(t[1])
                if ("gary" in t[0]) or ("johnson" in t[0]) or ("@govgaryjohnson" in t[0]):
                    statusGary.append(str(TextBlob(t[0])))
                    if t[1][0] != 0.0 and t[1][1] != 0.0:
                        gary.append(t[1])
                if ("jill" in t[0]) or ("stein" in t[0]) or ("@drjillstein" in t[0]):
                    statusJill.append(str(TextBlob(t[0])))
                    if t[1][0] != 0.0 and t[1][1] != 0.0:
                        jill.append(t[1])
                if ("harambe" in t[0]):
                    statusHarambe.append(str(TextBlob(t[0])))
                    if t[1][0] != 0.0 and t[1][1] != 0.0:
                        harambe.append(t[1])     

                        
            print "Time:\t", current_time.isoformat()
            print "Hillary:", avgPolarity(hillary), "\t\t\tCount:", len(hillary), "\nCommon Words:", wordID(statusHillary)
            print "\n\nTrump:", avgPolarity(trump), "\t\t\tCount:", len(trump), "\nCommon Words:", wordID(statusTrump)
            print "\n\nGary:", avgPolarity(gary), "\t\t\tCount:", len(gary), "\nCommon Words:", wordID(statusGary)
            print "\n\nJill:", avgPolarity(jill), "\t\t\tCount:", len(jill), "\nCommon Words:", wordID(statusJill)
            print "\n\nHarambe:", avgPolarity(harambe), "\t\tCount:", len(harambe), "\nCommon Words:", wordID(statusHarambe)
            print "===================================================================="

            PieChart(hillary, trump, gary, jill, harambe)

            time.sleep(60)

    except KeyboardInterrupt:
        raise
    
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
