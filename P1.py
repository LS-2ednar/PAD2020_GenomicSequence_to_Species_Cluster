def ParseSeqFile(File):
    """
    Parses a Sequence File by selecting only correct datainput and returns a 
    list of tuples containing the species and the dna sequence.

    Parameters
    ----------
    File : Paht to sequence file in string format
        For Parsing, the Data needs to start with > and there needs tobe 
        whitespace between the species and the following dna sequence.

    Returns
    -------
    returnlist : list of tuples with species and corrsiponing dna sequence
    """
    returnlist =list()
    try:
        file = open(File,'r')
    except:
        return 'malformed input'
    for line in file:
        if line[0] == ">":
            partslist = line.strip(">").strip("\n").split()
            label = partslist[0].upper()
            dnaparts = partslist[1:]
            dna = ''.join(dnaparts).upper()
            if is_dna(dna) == True:
                returnlist.append((label, dna))
            else:
                break
    return returnlist

def is_dna(sequence):
    """
    Checks if the length of a string is 0 when all DNA bases are removed.

    Parameters
    ----------
    sequence : string

    Returns
    -------
    bool
        True if len(seq) == 0
        otherwise Wrong 

    """
    if len(sequence.replace("A", "").replace("C", "").replace("G","").replace("T","")) == 0:
        return True
    else:
        return False

