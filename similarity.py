import numpy as np
import pandas as pd
from gensim.models.keyedvectors import KeyedVectors
import vectorize


## https://stackoverflow.com/questions/22129943/how-to-calculate-the-sentence-similarity-using-word2vec-model-of-gensim-with-pyt



## Cosine similarity for vector space models - 

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
    


data["vector"] = data['cleaned_html'].apply(lambda x: vectorize.tovector(str(x).split(" ")))

s1 = data['vector'][0]
s2 = data['vector'][1]

distance = model.wmdistance(s1, s2)


## example distance calculation - Word mover's distance 
s1 = data['cleaned_html'][0]
s2 = data['cleaned_html'][1]



# #cosine distance 
# vectorize.model.similarity(s1,s2)

# distance = vectorize.model.wmdistance(s1, s2)
