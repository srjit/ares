from gensim.models.keyedvectors import KeyedVectors

import numpy as np
import pandas as pd

__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"



model = KeyedVectors.load_word2vec_format('/media/sree/venus/pre-trained-models/GoogleNews-vectors-negative300.bin', binary=True)


def tovector(words):
    vector_array = []
    for w in words:
        try:
            vector_array.append(model[w])
        except:
            continue
    vector_array = np.array(vector_array)
    v = vector_array.sum(axis=0)
    return v / np.sqrt((v ** 2).sum())



def get_vectorizer_model():
    """
    """
    return model




csv_input = "/home/sree/code/ares/data/op_trial1.csv"
data = pd.read_csv(csv_input, sep="\t")

#test on a sample
test_string = data['cleaned_html'][0]
vector = toVector(test_string)

data["vector"] = data['cleaned_html'].apply(lambda x: tovector(str(x).split(" ")))
data.to_csv("/home/sree/op_vectorized.csv", sep="\t")





