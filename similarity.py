
import numpy as np
import pandas as pd


__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"


input = "/home/sree/code/ares/data/op_trial1.csv"

data = pd.read_csv(input, sep="\t")
data.rename(columns={'Unnamed: 0': 'index'}, inplace=True)
print(data.columns)



similarity_dictionary = {_idx:{} for _idx in range(len(data))}

for k, v in similarity_dictionary.items():
    similarity_dictionary[k] = similarity_dictionary
    



