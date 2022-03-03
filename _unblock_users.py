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
import twitter

logger = logging.getLogger("root")
logging.basicConfig(
    format = "\033[1;36m%(levelname)s: %(filename)s (def %(funcName)s %(lineno)s): \033[1;37m %(message)s",
    level=logging.DEBUG
)

CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET")
ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

class TwitterUserSearch(object):

    def _init(self, *args, **kwargs):
        auth = twitter.Api(
            consumer_key=CONSUMER_KEY,
            consumer_secret=CONSUMER_SECRET,
            access_token_key=ACCESS_TOKEN,
            access_token_secret= ACCESS_TOKEN_SECRET
        )
        logger.debug(auth.GetBlocksIDs())
        blocked_count = 0
        while True:
            blocked_user_ids = auth.GetBlocksIDs()
            logger.debug(blocked_user_ids)
            if not blocked_user_ids:
                print("No more IDs to unblock")
                break
            for user_id in blocked_user_ids:
                blocked_count = blocked_count + 1
                f = '%s: %s' % (blocked_count, user_id)
                logger.debug(f)
                try:
                    auth.DestroyBlock(user_id=user_id, include_entities=False, skip_status=True)
                except:
                    print("error")

if __name__ == '__main__':
    task_run = TwitterUserSearch()
    task_run._init()
    print "\nTask finished at %s\n" % str(datetime.datetime.now())
