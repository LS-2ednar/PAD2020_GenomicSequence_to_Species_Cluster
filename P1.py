import os

def ParseSeqFile(File):
    """
    Parses a sequencefile and returns a list of tuples containing the species 
    and the dna sequence. For Parsing, the Data needs to start with ">" and there 
    needs to be whitespace between the species and the following dna sequence.

    Parameters
    ----------
    File : Paht to sequencefile in string format
        

    Returns
    -------
    returnlist : list of tuples with species and corresponding dna sequence
    """
    #input checks
    if os.path.isfile(File) != True:
        raise TypeError ('malformed input')
    
    returnlist = list()
    try:
        file = open(File,'r')
    except:
        return 'malformed input'
    
    #converting file to wished output
    for line in file:
        if line[0] != ">" and len(line)!=1:
            raise ValueError ('malformed input')
        #first check if the line follows the wished format
        if line[0] == ">":
            #creating a list and removeing unwanted > and \n
            partslist = line.strip(">").strip("\n").split()
            #check partslist size if 1 malformed input
            if partslist == []:
                raise ValueError ('malformed input')
            #catching label and format to capital letters
            label = partslist[0].upper()
            #generating dna and format to captial letters
            dnaparts = partslist[1:]
            dna = ''.join(dnaparts).upper()
            returnlist.append((label, dna))
        else:
            raise ValueError ('malformed input')
        #check if DNA is acual DNA
        if is_dna(dna) != True:
            raise TypeError ('malformed input')
            
            
    #checking output if it is a empty list raise ValueError
    if returnlist == []:
        raise ValueError ('malformed input')
    return (returnlist)

def is_dna(sequence):
    """
    Checks if the length of a string is 0 when all DNA bases are removed.

    Parameters
    ----------
    sequence : string of DNA

    Returns
    -------
    bool
        True if len(seq) == 0
        otherwise False 

    """
    #ensure that the given sequence is uppercase
    sequence = sequence.upper()
    
    #replace all A C G and T and compare length with 0
    if len(sequence.replace("A", "").replace("C", "").replace("G","").replace("T","")) == 0:
        return True
    else:
        return False
    
def get_labels(returnlist):
    """
    Function to get all labels in a order for later use in P4 (utility)

    Parameters
    ----------
    returnlist : list of tuples
        A list with labels and corisponding DNA sequences.

    Returns
    -------
    labellist : list of labels
        A list of labels.

    """
    labellist = []
    #gets labels of the tuples 
    for tuples in returnlist:
        labellist.append(tuples[0])
    return (labellist)
