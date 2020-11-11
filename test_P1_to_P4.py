import os
#set current working directory to file location
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
import time
import P1
import P2
import P3
import P4

#RunCode
start1 = time.time()
a = P1.ParseSeqFile('newsequencefile.txt')
end1 =time.time()
print('*******************\nParseSeqFile: \n*******************\n\n',a, '\n\n')
labels = []
for tuples in a:
    labels.append(tuples[0])
start2 =time.time()
b = P2.AlignByDP(a)
end2 = time.time()
print('*******************\nAlignByDP: \n*******************\n\n',b, '\n\n')
start3 =time.time()
c = P3.ComputeDistMatrix(b)
end3 = time.time()
print('*******************\nComputeDistMatrix: \n*******************\n\n',c, '\n\n')
start4 =time.time()
d = P4.Cluster(c, labels)
end4 = time.time()
print('*******************\nCluster: \n*******************\n\n',d)
print('\n')
print('|+++++++++++++++|\n| Test Analysis |\n|+++++++++++++++|\n')
print('|#', '-'*21, '#|')
print('|#','*'*21,'#|')
print('|Overall time: %9.3f s|\n|P1 %20.3f s|\n|P2 %20.3f s|\n|P3 %20.3f s|\n|P4 %20.3f s|\n|# DNA Sequences %7i  |\n|# of paars %12i  |' %((end4-start1),(end1-start1),(end2-start2),(end3-start3),(end4-start4), len(a), ((len(a)*(len(a)-1))/2)))
print('|#','*'*21,'#|')
print('|#', '-'*21, '#|')