import os
import P1
from collections import defaultdict

#set current working directory to file location
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

import P1
import P2


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
    
    while len(dist_Matrix) > 1:
        n,m = find_mat_min_but_0(dist_Matrix)        
        
        if n < m:
            labels[n] = ('(%s, %s)' % (labels[n],labels[m]))
            labels.pop(m)
        else:
            labels[m] = ('(%s, %s)' % (labels[m],labels[n]))
            labels.pop(n)
        
        #remove unneeded colum
        for i in range(len(dist_Matrix)):
            dist_Matrix[i].pop(m)
        
        #recalc second row and remove first row (n)
        for j in range(1,len(dist_Matrix[0])):
            dist_Matrix[1][j] = (dist_Matrix[0][j]+dist_Matrix[1][j])/2
        
        #remove first row
        dist_Matrix.pop(n)
        
        #element j j will be 0 again
        for z in range(len(dist_Matrix)):
            dist_Matrix[z][z] = 0
    
    returnstring = ''.join(labels)
        
    return returnstring
        
def find_mat_min_but_0(matrix):
    """
    Fiinds the min value in a matrix which is not a 0 and returns 
    its n m coordinates
    Parameters
    ----------
    matrix : list of list 
        distance matrix of two species.

    Returns
    -------
    n and m coordinates.

    """
    
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
    
    #replace input values again with 0
    for line in matrix:
        i = 0
        for element in line:
            if element == 999999:
                line[i] = 0
            i += 1
        
    return(n,m)
