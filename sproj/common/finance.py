## finance.py

import pandas as pd

def getdiff(data):
    """

    :param data: DataFrame with "datetime" and "value" columns
    :return: Dataframe with one less row and the delta of each value column at the later datetime
    """

    return data.diff()