def Cluster(dist_Matrix):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    sequences = []
    
    for i in range(len(dist_Matrix[0])-1):
        sequences.append(abc[i])
    print(sequences)
    cluster = []
    print(cluster)
    i = 1
    
    for line in dist_Matrix:
        if i == 1:
            i += 1
            line = line[i:]
            indice = line.index(min(line))
            cluster.append('(a, %s' % sequences[indice])
            sequences.pop()
            sequences.pop(indice)
        else:
            try:
                i += 1
                line = line[i:]
                indice = line.index(min(line))
                print(indice)
                cluster.append('%s)' % sequences[indice])
                sequences.pop(indice)
            except:
                continue
        #print(cluster)
    return(cluster)


#########################
##Function not done jet##
#########################


