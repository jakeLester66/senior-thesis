## update_db.py

import database.update as update
import pandas as pd

def load_flair(fp="tweets.csv"):
    tweet_data = pd.read_csv(fp, header=0, index_col="tweet_id")
    return tweet_data

def load_validate(fp="data\\validateSentiment.csv"):
    validate_data = pd.read_csv(fp, header=0, index_col=0)
    return validate_data

def update_db_validate(data):

    vals = [
        (index,
         row['sentiment'],
         row['text'],
         row['nltk'],
         row['flair']
        )
        for index, row in data.iterrows()
    ]

    query = "INSERT INTO validate (`id`, `sentiment`, `text`, `nltk`, `flair`) " + \
            "Values(%s, %s, %s, %s, %s)"

    update.add_rows(vals, query)

if __name__ == "__main__":
    #tweet_data = load_flair()
    #update.add_flair(tweet_data)
    data = load_validate()
    print(data.head())
    update_db_validate(data)