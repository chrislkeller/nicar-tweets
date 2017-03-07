import os
import csv
import time
import logging
import datetime
import re
from datetime import tzinfo
import pytz
from pytz import timezone
from dateutil import parser
from twitter import *

logger = logging.getLogger("root")
logging.basicConfig(
    format = "\033[1;36m%(levelname)s: %(filename)s (def %(funcName)s %(lineno)s): \033[1;37m %(message)s",
    level=logging.DEBUG
)

TWITTER_CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY")
TWITTER_CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET")
TWITTER_ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
LOCAL_TIMEZONE = pytz.timezone("US/Pacific")
TWITTER_TIMEZONE = timezone("UTC")

class TwitterUserSearch(object):

    # username to search
    user = "chrislkeller"

    # column names for our csv
    # this will change if you pull in more data
    csv_headers = [
        "tweet_utc_date",
        "user_name",
        "user_screen_name",
        "tweet_text",
        "tweet_url",
        "tweet_id",
        "user_profile_image_url",
        "user_location",
        "source",
        "in_reply_to_screen_name",
        "in_reply_to_status_id",
        "image_link",
        "retweet_count",
        "favorite_count",
        "time_zone",
        "geo_enabled",
        "geography",
        "coordinates",
        "lang",
    ]

    # what we'll name our csv file
    csv_filename = "_%s_tweets.csv" % (user)


    def _init(self, *args, **kwargs):
        """
        start the whole twitter hashtag search a rollin
        """

        # open a file
        with open(self.csv_filename, "wb") as csv_file:

            # that will become our csv
            csv_output = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)

            # write the header row to the csv file
            csv_output.writerow(self.csv_headers)

            # return our tweets
            tweet_results = self.construct_twitter_search(self.user)

            # for each status
            for tweet in tweet_results:

                # get the UTC time for each
                tweet_date = parser.parse(tweet["created_at"])

                # set some timezone information
                tweet_date = tweet_date.replace(tzinfo=TWITTER_TIMEZONE)

                # build a new csv row
                csv_row = self.build_csv_row_from(tweet, tweet_date)

                # write the new csv row
                csv_output.writerow(csv_row)


    def construct_twitter_search(self, user):
        """
        function to auth with twitter and return tweets
        """

        # build the authorization for the twitter api
        twitter_object = Twitter(
            auth=OAuth(
                TWITTER_ACCESS_TOKEN,
                TWITTER_ACCESS_TOKEN_SECRET,
                TWITTER_CONSUMER_KEY,
                TWITTER_CONSUMER_SECRET
            )
        )

        # retrieve the tweets
        tweet_results = twitter_object.statuses.user_timeline(
            screen_name=user,
            count=200
        )

        # return them
        return tweet_results


    def build_csv_row_from(self, tweet, tweet_date):
        """
        create a csv row from tweet results
        """

        # construct url format
        tweet_url = "https://twitter.com/" + tweet["user"]["screen_name"].encode('ascii', 'ignore') + "/status/" + str(tweet["id"])

        # output some information
        print "%s - %s - %s" % (
            tweet_date,
            tweet["user"]["screen_name"],
            tweet_url,
        )

        # see if an image is present in the dictionary
        has_image = tweet.has_key("media")

        # if there are images
        if has_image == True:

            # grab it
            tweet_image = tweet["media"]["media_url_https"]

        # otherwise
        else:

            # call it none
            tweet_image = None

        # build a row of tweet data
        csv_row_data = [
            tweet_date,
            tweet["user"]["name"].encode('ascii', 'ignore'),
            tweet["user"]["screen_name"].encode('ascii', 'ignore'),
            tweet["text"].encode('ascii', 'ignore'),
            tweet_url.encode('ascii', 'ignore'),
            tweet["id"],
            tweet["user"]["profile_image_url"].encode('ascii', 'ignore'),
            tweet["user"]["location"].encode('ascii', 'ignore'),
            tweet["source"].encode('ascii', 'ignore'),
            tweet["in_reply_to_screen_name"],
            tweet["in_reply_to_status_id_str"],
            tweet_image,
            tweet["retweet_count"],
            tweet["favorite_count"],
            tweet["user"]["time_zone"],
            tweet["user"]["geo_enabled"],
            tweet["geo"],
            tweet["coordinates"],
            tweet["lang"],
        ]

        # print the row
        print csv_row_data

        # return the row
        return csv_row_data


if __name__ == '__main__':
    task_run = TwitterUserSearch()
    task_run._init()
    print "\nTask finished at %s\n" % str(datetime.datetime.now())
