import random

class Markov: 
    def __init__(self, text):
        self.word_dict = {}
        self.words = text.lower().split()
        self.words_len = len(self.words)
        self.generate_dict()
        
    def thirds(self):
        for index in range(len(self.words) - 2):
            yield (self.words[index], self.words[index+1], self.words[index+2])
            
    def generate_dict(self):
        
        for w1, w2, w3 in self.thirds():
            key = (w1, w2)
            if key in self.word_dict:
                self.word_dict[key].append(w3)
            else:
                self.word_dict[key] = [w3]

    def generate_tweet_text(self, word_limit=20):
        
        n = random.randint(0, self.words_len - (word_limit + 3))
        w1, w2 = self.words[n], self.words[n + 1]
        tweet = ''
        
        for x in xrange(word_limit):
            tweet += '%s ' % (w1)
            try:
                w1, w2 =  w2, random.choice(self.word_dict[(w1, w2)])
            except KeyError:
                print "EXCEPTION"
                n = random.randint(0, self.words_len - (word_limit + 3 - x))
                w1, w2 = self.words[n], self.words[n + 1]
        return tweet.capitalize()

class TweetProc:
    def __init__(self, text):
        self.text = text
        self.dupe_count = 0
        self.long_count = 0
        
    def original(self,tweet):
        if self.text.lower().find(tweet.lower()) > -1:
            print "NOT ORIGINAL"
            self.dupe_count += 1
            return False
        return True
    def too_long(self, tweet):
        if len(tweet) > int(140):
            print "TOO LONG"
            self.long_count += 1
    def remove_mentions(self, tweet):
        words = tweet.split()
        retVal = ''
        for word in words[:]:
            if word.find('@') == 0:
                words.remove(word)
        for word in words:
            print word
            retVal += '%s ' % (word)
        return retVal
        
    