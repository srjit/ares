import connector
import cleaner
import utils
import config

import gc
from textstat import textstat
from readcalc import readcalc

import text_simplicity


import similarity

__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"

cfg = config.read()

data = connector.postgres_to_dataframe()

data['index'] = data.index


## Preprocessing Steps
data['value'] = data['value'].apply(lambda x: cleaner.replace_null_with_empty_string(x))
data['readable_text'] = data['value'].apply(lambda x: cleaner.get_readable_text(x))
data['processed_value'] = data['value'].apply(lambda x: cleaner.clean_html_and_extract_text(x))

## Adding a column to count the number of words
data['word_count'] = data['processed_value'].apply(lambda x: utils.count_words(x))


print("Collecting text statistics...")

## Collect text stats from Readcalc https://pypi.python.org/pypi/ReadabilityCalculator
text_simplicity.get_readability_scores_from_readcalc(data)

## Text statistics from textstat
#text_simplicity.get_readability_scores_from_textstat(data)



print("Beginning to write data to postgres")
connector.updated_input_dataframe_to_postgres(data)

## Quality check - writing to csv
checkpoint1_name = cfg.get('checkpoint','ch1')
data.to_csv(checkpoint1_name, sep="\t")

## calculate similarity with
checkpoint2_name = cfg.get('checkpoint','ch2')

document_ids  = data['id'].tolist()
documents_list = data.processed_value.tolist()

vector_type = cfg.get('vector','type')
output = similarity.get_similarity(vector_type, documents_list, document_ids)

#write output to csv file
utils.output_to_csv(vector_type, output, document_ids, checkpoint2_name)

## writeback to postgres
connector.csv_to_postgres(checkpoint2_name)
