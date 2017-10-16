import data_reader
import cleaner
import utils
import config

import gc
from textstat import textstat

import similarity

__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"

cfg = config.read()

data = data_reader.postgres_to_dataframe()

## Preprocessing Steps
data['value'] = data['value'].apply(lambda x: cleaner.replace_null_with_empty_string(x))
data['processed_value'] = data['value'].apply(lambda x: cleaner.clean_html_and_extract_text(x))

## Adding a column to count the number of words
data['word_count'] = data['processed_value'].apply(lambda x: utils.count_words(x))


## Text statistics from textstat
# data['reading_ease'] = data['processed_value'].apply(lambda x: 
#                               textstat.textstat.flesch_reading_ease(str(x)) if x is not '' else 0.0)
# data['smog_index'] = data['processed_value'].apply(lambda x: 
#                               textstat.textstat.smog_index(str(x)) if x is not '' else 0.0)
# data['automated_readability_index'] = data['processed_value'].apply(lambda x: 
#                               textstat.textstat.automated_readability_index(str(x)) if x is not '' else 0.0)
# data['coleman_liau_index'] = data['processed_value'].apply(lambda x: 
#                               textstat.textstat.coleman_liau_index(str(x)) if x is not '' else 0.0)
# data['linsear_write_formula'] = data['processed_value'].apply(lambda x: 
#                               textstat.textstat.linsear_write_formula(str(x)) if x is not '' else 0.0)
# data['dale_chall_readability_score'] = data['processed_value'].apply(lambda x: 
#                              textstat.textstat.dale_chall_readability_score(str(x)) if x is not '' else 0.0)


## Quality check - writing to csv
checkpoint1_name = cfg.get('checkpoint','ch1')
data.to_csv(checkpoint1_name, sep="\t")


## calculate similarity with
checkpoint2_name = cfg.get('checkpoint','ch2')
documents_list = data.processed_value.tolist()
matrix = similarity.pairwise_similarity(documents_list)
pairwise_similarities = utils.matrix_to_rows(matrix, checkpoint2_name)






