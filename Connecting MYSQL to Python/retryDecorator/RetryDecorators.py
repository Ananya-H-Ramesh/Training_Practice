
import mysql.connector
import logging
from tenacity import retry, stop_after_attempt, wait_fixed
from . import config as params




@retry(wait=wait_fixed(2), stop=stop_after_attempt(3))
def connect_to_database():
    """
    Connect to a MySQL database and retrieve the list of databases.

    Returns:
        list: A list of records representing the databases.
    """
    connection = mysql.connector.connect(host=params.host, user=params.user, password=params.password)

    cursor = connection.cursor()
    cursor.execute("show databases")
    records = cursor.fetchall()

    cursor.close
    connection.close
    
    return records

