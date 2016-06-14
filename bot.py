from TwitterAPI import TwitterAPI
import setup
from twitterclasses import Markov, TweetProc
import random

# Sets up Twitter auth    
api = TwitterAPI(setup.consumer_key, setup.consumer_secret, setup.access_token_key, setup.access_token_secret)  

min_volume = 1000
topics = []
r = api.request('trends/place', {'id': '2357024'})
for item in r.get_iterator():
    if item['tweet_volume'] > min_volume:
        topics.append(item['name'])
    if 'text' in item:
        print item['text']
    elif 'message' in item:
        print '%s (%d)' % (item['message'], item['code'])

tweet_text = ''
r = api.request('search/tweets', {'q': random.choice(topics), 'count': '100'})
for item in r.get_iterator():
    tweet_text += item['text']
    
mark = Markov(tweet_text)
proc = TweetProc(tweet_text)
tweet = ''

tweet = mark.generate_tweet_text()
while not proc.original(tweet) or proc.too_long(tweet):
    tweet = mark.generate_tweet_text()
    tweet = proc.remove_mentions(tweet)
    
try:
    print 'Number of generated tweets that were too long: {}'.format(proc.long_count)
    print 'Number of generated tweets that were duplicates: {}'.format(proc.dupe_count)
    print (tweet)
except Exception as e:
    print e
    print tweet.encode("utf8","ignore")

r = api.request('statuses/update', {'status': tweet})

if not r.status_code // 100 == 2:
    print 'Tweet status {}'.format(r.status_code)
    for item in r.get_iterator():
        print item
    