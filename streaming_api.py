from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "4010780236-Q2YCnYqSCgdmTMiT2G6Hj2YGxmH34pt3slVEueM"
access_token_secret = "0DDNg2tS2XJK32bPggoJXzRX2W2xJVUxmFw1kdMLmA0J1"
consumer_key = "Of9RURntChba6Ygrt5egqJe2E"
consumer_secret = "0nm1zr65lkdpM6RKNPQEiGLa3Xq7B3v6jUDxoXwFKrlN7yqTc7"

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


