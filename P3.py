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
        The number of sequence.

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
    length : A Integer
        A integer of length n.

    Returns
    -------
        Initialies a nXn dist matrix containing only zeros.

    """
    dist_matrix = []
        
    while len(dist_matrix) < length:
        dist_matrix.append([])
        while len(dist_matrix[-1]) < length:
            dist_matrix[-1].append(0)
    return(dist_matrix)

def calculate_distance(seq1,seq2):
    """
    

    Parameters
    ----------
    seq1 : String
        DNA Sequence 1.
    seq2 : String
        DNA Sequence 2.

    Returns
    -------
        A caluclated and corrected distance value between seq1 and seq2. 

    """
    mmcounter = 0 #mismatchcount
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            mmcounter += 1
    p = (mmcounter/i)
    pcorr = -1*(3/4)*np.log(1-(4/3*p))
    return(pcorr)
    
def ComputeDistMatrix(dictWithKeysAsTuplesAndTuplesAsElements):
    """
    

    Parameters
    ----------
    dictWithKeysAsTuplesAndTuplesAsElements : TYPE
        A Dict with Tuples as Key and Tuples as Elements.

    Returns
    -------
        distMatrix which is a list of values

    """
    try:
        matrixdim = howmany_sequences(dictWithKeysAsTuplesAndTuplesAsElements)
        distMatrix = init_Dist_Matrix(matrixdim)
        for i in dictWithKeysAsTuplesAndTuplesAsElements.keys():
            seq = dictWithKeysAsTuplesAndTuplesAsElements[i]
            distance = calculate_distance(seq[0],seq[1])
            distMatrix[i[0]-1][i[1]-1] = distance
            distMatrix[i[1]-1][i[0]-1] = distance
    except:
        'malformed input'
    return(distMatrix)
