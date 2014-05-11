"""
Gets auth, save this in your .tweetnet
"""
import os
import sys
sys.path.append("/mit/ofir/6857/tweetnet");
import tweepy

consumer_token = os.environ['TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print 'Error! Failed to get request token.'

print "Go to:", redirect_url

verifier = raw_input("verifier: ")

auth.get_access_token(verifier)

print "Save these lines to your .tweenet..."
print "export TWITTER_ACCESS_KEY=%s" % auth.access_token.key
print "export TWITTER_ACCESS_SECRET=%s" % auth.access_token.secret
