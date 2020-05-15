## dates.py

import pandas as pd


def group_data(data, value_col_names, method="lastValue", group='1440T'):
    """
    Group data by specified method and Group value
    :param data: DataFrame with DateTime index
    :param value_col_names: List of Strings
    :param method: String in {'lastValue', 'avg', 'count'}
    :param group: String where last character is 'T' and preceding chars are Ints
    :return: DataFrame with Index and specified value_col_names grouped by group and method
    """
    df = pd.DataFrame()
    df['datetime'] = pd.to_datetime(data['datetime'])
    for value_col_name in value_col_names:
        df[value_col_name] = pd.to_numeric(data[value_col_name])
    df.set_index(df['datetime'], drop=True, inplace=True)
    if method == "lastValue":
        df = df.resample(group).last()
    elif method == "avg":
        df = df.resample(group).mean()
    elif method == 'count':
        df = df.resample(group).count()
    else:
        assert False
    return df


def standardize(data1, data2, value_col_name1, value_col_name2):
    """
    conform data1 and data2 to same date points to allow easier analysis
    Keyword arguments:
        data1 -- dictionary with keys "date" "value"
        value_col_name1 -- name of column in data1 that serves as
    :return two DataFrames with conformed datetime points
    """

    # todo assert dates sorted ascending for both data
    start_date = max(min(data1['datetime']), min(data2['datetime']))
    end_date = min(max(data1['datetime']), max(data2['datetime']))

    start_index_1 = next(x for x, date in enumerate(data1['datetime']) if date >= start_date)
    start_index_2 = next(x for x, date in enumerate(data2['datetime']) if date >= start_date)

    end_index_1 = next(x for x, date in enumerate(data1['datetime']) if date >= end_date)
    end_index_2 = next(x for x, date in enumerate(data2['datetime']) if date >= end_date)

    if data1['datetime'][end_index_1] == end_date:
        end_index_1 += 1
    if data2['datetime'][end_index_2] == end_date:
        end_index_2 += 1

    data1['datetime'], data1['datetime'] = data1['datetime'][start_index_1:end_index_1], data1['value'][
                                                                                         start_index_1:end_index_1]
    data2['datetime'], data2['datetime'] = data2['datetime'][start_index_2:end_index_2], data2['value'][
                                                                                         start_index_2:end_index_2]

    return data1, data2
