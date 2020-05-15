## clean_tweets.py

import re


def remove_url_token(text):
    """
    Removes url tokens from a string
    :param text: string
    :return: string clean from url tokens
    """
    s2 = re.sub(r'http\S+', '', text)
    return s2


def remove_all_urls(tweets_df):
    """
    Removes all url tokens from the 'text' field of a DataFrame
    :param tweets_df: DataFrame with 'text' field containing strings
    :return: DataFrame with 'text' field clean from url tokens
    """
    tweets_df['text'] = [remove_url_token(row['text']) for index, row in tweets_df.iterrows()]
    return tweets_df
