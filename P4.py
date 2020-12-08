from collections import defaultdict

def Cluster(dist_Matrix, labels):
    """
    Cluster the different Labels are put in a binary tree in string format 
    based on distance Matrix
    Parameters
    ----------
    dist_Matrix : list of lists of floats
    
    labels : list of strings

    Returns
    -------
    returnstring: by parentesis clustered labels

    """
    # check if List of Tuples with strings and DNA
    check = True
    
    #check if it is a list of list
    if isinstance(dist_Matrix, list) == False:
        check = False
    
    #check of dist Matrix is equal to the length of labels
    if len(dist_Matrix) != len(labels):
        check = False
    #check every entry in the distmatrix
    i = 0 # initialize counter
    while len(dist_Matrix) > i:
        #check if the elements in the dist matrix are lists
        if isinstance(dist_Matrix[i], list) == False:
            check = False
            break
        #check if the elements in the lists are floats
        for n in range(len(dist_Matrix[i])):
            if isinstance(dist_Matrix[i][n], float) == False:
                check = False
                break
        i += 1
    
    #Check list dimensions
    for lis in dist_Matrix:
        if len(lis) != len(dist_Matrix):
            check = False
            break
    
    if check == False:
        raise TypeError ('malformed input')
    
    #initialize a 2d dict with keys as labels and  
    ClusterDict = defaultdict(dict)
    for n in range(len(labels)):
        for m in range(len(labels)):
            ClusterDict[labels[n]][labels[m]] = dist_Matrix[n][m]
            
    #Cluster the binary tree together
    while len(ClusterDict)>2:
        #find minimum
        n,m = dict_min(ClusterDict)
        #recalculate Vlaues
        recalc_dict(ClusterDict,n,m)
    
    retlist = []
    for key in ClusterDict.keys():
        retlist.append(key)
    
    #combin all parts in the returnlist to one final string
    returnstring = ''.join('(%s,%s)' % (retlist[0],retlist[1]))
    
    return returnstring   

def dict_min(ClusterDict):
    """
    Returns the two labels which need to be connected with each other
    Parameters
    ----------
    ClusterDict : 2D dict containing the values of the ComputedDistMatrix

    Returns
    -------
    n : String

    m : String

    """
    #initialize artificial minima
    minima = float('inf')
    
    if len(ClusterDict.keys()) != 2:
        #test first key
        for k1 in ClusterDict:
            
            #test second key
            for k2 in ClusterDict[k1]:
                
                #check if the value is smaller current minima
                if ClusterDict[k1][k2] < minima and k1 !=k2:
                    #define new minimum and keys n and m
                    minima = ClusterDict[k1][k2]
                    n = k1
                    m = k2
                    
    return n,m

def recalc_dict(ClusterDict,n,m):
    """
    Returns the recalucated clusterdict
    Parameters
    ----------
    ClusterDict     : 2D dict containing the values of a Matrix with Corrisponding Keys
        
    n & m           : keys to the ClusterDict where n is the primary and m the secondary key
    Returns
    ------- 
    newClusterDict  : recalculated ClusterDict

    """ 
    #generate new key
    newKey = '(%s,%s)' % (n,m)
    
    # Get values to recalc distance
    nV = ClusterDict[n] 
    mV = ClusterDict[m]
    rV = {}
    
    rV[newKey] = float(0)
    
    # calculate the new values
    if n in ClusterDict.keys() and m in ClusterDict.keys():
        for key in nV:
            if key != n and key != m:
                rV[key] = (nV[key] + mV[key])/2

    #add new calculated dict 
    ClusterDict[newKey] = rV
    
    #remove unwanted keys
    del ClusterDict[n]
    del ClusterDict[m]
    
    #removeing unwanted subkeys
    for key in ClusterDict:
        if n in ClusterDict[key].keys():
            del ClusterDict[key][n]
            
        if m in ClusterDict[key].keys():
            del ClusterDict[key][m]
    
    for key in ClusterDict:
        if key != newKey:
            ClusterDict[key][newKey] = ClusterDict[newKey][key]
            
    return ClusterDict 
