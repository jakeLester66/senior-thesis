import mysql.connector
import logging
logger = logging.getLogger()

def create_cnx():
    cnx = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='password',
        port='1234',
        database='sproj',
        auth_plugin='mysql_native_password'
    )

    #todo make exceptions with logging. refer to streamers/config.py
    logger.info("Mysql connection created")
    return cnx