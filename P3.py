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
        
    #3 Check sequences contain aligned DNA and are of equal length
    for key in dict_alignedSequences:
        if is_aligned_dna(dict_alignedSequences[key][0]) == False or is_aligned_dna(dict_alignedSequences[key][1]) == False:
            check = False
            break
        if len(dict_alignedSequences[key][0]) != len(dict_alignedSequences[key][1]):
            check = False
            break
            
    #final evalauation if data is usable
    if check == False:
        raise TypeError ('malformed input')
    
    #get number of sequences
    matrixdim = howmany_sequences(dict_alignedSequences)
    #initialize dist matrix
    distMatrix = init_Dist_Matrix(matrixdim)
    
    
    for i in dict_alignedSequences.keys():
        # useing the key i to get the corisponding aligned sequences 
        seq = dict_alignedSequences[i]
        #calculate distances between the sequences
        distance = calculate_distance(seq[0],seq[1])
        #markdown result at the corrsiponding place in the distmatrix
        distMatrix[i[0]][i[1]] = distance
        distMatrix[i[1]][i[0]] = distance
    
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
    #initialize number of pairs as 0
    pairs = 0
    #count pairs
    for n in listOfTuples:
        pairs += 1
    k = 1
    #find number of initial sequences    
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
    seqlen = 0 #sequence length
    
    #cout the sequence length and mismatches
    for i in range(len(seq1)):
        if seq1[i]!='-' and seq2[i]!='-':
            seqlen += 1
            if seq1[i] != seq2[i]:
                mmcounter += 1
    #compute p
    p = (mmcounter/seqlen)
    #adjust p 
    if p >= 0.75:
        pcorr = float(30)
    else:
        pcorr = (-3/4)*np.log(1-((4/3)*p))
    
    return(pcorr)

def is_aligned_dna(sequence):
    """
    Checks if the length of a string is 0 when all DNA bases are removed.

    Parameters
    ----------
    sequence : string of DNA

    Returns
    -------
    bool
        True if len(seq) == 0
        otherwise False 

    """
    #ensure that the given sequence is uppercase
    sequence = sequence.upper()
    
    #replace all A C G and T and compare length with 0
    if len(sequence.replace("A", "").replace("C", "").replace("G","").replace("T","").replace("-","")) == 0:
        return True
    else:
        return False