from sklearn.metrics.pairwise import cosine_similarity
import operator
import gc
import pandas as pd
import json

__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"

## Source : 
## http://blog.christianperone.com/2013/09/machine-learning-cosine-similarity-for-vector-space-models-part-iii/

## uses only words from current set of documents


input = "/home/sree/code/ares/data/op_trial1.csv"

data = pd.read_csv(input, sep="\t")
data.rename(columns={'Unnamed: 0': 'index'}, inplace=True)
print(data.columns)

documents_list = documents_list = [doc if str(doc) != "nan" else "" for doc in data.cleaned_html.tolist() ]
documents = tuple(documents_list)


from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

similarity_dictionary = {}

output_folder = "/home/sree/code/ares/similarity_results_sklearn"

for i in range(len(similarity_matrix)):
    print("Processing index ", i)
    filename = output_folder + "/" + str(i + 1) + ".txt"
    test_row = similarity_matrix[i]
    _map = {}

    # import ipdb
    # ipdb.set_trace()

    # for index, value in enumerate(test_row):
    #     _map[index] = value
    _tmp = dict(enumerate(test_row))
    _tmp = dict(sorted(_tmp.items(), key=operator.itemgetter(1), reverse=True))
    _tmp = {k:v for k,v in _tmp.items() if v != 0.0}

    if len(_tmp) > 0:
        with open(filename, "w") as f:
            f.write(json.dumps(_tmp, indent=4))

    del _tmp
    gc.collect()



# import operator
# for i in range(len(similarity_matrix)):
#     print("Working on index", i)
#     test_row = similarity_matrix[i]
#     _map = {}

#     # for index, value in enumerate(test_row):
#     #     _map[index] = value
#     _tmp = dict(enumerate(test_row))
#     similarity_dictionary[i] = sorted(_tmp.items(), key=operator.itemgetter(1))    
#     del _tmp
#     gc.collect()
     

#print("Most similar documents:")



# import operator
# for key,value in similarity_dictionary.items():
#     similarity_dictionary[key] = sorted(value.items(), key=operator.itemgetter(1))


# for row_id, comparison_values in enumerate(similarity_matrix):
#     similarity_dictionary[row_id] = {}
#     for idx,value in enumerate(comparison_values):
#         similarity_dictionary[row_id][idx] = value


        



# similarity_matrix = [list(row) for row in similarity_matrix]
# similarity_dictionary = {_idx:{} for _idx in range(len(data))}

# for k, v in similarity_dictionary.items():
#     similarity_dictionary[k] = similarity_dictionary

# tfidf_vectorizer = TfidfVectorizer()
# tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

    


