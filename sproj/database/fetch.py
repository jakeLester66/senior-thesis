## fetch.py
import pandas as pd
from database.config import create_cnx


def fetch_vix():
    """

    :return: DataFrame object with vix data from mysql server
    """

    cnx = create_cnx()
    cursor = cnx.cursor()

    query = ("SELECT * FROM `Vix_Data` "
             "ORDER BY `datetime` ASC;")
    cursor.execute(query)
    vix_df = pd.DataFrame(cursor.fetchall())
    vix_df.columns = cursor.column_names
    vix_df.set_index(vix_df['datetime'], inplace=True)
    # vix_df.drop(labels='datetime', axis=1, inplace=True)  # weird bug above prevents drop

    cursor.close()
    cnx.close()

    return vix_df


def fetch_spx():
    """

    :return: DataFrame object with spx data from mysql server
    """

    cnx = create_cnx()
    cursor = cnx.cursor()

    query = ("SELECT * FROM `Spx_Data` "
             "ORDER BY `datetime` ASC;")
    cursor.execute(query)
    spx_df = pd.DataFrame(cursor.fetchall())
    spx_df.columns = cursor.column_names
    spx_df.set_index(spx_df['datetime'], inplace=True)
    # spx_df.drop(labels='datetime', axis=1, inplace=True)  # weird bug above prevents drop

    cursor.close()
    cnx.close()

    return spx_df


def fetch_tweets():
    """

    :return: DataFrame object with tweet data from mysql server
    """

    cnx = create_cnx()
    cursor = cnx.cursor()

    query = ("SELECT * FROM `Tweets` "
             "ORDER BY `created_at` ASC;")
    cursor.execute(query)
    tweet_df = pd.DataFrame(cursor.fetchall())
    tweet_df.columns = cursor.column_names
    tweet_df.set_index(tweet_df['tweet_id'], inplace=True)
    tweet_df.rename(columns={'created_at': 'datetime'}, inplace=True)

    cursor.close()
    cnx.close()

    return tweet_df


def fetch_users():
    """

    :return: DataFrame object with user data from mysql server
    """
    cnx = create_cnx()
    cursor = cnx.cursor()

    query = ("SELECT * FROM `Users`")
    cursor.execute(query)
    user_df = pd.DataFrame(cursor.fetchall())
    user_df.columns = cursor.column_names
    user_df.set_index(user_df['user_id'], drop=True, inplace=True)

    cursor.close()
    cnx.close()

    return user_df


def fetch_nltk_acc():
    cnx = create_cnx()
    cursor = cnx.cursor()

    query = ("SELECT * FROM `nltk_validate`")
    cursor.execute(query)
    nltk_acc = pd.DataFrame(cursor.fetchall())
    nltk_acc.columns = cursor.column_names
    nltk_acc.set_index(nltk_acc['correct_label'], drop=True, inplace=True)
    nltk_acc = nltk_acc.drop(columns=['correct_label'])

    cursor.close()
    cnx.close()

    return nltk_acc


def fetch_flair_acc():
    cnx = create_cnx()
    cursor = cnx.cursor()

    query = ("SELECT * FROM `flair_validate`")
    cursor.execute(query)
    flair_acc = pd.DataFrame(cursor.fetchall())
    flair_acc.columns = cursor.column_names
    flair_acc.set_index(flair_acc['correct_label'], drop=True, inplace=True)
    flair_acc = flair_acc.drop(columns=['correct_label'])

    cursor.close()
    cnx.close()

    return flair_acc


def fetch_cor():
    cnx = create_cnx()
    cursor = cnx.cursor()

    query = ("SELECT * FROM `corelation`")
    cursor.execute(query)
    cor_df = pd.DataFrame(cursor.fetchall())
    cor_df.columns = cursor.column_names
    # nltk_acc.set_index(nltk_acc['label'], drop=True, inplace=True)
    # cor_df = cor_df.drop(columns=['label'])

    cursor.close()
    cnx.close()

    return cor_df


def custom_query(query):
    cnx = create_cnx()
    cursor = cnx.cursor()

    cursor.execute(query)
    custom_df = pd.DataFrame(cursor.fetchall())
    custom_df.columns = cursor.column_names

    cursor.close()
    cnx.close()

    return custom_df
