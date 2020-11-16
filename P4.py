import os

#set current working directory to file location
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

import P1


def Cluster(dist_Matrix, listOflabels):
    """
    

    Parameters
    ----------
    dist_Matrix : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    
    labels = listOflabels
    
    while len(dist_Matrix) != 2:
        
        #find location of minium in matrix
        n,m = find_mat_min_but_0(dist_Matrix)
        
        #put togehter what needs to be together
        labels[n] = (labels[n], labels[m])
        labels.pop(m)
        
        #recalc of matrix
        for element in range(len(dist_Matrix[0])):
            dist_Matrix[1][element] = (dist_Matrix[1][element] + dist_Matrix[0][element])/2
        
        for line in range(len(dist_Matrix)):
            dist_Matrix[line][1] = (dist_Matrix[line][1] + dist_Matrix[line][0]) /2 
        
        #edit matrix size
        #remove row
        dist_Matrix.pop(n)
        #remove col
        for line in dist_Matrix:
            line.pop(m)
        
        #correct new 0,0 value
        dist_Matrix[0][0] = 0
    cluster = '(%s, %s)' % (labels[0],labels[1])
    # print(cluster)
    return cluster
        
def find_mat_min_but_0(matrix):
    
    minInLine = []
    n = 0
    m = 0
    #remove zeros for acual minmum location
    for line in matrix:
        i = 0
        for element in line:
            if element == 0:
                line[i] = 999999
            i += 1
    
    #finding mimum
    for line in matrix:
        minInLine.append(min(line))
        for element in minInLine:
            while minInLine[n] != min(minInLine):
                n += 1
    while matrix[n][m] != min(matrix[n]):
        m +=1   
    return(n,m)
