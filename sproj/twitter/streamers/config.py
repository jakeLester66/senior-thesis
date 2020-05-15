# tweepy-streamer\streamers\config.py

import tweepy
import logging
import os

logger = logging.getLogger()


def create_api():
    consumer_key = os.getenv("CONSUMER_KEY").replace('"','')
    consumer_secret = os.getenv("CONSUMER_SECRET").replace('"','')
    access_token = os.getenv("ACCESS_TOKEN").replace('"','')
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET").replace('"','')

    assert 25== len(consumer_key)
    assert 50 == len(consumer_secret)
    assert 50 == len(access_token)
    assert 45 == len(access_token_secret)

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
