import psycopg2
import pandas as pd

__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"


host = "localhost"
database = "business"
user = "postgres"
password = "password"

conn_str = "host={} dbname={} user={} password={}".format(host, database, user, password)

conn = psycopg2.connect(conn_str)
data = pd.read_sql('select * from textblock', con=conn)
