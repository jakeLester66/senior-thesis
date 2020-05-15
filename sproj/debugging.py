import database.fetch as fetch
import database.update as update
import common.finance as finance
import common.dates as dates
import sentiment.sentiment as sentiment

import pandas as pd
import matplotlib.pyplot as plt


def fetch_data():
    # Fetch data from DB
    vix_df = fetch.fetch_vix()
    spx_df = fetch.fetch_spx()
    tweet_df = fetch.fetch_tweets()
    return vix_df, spx_df, tweet_df


def group_data(vix_df, spx_df, tweet_df, group='1D'):
    # Group data by time period
    vix_df = dates.group_data(vix_df, 'close', method='lastValue', group=group)
    vix_df.drop(labels='datetime', axis=1, inplace=True)
    spx_df = dates.group_data(spx_df, 'close', method='lastValue', group=group)
    spx_df.drop(labels='datetime', axis=1, inplace=True)
    tweet_df = dates.group_data(tweet_df, 'flair', method='avg', group=group)

    return vix_df, spx_df, tweet_df


def get_fin_diff(fin_df):
    fin_df = finance.getdiff(fin_df)
    # fin_df = fin_df.pct_change()
    return fin_df


def combine_data(vix_df, spx_df, tweet_df):
    data = pd.concat([vix_df, spx_df, tweet_df], axis=1, sort=False)
    return data


def make_combined_df(vix_df, spx_df, tweet_df, group='1D'):
    vix_df, spx_df, tweet_df = group_data(vix_df, spx_df, tweet_df, group)
    vix_df = get_fin_diff(vix_df)
    spx_df = get_fin_diff(spx_df)
    vix_df, spx_df = rename_fin_columns(vix_df, spx_df)
    data = combine_data(vix_df, spx_df, tweet_df)
    return data


def remove_neutral_sentiment(tweet_df, thresh=.2):
    tweet_df = tweet_df[tweet_df['sentiment_score'].abs() > thresh]
    return tweet_df


def shift_by_delta(data, delta=0):
    data['vix_close'] = data['vix_close'].shift(delta)
    data['spx_close'] = data['spx_close'].shift(delta)
    return data


def rename_fin_columns(vix_df, spx_df):
    vix_df = vix_df.rename(columns={'close': 'vix_close'})
    spx_df = spx_df.rename(columns={'close': 'spx_close'})
    return vix_df, spx_df


def calc_corr(data):
    return data.corr()

def make_flair_sentiment(tweet_df):
    tweet_df['flair'] = [sentiment.make_sentiment(txt, model='flair') for txt in tweet_df['text']]
    return tweet_df



if __name__ == "__main__":
    import sentiment.clean_tweets as clean
    #vix_df, spx_df, tweet_df = fetch_data()


    '''
    # new_column("tweets", 'flair')
    df = pd.read_csv("tweets2.csv")
    df = df.drop("tweet_id.1", axis=1)
    df = df.set_index("tweet_id", drop=True)
    df = replace_nan_none(df)
    df = df.rename(columns = {'text':'clean_text'})
    update.new_column("tweets", "clean_text", datatype="VARCHAR(350)")
    update.add_flair(df, column_name='clean_text')
    '''

    #tweet_df = clean.remove_all_urls(tweet_df)
    #print(tweet_df.loc["1249003841732870147"]['text'])

    #print(sentiment.make_sentiment("hello i am happy", model='flair'))
    #vix_df, spx_df, tweet_df = fetch_data()
    #s1 = "About to go live with Jon and Pete Najarian in 5-10 minutes.Streaming live and FREE: https://t.co/" \
    #   "bpz9tC5Rji"
    #s2 = "About to go live with Jon and Pete Najarian in 5-10 minutes.Streaming live and FREE"
    #score1 = sentiment.make_sentiment(s1, model='flair')
    #score2 = sentiment.make_sentiment(s2, model='flair')
    #print(score1, score2)
    """group = 'T'
    vix_df, spx_df, tweet_df = fetch_data()
    tweet_df = make_flair_sentiment(tweet_df)
    tweet_df.to_csv("tweets.csv")
    # tweet_df=remove_neutral_sentiment(tweet_df)
    data = make_combined_df(vix_df, spx_df, tweet_df, group)
    data['datetime'] = data.index
    data2 = data.copy(deep=True)
    data2 = shift_by_delta(data2, delta=1)
    print(calc_corr(data))

    data.plot(x='flair', y='spx_close', kind='scatter')
    plt.show()

    # Calculate and update vix difference

    # Concatonate dataframes"""
