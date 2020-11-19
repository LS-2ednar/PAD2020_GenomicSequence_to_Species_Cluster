import os

#set current working directory to file location
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

import numpy as np


def ComputeDistMatrix(dict_alignedSequences):
    """
    Useing a given dict with keys containing aligned sequences numbers 
    (integers)and vlaues which are aligned DNA-sequences (strings) compute
    a distance matrix as a list of lists of floats

    Parameters
    ----------
    dict_alignedSequences : dict{(int1,int2): (aSeq1, aSeq2)}
        DESCRIPTION.

    Returns
    -------
    dist_Matrix: list of lists of floats.

    """
    
    # check if dictionary with keys as tuples containing integers and values as tuples containing strings
    check = True 
    #1 Check Input is dict
    if isinstance(dict_alignedSequences, dict) == False:
        check = False
        
    #2 Check are the keys and values tuples. Do the keys only contain integers and the vlaues only strings
    i = 0
    while len(dict_alignedSequences) > i:
        #checking for keys and values as tuples
        if isinstance(list(dict_alignedSequences.keys())[i], tuple) == False or isinstance(list(dict_alignedSequences.values())[i], tuple) == False:
            check = False
            break
        #checking keys for integers
        if isinstance(list(dict_alignedSequences.keys())[i][0], int) == False or isinstance(list(dict_alignedSequences.keys())[i][1], int) == False:
            check = False
            break
        #checking values for strings
        if isinstance(list(dict_alignedSequences.values())[i][0], str) == False or isinstance(list(dict_alignedSequences.values())[i][1], str) == False:
            check = False
            break
        #increment the counter for while loop
        i += 1
    
    #final evalauation if data is usable
    if check == False:
        raise TypeError ('malformed input')
    
    matrixdim = howmany_sequences(dict_alignedSequences)
    distMatrix = init_Dist_Matrix(matrixdim)
    for i in dict_alignedSequences.keys():
            
        seq = dict_alignedSequences[i]
            
        distance = calculate_distance(seq[0],seq[1])
        distMatrix[i[0]-1][i[1]-1] = distance
        distMatrix[i[1]-1][i[0]-1] = distance
    
    return(distMatrix)

def howmany_sequences(listOfTuples):
    """
    Determines the amount of DNA sequences which where aligned

    Parameters
    ----------
    listOfTuples : A list of Tuples
        list of tuples .

    Returns
    -------
    k:  integer
        Number of compared Sequences

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
    initialies a distance matrix containing notthing but 0.0

    Parameters
    ----------
    length : integer

    Returns
    -------
    list of lists of 0.0.

    """
    dist_matrix = []
        
    while len(dist_matrix) < length:
        dist_matrix.append([])
        while len(dist_matrix[-1]) < length:
            dist_matrix[-1].append(float(0))
    
    # print_matrix(dist_matrix) #just for the visuals can be removed later
    return(dist_matrix)

def calculate_distance(seq1,seq2):
    """
    

    Parameters
    ----------
    seq1 : string
        aligend DNA-sequence 1.
    seq2 : string
        aligend DNA-sequence 2.

    Returns
    -------
    pcorr: float
        Calculated distance value.
    """
    mmcounter = 0 #mismatchcount
    seqlen = 0
    
    for i in range(len(seq1)):
        if (seq1[i] or seq2[i]) != '-':
            seqlen += 1
            if seq1[i] != seq2[i]:
                mmcounter += 1
    p = (mmcounter/i)
    pcorr = -1*(3/4)*np.log(1-(4/3*p))
    
    #distance when pcorr is biger then 0.75
    if pcorr >= 0.75:
        pcorr = float(30)
        
    return(pcorr)
    
