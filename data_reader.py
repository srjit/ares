import psycopg2
import config
import pandas as pd

__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"


def postgres_to_dataframe():
    """

    """
    cfg = config.read()
    host = cfg.get("postgres","host")
    database = cfg.get("postgres","database")
    user = cfg.get("postgres","user")
    password = cfg.get("postgres","password")
    table = cfg.get("postgres","table")

    conn_str = "host={} dbname={} user={} password={}".format(host, database, user, password)
    conn = psycopg2.connect(conn_str)

    return pd.read_sql('select * from ' + table, con=conn)

