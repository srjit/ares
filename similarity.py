import itertools
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"


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
