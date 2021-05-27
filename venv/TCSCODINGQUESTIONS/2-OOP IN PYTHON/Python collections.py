import collections
from collections import OrderedDict
from collections import defaultdict

def collectionfunc(text1, dictionary1, key1, val1, deduct, list1):
    dic = text1.split(" ")
    x=collections.Counter(dic)
    items=dict(x).items()
    dic1={key:val for key,val in sorted(items)}
    print(dic1)
    # temp1=collections.Counter(dictionary1)
    # temp2=collections.Counter(deduct)
    # res=temp1-temp2
    # print(res)
    # print(deduct)
    # print(dictionary1)
    keys=[]
    for k in dictionary1.keys():
        keys.append(k)
    for i in deduct.keys():
        keys.append(i)
    nkeys=keys
    res={key:dictionary1.get(key,0)-deduct.get(key,0) for key in nkeys}
    print(res)
    od=OrderedDict()
    for k,v in zip(key1,val1):
        od[k]=v
    od.pop(key1[1])
    od[key1[1]]=val1[1]
    print(dict(od))
    dd=defaultdict(lambda :0)
    ev=[]
    odd=[]
    for i in list1:
        if i%2==0:
            ev.append(i)

        else:
            odd.append(i)
    if len(odd)>0:
        dd["odd"] = odd
    if len(ev)>0:
        dd["even"]=ev
    print(dict(dd))

if __name__ == '__main__':
    from collections import Counter

    text1 = input()

    n1 = int(input().strip())
    qw1 = []
    qw2 = []
    for _ in range(n1):
        qw1_item = (input().strip())
        qw1.append(qw1_item)
        qw2_item = int(input().strip())
        qw2.append(qw2_item)
    testdict = {}
    for i in range(n1):
        testdict[qw1[i]] = qw2[i]
    collection1 = (testdict)

    qw1 = []
    n2 = int(input().strip())
    for _ in range(n2):
        qw1_item = (input().strip())
        qw1.append(qw1_item)
    key1 = qw1

    qw1 = []
    n3 = int(input().strip())
    for _ in range(n3):
        qw1_item = int(input().strip())
        qw1.append(qw1_item)
    val1 = qw1

    n4 = int(input().strip())
    qw1 = []
    qw2 = []
    for _ in range(n4):
        qw1_item = (input().strip())
        qw1.append(qw1_item)
        qw2_item = int(input().strip())
        qw2.append(qw2_item)
    testdict = {}
    for i in range(n4):
        testdict[qw1[i]] = qw2[i]
    deduct = testdict

    qw1 = []
    n5 = int(input().strip())
    for _ in range(n5):
        qw1_item = int(input().strip())
        qw1.append(qw1_item)
    list1 = qw1

    collectionfunc(text1, collection1, key1, val1, deduct, list1)
