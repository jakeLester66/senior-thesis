import requests
import pandas as pd
from bs4 import BeautifulSoup
from config import create_api
import tweepy


class FollowAccounts():
    """ """
    def __init__(self, url=r'https://www.forbes.com/sites/alapshah/2017/11/16/the-100-best-twitter-accounts-for-finance/#72997b3f7ea0'):
        self.api = create_api()
        accounts_df = self.url2table(url)
        accounts_df = self.handleExceptions(accounts_df)
        self.includeHandleID(accounts_df)
        accounts_df = self.removeUnavailable(accounts_df)
        self.df =  accounts_df

    def url2table(self, url):
        tables = pd.read_html(url)  # Returns list of all tables on page
        financial_twitter_accounts = tables[0]  # Select table of interest
        financial_twitter_accounts = financial_twitter_accounts.rename(columns=financial_twitter_accounts.iloc[0]).drop(
            financial_twitter_accounts.index[0])
        financial_twitter_accounts = financial_twitter_accounts.set_index("Twitter Handle")
        return financial_twitter_accounts

    def handleExceptions(self, df):
        return df.rename(index={"HedgeyeHWP": "HowardWPenney"})

    def includeHandleID(self, df):
        accnt_ids = []
        for handle in df.index:
            try:
                accnt_ids.append(str(self.api.get_user(handle).id_str))
            except:
                print(handle, "not found")
                accnt_ids.append(None)
        df.insert(0, "Twitter_ID", accnt_ids)
        return df

    def removeUnavailable(self, df):
        return df[df["Twitter_ID"].notnull()]


if __name__ == "__main__":
    import os
    accountsdf = FollowAccounts().df
    accountsdf.to_csv(os.getcwd()+"\\finAccounts.csv")

    """import pandas as pd

    url = r'https://www.forbes.com/sites/alapshah/2017/11/16/the-100-best-twitter-accounts-for-finance/#72997b3f7ea0'
    tables = pd.read_html(url)  # Returns list of all tables on page
    financial_twitter_accounts = tables[0]  # Select table of interest
    financial_twitter_accounts = financial_twitter_accounts.rename(columns=financial_twitter_accounts.iloc[0]).drop(financial_twitter_accounts.index[0])
    financial_twitter_accounts = financial_twitter_accounts.set_index("Twitter Handle")
    print(financial_twitter_accounts.head())

    #adding new column for twitter ids
    """

