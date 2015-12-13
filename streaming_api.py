from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

f = open("data.txt", "w")
class Listener(StreamListener):

    def on_data(self,data):
        f.write(data+'\n')
        print "writing object to file"
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth, Listener())
print "Enter a keyword"
keyword=raw_input()
stream.filter(track=[keyword])


