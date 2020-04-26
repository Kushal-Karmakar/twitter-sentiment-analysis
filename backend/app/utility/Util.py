from textblob import TextBlob


class Util():

    def sentiment_calc(tweet_text):
        try:
            return TextBlob(tweet_text).sentiment
        except:
            return None