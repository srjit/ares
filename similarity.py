import itertools
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import word2vec
import scipy.spatial.distance


__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"



    

def word2vec_similarity(documents):
    sentence_vectors = list(map(word2vec.tovector, documents))

    output_list = []
    
    for idx_root, root_vector in enumerate(sentence_vectors):
        print("Calculating similarities of:", str(idx_root))
        for idx_tmp, tmp_vector in enumerate(sentence_vectors):
            if idx_root <= idx_tmp:
                try:
                    similarity = 1 - scipy.spatial.distance.cosine(root_vector, tmp_vector)
                except:
                    similarity = 0.0
                output_list.append([idx_root, idx_tmp, similarity])
            
    return output_list


def pairwise_similarity(documents):
    """
    
    Arguments:
    - `documents`:
    """
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(tuple(documents))
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return similarity_matrix



def word2vec_cosine_similarity(documents):
    """
    
    Arguments:
    - `documents`:
    """
    pairs = list(itertools.combinations(range(len(documents)),2))
    pass



def get_similarity(type, documents):
    if type == "scikit":
        return pairwise_similarity(documents)
    elif type == "word2vec":
        return word2vec_similarity(documents)
