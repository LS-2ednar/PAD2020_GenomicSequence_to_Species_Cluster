import os

#set current working directory to file location
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


def Cluster(dist_Matrix, listOflabels):
    """
    Cluster the different Labels are put in a binary tree in string format 
    based on distance Matrix
    Parameters
    ----------
    dist_Matrix : list of list of floats
    
    listOflabels : list of strings

    Returns
    -------
    returnstring: by parentesis clustered labels

    """
    
    # check if List of Tuples with strings and DNA
    check = True
    
    i = 0
    #check if it is a list of list
    if isinstance(dist_Matrix, list) == False:
        check = False
        
    while len(dist_Matrix) > i:
        if isinstance(dist_Matrix[i], list) == False:
            check = False
            break
        for n in range(len(dist_Matrix[i])):
            if isinstance(dist_Matrix[i][n], float) == False:
                print(dist_Matrix[i][n])
                check = False
                break
        i += 1
        
    if check == False:
        raise TypeError ('malformed input')
    
    
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
    n: integer
        row number indix of minimum which is not 0
    m: integer
        column number index of minimum which is not 0

    """
    
    minInLine = []
    n = 0
    m = 0
    
    #remove zeros for acual minmum location
    for line in matrix:
        i = 0
        for element in line:
            if element == float(0):
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
                line[i] = float(0)
            i += 1
        
    return(n,m)
