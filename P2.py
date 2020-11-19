from P1 import is_dna                                
import copy
import os

#set current working directory to file location
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


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
    #Check if listOfTuples is a list of tuples with strings and DNA
    check = True 
    #1 Check Input is list
    if isinstance(listOfTuples, list) == False:
        check = False
    
    #Check Contents of list for being tuples with only strings
    i = 0
    while len(listOfTuples) > i:
        #check if the contents of the list are tuples
        if isinstance(listOfTuples[i], tuple) == False:
            check = False
            break
        #check if the containts of the tuples are strings
        elif isinstance(listOfTuples[i][0], str) == False or (isinstance(listOfTuples[i][1], str) == False or is_dna(listOfTuples[i][1]) == False):
            check = False
            break
        i += 1
        
    #final evalauation if data is usable
    if check == False:
        raise TypeError ('malformed input')
    
    #initialize returndict
    returndict = dict()
    i = 0
    #loops true the listOfTuples and get scores and aligned sequences
    while len(listOfTuples) > i:
        for j in range(i+1,len(listOfTuples)):
            score = scoring_matrix(listOfTuples[i][1], listOfTuples[j][1])
            aseqs = alline(score[0],score[1],score[2],score[3])
            returndict[(i,j)] = (aseqs[0],aseqs[1])
            
        i += 1
    return(returndict)

def scoring_matrix(seq1, seq2):
    """
    Takes two DNA sequences and creates a corsiponding a scoring and a 
    trackback matrix, aswell as modified DNA-Sequence1 and DNA-Sequence2

    Parameters
    ----------
    seq1 : string
        DNA-Sequence 1.
    seq2 : string
        DNA-Sequence 2.

    Returns
    -------
    retele: list of (Scoringmatrix, Tracbackmatrix, modified DNA-Sequence 1 
                     and modified DNA-Sequence 2)
        Discription:
        Scoringmatrix (list of list of integers)
        Tracbackmatrix(list of list of strings) 
        modified DNA-Sequence1 (string)
        modified DNA-sequence2 (string).

    """
    try:
        is_dna(seq1)
    except:
        raise TypeError ('wrong format')
            
    try:
        is_dna(seq2)
    except:
        raise TypeError ('wrong format')
        
    #increase sice of matrixices as needed for scoring matrix
    seq1 = '0' + seq1
    seq2 = '0' + seq2
    #initialize matrix
    matrix = []        
            
    while len(matrix) < len(seq1):
        matrix.append([])
        while len(matrix[-1]) < len(seq2):
            matrix[-1].append(0)
    #copy matrix for traceback later and replace [0][0] with letter E
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
            
    #calculate scoring for scoring matrix and get origin in tracback matrix
    for n in range(len(matrix)):
        for m in range(len(matrix[0])):
            if n != 0 and m != 0:
                vl = matrix[n][m-1] - 6
                vt = matrix[n-1][m] - 6
                if seq1[n] == seq2[m]:
                    vd = matrix[n-1][m-1] + 5
                else:
                    vd = matrix[n-1][m-1] - 2
                    
                #fill scoring values and tracback origin
                if max(vd,vl,vt) == vd:
                    matrix[n][m] = vd
                    tbmat[n][m] = 'D'
                    
                elif max(vd,vl,vt) == vl:
                    matrix[n][m] = vl
                    tbmat[n][m] = 'L'
                    
                else:
                    matrix[n][m] = vt 
                    tbmat[n][m] = 'T'
    
    #put returnelements in a list
    retele = [matrix,tbmat,seq1,seq2]
    return(retele)

def find_mat_max_corr(matrix):
    """
    Find the indices of the max value inside of a scoring matrix 
    Parameters. 
    ----------
    matrix : list of lists of numbers
        Scoring matrix with numbers.

    Returns
    -------
    n & m: Indices n and m.

    """
    #create an empty list for all max values in all lines
    maxInLine = []
    n = 0
    m = 0
    
    #fill the maxInLine lsit with max values of each line
    for line in matrix:
        maxInLine.append(max(line))
        #get n index for the max in the matrix 
        for element in maxInLine:
            while maxInLine[n] != max(maxInLine):
                n += 1
    #get the m index
    while matrix[n][m] != max(matrix[n]):
        m +=1   
    return(n,m)
            

def alline(matrix, tbmat, seq1, seq2):
    """
    Allines two sequences (seq1 and seq2) to oneanother by checking the values 
    useing a scoring and traceback matrix.

    Parameters
    ----------
    matrix : list of lists of integers
        Soring matrix.
    tbmat : list of lists of strings
        Traceback matrix.
    seq1 : string
        DNA-sequence 1 to aligne.
    seq2 : string
        DNA-sequence 2 to aligne.

    Returns
    -------
    aseq1 & aseq2: two strings of aligned sequences 1 and 2.

    """
    
    #initialize aligned sequences 1 and 2
    aseq1 = []
    aseq2 = []
    
    #find starting location to begin traceback
    start = find_mat_max_corr(matrix)
    n = start[0]
    m = start[1]
    
    #ensure final alignement
    #comapre n with len seq1 without 0
    nleft = len(seq1)-n-1
    #compare m with len seq2 without 0
    mleft = len(seq2)-m-1
    
    #traceback and writing the characters of the dna sequeces in lists 
    while tbmat[n][m] != 'E':
        if tbmat[n][m] == 'D':
            aseq1.append(seq1[n])
            aseq2.append(seq2[m])
            n -= 1
            m -= 1
            
        elif tbmat[n][m] == 'L':
            aseq1.append('-')
            aseq2.append(seq2[m])
            n  = n
            m -= 1
            
        else:
            aseq1.append(seq1[n])
            aseq2.append('-')
            n -= 1
            m  = m
    
    #formating for return lists become strings
    aseq1 = ''.join(aseq1)[::-1]
    aseq2 = ''.join(aseq2)[::-1]                                 
    
    #add missing values to aseq1 and aseq2 due to not starting traceback 
    #in bottom rihgt corner
    for i in range(nleft):
        aseq1 = aseq1+(seq1[::-1][i])
        
    for j in range(mleft):
        aseq2 = aseq2+(seq2[::-1][j])
    
    #adjusting of aseq1 and aseq2 to have equal length
    while len(aseq1) > len(aseq2):
        aseq2 = aseq2+'-'
        
    while len(aseq1) < len(aseq2):
        aseq1 = aseq1+'-'
        
    return(aseq1,aseq2)

def print_matrix(matrix):
    """
    Trys to print each line of a matrix in a nice format otherwise it prints 
    each line

    Parameters
    ----------
    matrix : list of lists
        A Matrix in form of a list of lists.

    Returns
    -------
    matrix: the given input Matrix

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