import os
import csv


__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"


def count_words(text):
    return len(text.split())


def list_to_csv(lists, document_ids, output_file):

    batchsize = 10
    headers = [["index1","index2","similarity"]]
    
    if os.path.isfile(output_file):
        os.remove(output_file)

    with open(output_file, "w") as sim_pair_file:

        writer = csv.writer(sim_pair_file)
        for slider_index in range(0, len(lists), batchsize):
            begin_index = slider_index
            end_index = slider_index + batchsize

            similarities_for_range = lists[begin_index: end_index]
            
            writer.writerows(similarities_for_range)
               
        
        
    

def matrix_to_pairwise_csv(matrix, document_ids, output_file):
    """
    
    Arguments:
    - `matrix`:
    """

    batchsize = 100
    headers = [["index1","index2","similarity"]]
    
    if os.path.isfile(output_file):
        os.remove(output_file)

    with open(output_file, "w") as sim_pair_file:

        writer = csv.writer(sim_pair_file)
#        writer.writerows(headers)        

        for slider_index in range(0, len(matrix), batchsize):
            begin_index = slider_index
            end_index = slider_index + batchsize
            
            similarities_for_range = [[document_ids[begin_index + i], document_ids[j], matrix[i,j]] 
                                         for i in range(begin_index, end_index) 
                                         for j in range(len(matrix))]

            writer.writerows(similarities_for_range)




def output_to_csv(_type, output, document_ids, output_file):
    if _type == "scikit":
        return matrix_to_pairwise_csv(output, document_ids, output_file)
    elif _type == "word2vec":
        return list_to_csv(output, document_ids, output_file)
    
