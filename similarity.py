import numpy as np
import pandas as pd
from gensim.models.keyedvectors import KeyedVectors
import vectorize
import scipy.spatial.distance

import operator
import gc

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


sentence_vectors = data["vector"].tolist()

similarity_dictionary = {}

output_folder = "/home/sree/code/ares/similarity_results_word2vec"        

for i, root_vector in enumerate(sentence_vectors):

    output_file = output_folder + "/" + i + ".txt"
    tmp = {}

    print("Calculating similarity of vector" , i)
    similarity_dictionary[i] = {}
    for j, tmp in enumerate(sentence_vectors):
#        print(vectorize.model.wmdistance(root_vector,tmp))
        try:
#            similarity_dictionary[i][j] = scipy.spatial.distance.cosine(root_vector, tmp)
            tmp = scipy.spatial.distance.cosine(root_vector, tmp)
        except:
#            similarity_dictionary[i][j] = 0.0
            tmp = 0.0

        _tmp = dict(sorted(_tmp.items(), key=operator.itemgetter(1), reverse=True))
        _tmp = {k:v for k,v in _tmp.items() if v != 0.0}

        if len(_tmp) > 0:
            with open(filename, "w") as f:
                f.write(json.dumps(_tmp, indent=4))

         del _tmp
         gc.collect()




for i 


# s1 = data['vector'][0]
# s2 = data['vector'][1]

# distance = model.wmdistance(s1, s2)


## example distance calculation - Word mover's distance 
s1 = data['cleaned_html'][0]
s2 = data['cleaned_html'][1]



# #cosine distance 
# vectorize.model.similarity(s1,s2)

# distance = vectorize.model.wmdistance(s1, s2)
