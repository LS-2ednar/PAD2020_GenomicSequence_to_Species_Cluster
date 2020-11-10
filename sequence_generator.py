import random as r
import time

def generate_dna(length, number):
    start = time.time()
    Parser = ' >XY'
    #whitespace
    DNA = 'ATGC ATGC ATGC ATGC   ATGCATGCATGCATGCATGCATGCATGCATGC ATGC ATGC ATGC   ATGCATGCATGCATGCATGCATGCATGC ATGC ATGC ATGC ATGC   ATGCATGCATGCATGCATGCATGCATGCATGC ATGC ATGC ATGC   ATGCATGCATGCATGCATGCATGCATGC  >'
    newsequencefile = open('newsequencefile.txt', '+w')
    for i in range(number+1):
        sequence = ''
        for j in range(length):
            sequence = sequence + DNA[r.randint(0,200)]
        
        #Create Random Elements for the File
        Inital = Parser[r.randint(0, 3)]
        Label = 'Test%05i' % i
        wSpace = ' '*r.randint(1,10)
        print(Inital, Label, sequence)
        
        #write newsequencefile.txt
        newsequencefile.write(Inital+Label+wSpace+sequence+'\n')
    newsequencefile.close()
    end = time.time()
    print('Needed %f s' % (end-start))
    
generate_dna(50,125)