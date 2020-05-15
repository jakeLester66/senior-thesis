## update.py

from database.config import create_cnx


def new_column(table_name, column_name, datatype="DECIMAL(5,2)"):
    cnx = create_cnx()
    cursor = cnx.cursor()
    cursor.execute("ALTER TABLE " + str(table_name) + " ADD " + str(column_name) + " " + str(datatype))
    cursor.close()
    cnx.close()


def add_flair(data, table_name="tweets", column_name="flair", primary_key="tweet_id"):
    """
    adds data to column
    :param data: dataframe
    :param table_name: string of table in DB
    :param column_name: string of column in DB. Must be same as column name in data to add
    :param primary_key: string primary key in DB. Must be same as index in data.
    :return: None
    """
    cnx = create_cnx()
    cursor = cnx.cursor()

    query = "UPDATE " + str(table_name) + \
            " SET " + str(column_name) + " = %s " + \
            "WHERE " + str(primary_key) + " = %s"

    val = [(row[str(column_name)], str(tweet_id))
           for tweet_id, row in data.iterrows()]

    cursor.executemany(query, val)
    cnx.commit()
    print(cursor.rowcount, "row(s) affected")
    cursor.close()
    cnx.close()


def fill_table(data, table_name, column_name, primary_key):
    """
    adds data to column
    :param data: dataframe
    :param table_name: string of table in DB
    :param column_name: string of column in DB. Must be same as column name in data to add
    :param primary_key: string primary key in DB. Must be same as index in data.
    :return: None
    """
    cnx = create_cnx()
    cursor = cnx.cursor()

    query = "UPDATE " + str(table_name) + \
            " SET " + str(column_name) + " = %s " + \
            "WHERE " + str(primary_key) + " = %s"

    val = [(row[str(column_name)], str(tweet_id))
           for tweet_id, row in data.iterrows()]

    cursor.executemany(query, val)
    cnx.commit()
    print(cursor.rowcount, "row(s) affected")
    cursor.close()
    cnx.close()


def add_corelations(data, table_name="corelations"):
    import common.misc as misc
    cnx = create_cnx()
    cursor = cnx.cursor()

    query = "INSERT INTO " + table_name + "(`group`, `delta`, `spx:tweet`, `vix:tweet`, `spx:vix`) " + \
            "Values(%s, %s, %s, %s, %s)"

    data = misc.replace_nan_none(data)
    # data['spx:tweet'] = np.where(data['spx:tweet'].isnull(), None, data['spx:tweet'])
    # data['vix:tweet'] = np.where(data['vix:tweet'].isnull(), None, data['vix:tweet'])
    # data['spx:vix'] = np.where(data['spx:vix'].isnull(), None, data['spx:vix'])

    val = [
        (index[0],
         index[1],
         row['spx:tweet'],
         row['vix:tweet'],
         row['spx:vix'])
        for index, row in data.iterrows()]

    cursor.executemany(query, val)
    cnx.commit()


def add_rows(vals, query):
    """
    Update mysql table with values
    :param vals: list of tuples
    :param query: string syntactically correct mysql query
    :return: None
    """
    cnx = create_cnx()
    cursor = cnx.cursor()
    cursor.executemany(query, vals)
    cnx.commit()
