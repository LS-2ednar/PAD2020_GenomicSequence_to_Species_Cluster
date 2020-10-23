import copy

def scoring_matrix(seq1, seq2):
    """
    generate a scoring matrix for two dna sequences

    Parameters
    ----------
    seq1 : String
        First DNA sequence to allign.
    seq2 : String
        Second DNA sequence to allign.

    Returns
    -------
    matrix : list of lists
        containing the scoring for the DNA alignment.

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
    #prepare first row and first colum
    for n in range(len(matrix[0])):
        if n != 0:
            matrix[0][n] = n*-6
    for m in range(len(matrix)):
        if m != 0:
            matrix[m][0] = m*-6
            
    #calculate scoring
    for n in range(len(matrix)):
        for m in range(len(matrix[0])):
            if n != 0 and m != 0:
                vl = matrix[n][m-1]-6
                vt = matrix[n-1][m]-6
                if seq1[n] == seq2[m]:
                    vd = matrix[n-1][m-1]+5
                else:
                    vd = matrix[n-1][m-1]-2
                    
                #which element will be inserted in matrix ???
                if max(vd,vl,vt) == vd:
                    matrix[n][m] = vd
                    tbmat[n][m] = (n-1,m-1)
                    
                elif max(vd,vl,vt) == vl:
                    matrix[n][m] = vl
                    tbmat[n][m] = (n,m-1)
                    
                else:
                    matrix[n][m] = vt 
                    tbmat[n][m] = (n,m-1)
    ###                
    # need a function to determine the max value in the matrix for  traceback
    # tbmat will be used afterwards to do the alignment
    ###
    return(matrix)


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
