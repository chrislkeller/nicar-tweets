nicar-tweets
============

**What**: A quick script using the Twitter python library and the Twitter search API to pull and store in csv the annual #NICAR tweets.


From Twitter's [search API documentation](https://dev.twitter.com/rest/public/search):

>Before getting involved, it’s important to know that the Search API is focused on relevance and not completeness. This means that some Tweets and users may be missing from search results. If you want to match for completeness you should consider using a Streaming API instead.

The search API is also rate-limited. More information on that [here](https://dev.twitter.com/rest/public/rate-limiting).

**What is here?**:

* [_#NICAR17_tweets.csv](_%23NICAR17_tweets.csv): Pulled from a date range of 2/26/17 and 3/6/17.
* [_#NICAR16_tweets.csv](_%23NICAR16_tweets.csv): Pulled from a date range of 3/7/16 and 3/14/16.
* [_#srccon_tweets.csv](_%23srccon_tweets.csv): Pulled from a date range of 6/23/15 and 6/27/15.
* [_#IRE15_tweets.csv](_%23IRE15_tweets.csv): Pulled from a date range of 6/3/15 and 6/9/15.
* [_#NICAR15_tweets.csv](_%23NICAR15_tweets.csv): Pulled from a date range of 3/3/15 and 3/10/15.
* [_#IRE14_tweets.csv](_%23IRE14_tweets.csv): Pulled from a date range of 6/26/14 and 7/1/14.
* [_#NICAR14_tweets.csv](_%23NICAR14_tweets.csv): Pulled from a date range 2/25/14 and 3/4/14. I have no idea if these are all of them, but there are a lot. Let me know if you do anything fun with them.

**Getting Started**:

* Create a virtual enviroment or if that's not your thing install the requirements

    ```pip install -r requirements.txt```

* Configure init_search.py
    * There are a handful of variables to change.
        * ```TWITTER_CONSUMER_KEY```: You wil need to [register an application](https://apps.twitter.com/) to acquire the proper authentication keys & tokens.
        * ```TWITTER_CONSUMER_SECRET```: You wil need to [register an application](https://apps.twitter.com/) to acquire the proper authentication keys & tokens.
        * ```TWITTER_ACCESS_TOKEN```: You wil need to [register an application](https://apps.twitter.com/) to acquire the proper authentication keys & tokens.
        * ```TWITTER_ACCESS_TOKEN_SECRET```: You wil need to [register an application](https://apps.twitter.com/) to acquire the proper authentication keys & tokens.
        * ```LOCAL_TIMEZONE```:
        * ```start_date_for_search```: The date and time you want to begin your search - localized for the ```LOCAL_TIMEZONE``` in a Python datetime format - (year, month, day, hour, minutes). You can really only search back 6 or 7 days.
        * ```hashtag```: the hashtag to search

    * The script will write the following to a csv named after your chosen hashtag:
        * hashtag:
        * tweet_utc_date:
        * user_name:
        * user_screen_name:
        * bot_or_not:
        * tweet_text:
        * tweet_url:
        * tweet_id:
        * user_profile_image_url:
        * user_location:
        * source:
        * in_reply_to_screen_name:
        * in_reply_to_status_id:
        * image_link:
        * retweet_count:
        * favorite_count:
        * time_zone:
        * geo_enabled:
        * geography:
        * coordinates:
        * lang:

* Run init_search.py

    ```python init_search.py```
