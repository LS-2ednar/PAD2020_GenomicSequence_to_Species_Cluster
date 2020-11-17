from P1 import is_dna                                
import copy
import os

#set current working directory to file location
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def scoring_matrix(seq1, seq2):
    """
    Takes two DNA sequences adn modives them. Creates a Scoring matrix and 
    a Trackback matrix

    Parameters
    ----------
    seq1 : string
        DNA-Sequence 1.
    seq2 : string
        DNA-Sequence 2.

    Returns
    -------
    A list containging for elements 1.Scoringmatrix, 2.Tracbackmatrix, 
    3. modified DNA-Sequence1 and 4. modified DNA-sequence2.

    """
    try:
        is_dna(seq1)
    except:
        'Wrong format'
            
    try:
        is_dna(seq2)
    except:
        'Worng format'
        
    #increase sice of matrixices as needed for scoring matrix
    seq1 = '0' + seq1
    seq2 = '0' + seq2
    #initialize matrix
    matrix = []        
            
    while len(matrix) < len(seq1):
        matrix.append([])
        while len(matrix[-1]) < len(seq2):
            matrix[-1].append(0)
    #copy matrix for traceback later
    tbmat = copy.deepcopy(matrix)
    tbmat[0][0] = 'E'
    #prepare first row and first colum of matrix and tbmatrix
    for n in range(len(matrix[0])):
        if n != 0:
            matrix[0][n] = n*-6
            tbmat[0][n] = 'L'
    for m in range(len(matrix)):
        if m != 0:
            matrix[m][0] = m*-6
            tbmat[m][0] = 'T'
            
    #calculate scoring and fill tracebackmatrix with origin (tuples)
    for n in range(len(matrix)):
        for m in range(len(matrix[0])):
            if n != 0 and m != 0:
                vl = matrix[n][m-1] - 6
                vt = matrix[n-1][m] - 6
                if seq1[n] == seq2[m]:
                    vd = matrix[n-1][m-1] + 5
                else:
                    vd = matrix[n-1][m-1] - 2
                    
                #swap 0 scoring values
                if max(vd,vl,vt) == vd:
                    matrix[n][m] = vd
                    tbmat[n][m] = 'D'
                    
                elif max(vd,vl,vt) == vl:
                    matrix[n][m] = vl
                    tbmat[n][m] = 'L'
                    
                else:
                    matrix[n][m] = vt 
                    tbmat[n][m] = 'T'
                    
    retele = [matrix,tbmat,seq1,seq2]
    return(retele)

def find_mat_max_corr(matrix):
    """
    Find the indices of the possiton of the max value inside of a matrix
    Parameters
    ----------
    matrix : list of lists
        Matrix in form of a list of lists.

    Returns
    -------
    Indices n and m as tuple.

    """
    maxInLine = []
    n = 0
    m = 0
    for line in matrix:
        maxInLine.append(max(line))
        for element in maxInLine:
            while maxInLine[n] != max(maxInLine):
                n += 1
    while matrix[n][m] != max(matrix[n]):
        m +=1   
    # print(matrix[n][m]) # just here for now can be removed later :-D
    return(n,m)
            
def print_matrix(matrix):
    """
    Allows the print of matrices for easier visual interpretation

    Parameters
    ----------
    matrix : list of lists
        A Matrix in form of a list of lists.

    Returns
    -------
    Matrix.

    """
    try:
        for line in matrix:
            pline =[]
            for element in line:
                pline.append('%3.3f' % element)
            print(pline)
        return(matrix)
    except:
        for line in matrix:
            print(line)
    return(matrix)


def alline(matrix, tbmat, seq1, seq2):
    """
    Allines two sequences to oneanother by checking the values useing a scoring
    and traceback matrix.

    Parameters
    ----------
    matrix : list of lists
        Soring matrix.
    tbmat : list of lists
        Traceback matrix.
    seq1 : string
        DNA-sequence 1 to aligne.
    seq2 : string
        DNA-sequence 2 to aligne.

    Returns
    -------
    tuple of aligned sequences 1 and 2.

    """
    
    start = find_mat_max_corr(matrix)
    n = start[0]
    m = start[1]
    aseq1 = []
    aseq2 = []
    #start traceback
    while tbmat[n][m] != 'E':
        if tbmat[n][m] == 'D':
            # print('D')
            aseq1.append(seq1[n])
            aseq2.append(seq2[m])
            n -= 1
            m -= 1
            
        elif tbmat[n][m] == 'L':
            # print('L')
            aseq1.append('-')
            aseq2.append(seq2[m])
            n  = n
            m -= 1
            
        else:
            # print('T')
            aseq1.append(seq1[n])
            aseq2.append('-')
            n -= 1
            m  = m
                  
    #remove 0 from seq1 and seq2 for to complet alignment
    seq1 = seq1.replace('0', '')
    seq2 = seq2.replace('0', '')
    
    #append missing values        
    if len(seq1) > len(aseq1):
        while len(seq1) > len(aseq1):
            aseq1.append(seq1[len(seq1)-(len(seq1)-len(aseq1))])
            
            
    if len(seq2) > len(aseq2):
        while len(seq2) > len(aseq2):
            aseq2.append(seq2[len(seq2)-(len(seq2)-len(aseq2))])    
     
    
    #check if there are maybe missing elements in the front
    if len(aseq1) < len(aseq2):
        while len(aseq1) < len(aseq2):
            aseq1.append('-')
    elif len(aseq1) > len(aseq2): 
        while len(aseq1) > len(aseq2):
            aseq2.append('-')
     #formating for return
    aseq1 = ''.join(aseq1)[::-1]
    aseq2 = ''.join(aseq2)[::-1]                                 
    
    return(aseq1,aseq2)

def AlignByDP(listOfTuples):
    """
    Alinges all DNA sequences in a list of tuples which eachother and returns
    a dictionary with the keys of the combined sequences and the corsiponding
    aligned to onanother DNA sequences
    Parameters
    ----------
    listOfTuples : A list of Tuples 
        First element is a label secnond a DNA-sequence.
    Returns
    -------
    A dictionary with tuples of the indices for the aligned dna sequences and the aligned dna sequnece as tuples.
    """
    returndict = dict()
    i = 0
    while len(listOfTuples) > i:
        for j in range(i+1,len(listOfTuples)):
            # print(j)
            score = scoring_matrix(listOfTuples[i][1], listOfTuples[j][1])
            aseqs = alline(score[0],score[1],score[2],score[3])
            returndict[(i,j)] = (aseqs[0],aseqs[1])
        i += 1
    return(returndict)
