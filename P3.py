import os

#set current working directory to file location
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

import numpy as np


def howmany_sequences(listOfTuples):
    """
    Determines the amount of DNA sequences which where aligned

    Parameters
    ----------
    listOfTuples : A list of Tuples
        list of tuples .

    Returns
    -------
    None.

    """
    pairs = 0
    for n in listOfTuples:
        pairs += 1
    k = 1    
    while k*(k-1) != pairs*2:
        k += 1
    return(k)

def init_Dist_Matrix(length):
    """
    initialies a distance matrix containing notthing but 'X'

    Parameters
    ----------
    length : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    dist_matrix = []
        
    while len(dist_matrix) < length:
        dist_matrix.append([])
        while len(dist_matrix[-1]) < length:
            dist_matrix[-1].append(0)
    
    # print_matrix(dist_matrix) #just for the visuals can be removed later
    return(dist_matrix)

def calculate_distance(seq1,seq2):
    """
    

    Parameters
    ----------
    seq1 : TYPE
        DESCRIPTION.
    seq2 : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    mmcounter = 0 #mismatchcount
    seqlen = 0
    
    for i in range(len(seq1)):
        if seq1[i] or seq2[i] != '-':
            seqlen += 1
            if seq1[i] != seq2[i]:
                mmcounter += 1
    p = (mmcounter/i)
    pcorr = -1*(3/4)*np.log(1-(4/3*p))
    
    #distance when biger 0.75
    if pcorr >= 0.75:
        pcorr = 30
        
    return(pcorr)
    
def ComputeDistMatrix(dictWithKeysAsTuplesAndTuplesAsElements):
    """
    

    Parameters
    ----------
    dictWithKeysAsTuplesAndTuplesAsElements : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    try:
        matrixdim = howmany_sequences(dictWithKeysAsTuplesAndTuplesAsElements)
        distMatrix = init_Dist_Matrix(matrixdim)
        for i in dictWithKeysAsTuplesAndTuplesAsElements.keys():
            # print(i)
            # print(i[0], i[1])
            seq = dictWithKeysAsTuplesAndTuplesAsElements[i]
            # print(seq)
            distance = calculate_distance(seq[0],seq[1])
            distMatrix[i[0]-1][i[1]-1] = distance
            distMatrix[i[1]-1][i[0]-1] = distance
    except:
        'malformed input'
    return(distMatrix)

