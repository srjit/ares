import psycopg2
import pandas as pd
from bs4 import BeautifulSoup

import string

import re

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


sample = data['value'].iloc[0]

null = 0
empty = 0

def check_text(html):
    global null
    global empty
    if html is not None:
        if html.strip() == "":
            print("Empty string")
            empty  += 1
            return ""
    else:
        print("Null")
        null += 1
        return ""
    return html


def clean_html(raw_html):
    
    # remove roman numberals inside brackets
    raw_html = re.sub('\([v|i|x]+\)', '', raw_html)
    raw_html = re.sub('\s\d+\s', '', raw_html)


    raw_html = bytes(raw_html, 'utf-16').decode("utf-16", 'ignore')

    cleantext = BeautifulSoup(raw_html).text
    cleantext = " ".join(cleantext.split())

    # clean all arabic numerals
    numbers = re.findall('\d+', cleantext)
    for number in numbers:
        cleantext = cleantext.replace(number, " ")
     
        
    # remove punctuations
    table = cleantext.maketrans("","", string.punctuation)
    cleantext = cleantext.translate(table)

    # remove non - ascii
    printable = set(string.printable)
    cleantext = list(filter(lambda x: x in printable, cleantext))
    cleantext = "".join(cleantext)
    
    # remove roman from string
    toremove = [' ii ',' iii ', ' iv ', ' v ', ' vi ', ' vii ', ' viii ', ' ix ', ' x ']
    text_array = cleantext.split("\s+")
    cleantext = [word.strip() for word in text_array if word not in toremove]
    cleantext = " ".join(cleantext)
    

    return cleantext.strip()



def count_words(text):
    return len(text.strip().split())

data['cleaned_value'] = data['value'].apply(lambda x: check_text(x))
data['cleaned_html'] = data['cleaned_value'].apply(lambda x: clean_html(x))
data['number_of_words'] = data['cleaned_html'].apply(lambda x: count_words(x))

data.to_csv("/home/sree/op_trial1.csv", sep="\t")
