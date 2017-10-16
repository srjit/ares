import os
import csv


__author__ = "Sreejith Sreekumar"
__email__ = "sreekumar.s@husky.neu.edu"
__version__ = "0.0.1"


def count_words(text):
    return len(text.split())

def write_to_csv(sim_pair_file, similaities_for_range):
    """
    """
    writer = csv.writer(sim_pair_file)
    writer.writerows(similaities_for_range)


def matrix_to_rows(matrix, output_file):
    """
    
    Arguments:
    - `matrix`:
    """
    l = []
    batchsize = 10
    
    if os.path.isfile(output_file):
        os.remove(output_file)

    with open(output_file, "a+") as sim_pair_file:

        for slider_index in range(0, len(matrix), batchsize):
            begin_index = slider_index
            end_index = slider_index + batchsize
            
            similaities_for_range = [[i, j, matrix[i,j]] 
                                         for i in range(begin_index, end_index) 
                                         for j in range(len(matrix))]
            
            write_to_csv(sim_pair_file, similaities_for_range)
