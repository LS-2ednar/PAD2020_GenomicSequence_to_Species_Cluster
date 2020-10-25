import copy

def scoring_matrix(seq1, seq2):
    """
    Takes two DNA sequences adn modives them. Creates a Scoring matrix and 
    a Trackback matrix

    Parameters
    ----------
    seq1 : TYPE
        DESCRIPTION.
    seq2 : TYPE
        DESCRIPTION.

    Returns
    -------
    Scoringmatrix, Tracbackmatrix, modified DNA-Sequence1 
    and modified DNA-sequence2.

    """
    #increase sice of matrixices as needed
    seq1 = '0' + seq1
    seq2 = '0' + seq2
    #initialize matrix
    matrix = []
    
    while len(matrix) < len(seq1):
        matrix.append([])
        while len(matrix[-1]) < len(seq2):
            matrix[-1].append(0.0)
    #copy matrix for traceback later
    tbmat = copy.deepcopy(matrix)
    #prepare first row and first colum of matrix and tbmatrix
    for n in range(len(matrix[0])):
        if n != 0:
            matrix[0][n] = n*-6
            tbmat[0][n] = (0,n-1)
    for m in range(len(matrix)):
        if m != 0:
            matrix[m][0] = m*-6
            tbmat[m][0] = (m-1,0)
            
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
                    tbmat[n][m] = (n-1,m-1)
                    
                elif max(vd,vl,vt) == vl:
                    matrix[n][m] = vl
                    tbmat[n][m] = (n,m-1)
                    
                else:
                    matrix[n][m] = vt 
                    tbmat[n][m] = (n,m-1)
    retele = [matrix,tbmat,seq1,seq2]
    return(retele)

def find_mat_max_corr(matrix):
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
        
    return(n,m)

def alline(matrix, tbmat, seq1, seq2):
    #initialize returning order as1 and as2 
    as1 = []
    as2 = []
    #initialize aseq1 and aseq2 which are alignet sequences
    aseq1 = []
    aseq2 = []
    #get corrdinates from highest value in scoring matrix
    start = find_mat_max_corr(matrix)
    #start traceback
    while tbmat[start[0]][start[1]] != 0.0:
        as1.append(start[0]+1)
        as2.append(start[1]+1)
        try:
            start = (tbmat[start[0]][start[1]][0],tbmat[start[0]][start[1]][1])
        except:
            try:
                as1.append(start[0]+1)
                as2.append(start[1]+1)
            except:
                break
    #sort for ease of use
    as1 = sorted(as1)
    as2 = sorted(as2)
    
    #the following part needs some more refinement it seems that sequence two does
    #does not behave as intendet!!!
    
    #allign dna
    for n in as1:
        if len(as1) == len(seq1):
            if as1[n] == as1[n-1]:
                print('-')
            else:
                print(seq1[n])
    
    # for m in as2:
    #     if as2[m] == as2[m-1]:
    #         print('-')
    #     else:
    #         print(seq2[m])
    
    
    # print(aseq1, aseq2)

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
                pline.append('%4i' % element)
            print(pline)
        return(matrix)
    except:
        for line in matrix:
            print(line)
    return(matrix)
