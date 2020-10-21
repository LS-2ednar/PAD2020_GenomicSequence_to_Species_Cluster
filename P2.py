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
    seq1 = '0' + seq1
    seq2 = '0' + seq2
    matrix = []
    line = []
    n = -1
    for i in seq1:
        n += 1
        m = -1
        for j in seq2:
            m += 1
            if i == '0':
                line.append(m*-6)
            elif j == '0':
                line = [n*-6]
            else:
                #fill other values 
                if i == j:
                    v1 = int(matrix[n-1][m-1])+5
                else:
                    v1 = int(matrix[n-1][m-1])-2
                v2 = int(matrix[n-1][m])-6
                v = max(v1,v2)
                line.append(v)
        matrix.append(line)
    return matrix

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
    for line in matrix:
        pline =[]
        for element in line:
            pline.append('%3i' % element)
        print(pline)    
    return(matrix)
