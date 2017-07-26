import sys
import tweepy as tp
import re


def initialize():
    print ""
    print "Initializing..."
    ck = "3LjxCG5kBSTEPvVoV9CjpsaAw"
    cs = "qacbwE6POyfvqjiX9yu2TGUgVk2XwHeEnC5ERKOnR1t9pVG5BA"
    at = "2468857296-W1aTNkxN5prnH4VbNWTXK84uw1cWO5TEVENsWGb"
    ats = "CyZ31u3iQiHlNlvZghXu6er0xhm17qkoH5aEtedvK5aW"
    print "Authenticating..."
    try:
        auth = tp.OAuthHandler(ck, cs)
        auth.set_access_token(at, ats)
        apint = tp.API(auth)
    except:
        print("Error: Authentication Failed")
    else:
        print("Connected to twitter API successfully!")
    return apint


def processtw(tweet):
    tweet = tweet.lower()
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def fetchtw(ap, c):
    tweets = []
    qu = "sarcasm"
    ftchtw = ap.search(q=qu, lang='en', rpp=100)
    tweets.extend(ftchtw)
    oldest = tweets[-1].id - 1
    c = c - 100
    while (c >= 100):
        try:
            ftchtw = ap.search(q=qu, lang='en', rpp=100, max_id=oldest)
            tweets.extend(ftchtw)
            oldest = tweets[-1].id - 1
        except tweepy.TweepError as e:
            print("Error : " + str(e))
        c = c - 100
    if c > 0:
        ftchtw = ap.search(q=qu, lang='en', rpp=c, max_id=oldest)
        tweets.extend(ftchtw)
    return tweets


def main():
    apiobj = initialize()
    nu = input("Enter number tweets to be fetched:")
    stwts = fetchtw(apiobj, nu)
    f = open("stdata.txt", "w+")
    for onet in stwts:
        pt = processtw(onet.text)
        f.write(pt + "\n")
    print "File created!"
    f.close()


if __name__ == "__main__":
    main()
