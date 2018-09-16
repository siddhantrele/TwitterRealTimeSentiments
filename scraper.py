import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TwitterSentiment.settings")
django.setup(), 

import scraper_settings as settings
import tweepy
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from OutputSentiment.models import Tweet
import re

def find_all_words(words, sentence):
    all_words = re.findall(r'\w+', sentence)
    words_found = []
    for word in words:
        for all_word in all_words:
            if word.lower()==all_word.lower():
                words_found.append(word.lower())
    return words_found

class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if status.retweeted:
            return

        description = status.user.description
        loc = status.user.location
        text = status.text
        coords = status.coordinates
        geo = status.geo
        name = status.user.screen_name
        user_created = status.user.created_at
        followers = status.user.followers_count
        id_str = status.id_str
        created = status.created_at
        retweets = status.retweet_count
        bg_color = status.user.profile_background_color
        sentiment = SentimentIntensityAnalyzer().polarity_scores(text)


        terms_found=find_all_words(settings.TRACK_TERMS,text)

        for term in terms_found:
            tweet=Tweet.objects.create(term=term,text=text,sentiment=sentiment['compound'])

        return True

    def on_error(self, status_code):
        print("Error Code")
        print(status_code)

auth = tweepy.OAuthHandler(settings.TWITTER_KEY, settings.TWITTER_SECRET)
auth.set_access_token(settings.TWITTER_APP_KEY, settings.TWITTER_APP_SECRET)
api = tweepy.API(auth)

stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
#print('reached end')
stream.filter(track=settings.TRACK_TERMS)