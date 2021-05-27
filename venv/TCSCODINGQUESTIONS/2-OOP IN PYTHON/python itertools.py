from itertools import *

import operator
def performIterator(tuplevalues):
    mainl = []
    x1 = cycle(tuplevalues[0])
    anl = []
    for i in range(4):
       anl.append(next(x1))
    mainl.append(tuple(anl))
    x2=tuplevalues[1]
    an=[]
    y1=repeat(x2[0],len(x2))
    an.append(y1)
    mainl.append(tuple(y1))
    ################
    x3=tuplevalues[2]
    y2=accumulate(x3,operator.add)
    mainl.append(tuple(y2))
    ###########
    a=[]
    y3=tuple(chain(tuplevalues))
    for i in y3:
        for j in i:
           a.append(j)
    mainl.append(tuple(a))
    #############
    aa=[]
    for i in tuplevalues:
        for j in i:
            aa.append(j)
    y4=filterfalse(lambda x:x%2==0,aa)
    mainl.append(tuple(y4))

    return tuple(mainl)



if __name__ == '__main__':

    length = int(input().strip())

    qw1 = []
    for i in range(4):
        qw2 = []
        for _ in range(length):
            qw2_item = int(input().strip())
            qw2.append(qw2_item)
        qw1.append(tuple(qw2))
    tupb = tuple(qw1)

    q = performIterator(tupb)
    print(q)