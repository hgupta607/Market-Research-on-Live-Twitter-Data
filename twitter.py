from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s
#consumer key, consumer secret, access token, access secret.
ckey="wqDkzCYscaTGYTfwKUTecs6f0"
csecret="Uq7TD9nQLoL59ZCkzTokNJoeNNcHOGS0PGoaRxw7cBmVTYXGUH"
atoken="69835244-4oezQn0kF3MPzhSkn6UBnBYDXpW6mJVPKG16eAMNB"
asecret="vblQmJoU6LFkdWzvns4r20uZyMLMCL3kygZ4GeMhU3wb9"

ckey="wqDkzCYscaTGYTfwKUTecs6f0"
csecret="Uq7TD9nQLoL59ZCkzTokNJoeNNcHOGS0PGoaRxw7cBmVTYXGUH"
atoken="69835244-4oezQn0kF3MPzhSkn6UBnBYDXpW6mJVPKG16eAMNB"
asecret="vblQmJoU6LFkdWzvns4r20uZyMLMCL3kygZ4GeMhU3wb9"

class listener1(StreamListener):
    def on_data(self, raw_data):
        try:
            all_data = json.loads(raw_data)
            tweet = all_data["text"]
            sentiment_value, confidence = s.sentiment(tweet)
            print(tweet, sentiment_value, confidence)
            if confidence*100 >= 60 :
                output = open("twitter-out.txt","a")
                output.write(sentiment_value)
                output.write('\n')
                output.close()
            return True
        except:
            return True

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener1())
twitterStream.filter(track=["Obama"])