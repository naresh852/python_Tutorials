''''all test cases passed hurray'''
def stringmethod(para, special1, special2, list1, strfind):
    # opara = para
    for i in special1:
        temp = para.replace(i, "")
        para = temp
    word1 = temp
    rword2 = word1[69::-1]
    print(rword2)
    rword2 = rword2.replace(" ", "")
    joint_string = rword2.replace("", special2)
    le = len(joint_string)
    print(joint_string[1:le - 1])
    for i in list1:
        if i not in para.split():
            result = False
            break
        else:
            result = True
    if result:
        print(f"Every string in  {list1} were present")
    else:
        print(f"Every string in  {list1} were not present")
    print(word1.split()[:20])
    word2 = para.split()
    newlist = []
    for i in word2:
        if word2.count(i) < 3:
            newlist.append(i)
            if newlist.count(i) != 1:
                newlist.pop()
    nl = len(newlist)
    print(newlist[nl - 20:nl:1])
    print(word1.rfind(strfind))


if __name__ == '__main__':
    para = input()

    spch1 = input()

    spch2 = input()

    qw1_count = int(input().strip())

    qw1 = []

    for _ in range(qw1_count):
        qw1_item = input()
        qw1.append(qw1_item)

    strf = input()

    stringmethod(para, spch1, spch2, qw1, strf)
def stringmethod(para, special1, special2, lis, strfind):
    paralis = para.split()
    splen = len(special1)
    for i in range(splen):
        w = para.split(special1[i])
        j = "".join(w)
        para = j
    wordd = para

    word2 = para[69::-1]
    print(word2)
    word3 = word2.replace(" ", "")
    li = []
    for i in word3:
        li.append(i)
    word4 = special2.join(li)
    print(word4)

    for i in lis:
        if i in paralis:
            result = True
        else:
            result = False
            break

    if result:
        print(f"Every string in  {lis} were present")
    else:
        print(f"Every string in  {lis} were not present")
    word1 = wordd.split()
    print(word1[:20])
    list2 = []
    l = len(word1)
    for i in range(l):
        if word1.count(word1[i]) < 3:
            list2.append(word1[i])
            if list2.count(word1[i]) != 1:
                list2.pop()
    le = len(list2)
    print(list2[le - 20:le:1])
    sf=para.rfind(strfind)
    print(sf)






# more short version
# def stringmethod(para, special1, special2, lis, strfind):
#     paralis = para.split()
#     for i in special1:
#         w = para.replace(i,"")
#         para = w
#     wordd = para
#
#     word2 = para[69::-1]
#     print(word2)
#     word3 = word2.replace(" ","")
#     word4=word3.replace("",special2)
#     print(word4[1:len(word4)-1])
#
#     for i in lis:
#         if i in paralis:
#             result = True
#         else:
#             result = False
#             break
#
#     if result:
#         print(f"Every string in  {lis} were present")
#     else:
#         print(f"Every string in  {lis} were not present")
#     word1 = wordd.split()
#     print(word1[:20])
#     list2 = []
#     l = len(word1)
#     for i in range(l):
#         if word1.count(word1[i]) < 3:
#             list2.append(word1[i])
#             if list2.count(word1[i]) != 1:
#                 list2.pop()
#     le = len(list2)
#     print(list2[le - 20:le:1])
#     sf=para.rfind(strfind)
#     print(sf)
#
#
# if __name__ == '__main__':
"best till now"
"passed four testcases"
#
# def stringmethod(para, special1, special2, lis, strfind):
#     paralis = para.split()
#     # paralis=[]
#     # for i in parali:
#     #     paralis.append(i.lower())
#     splen = len(special1)
#     for i in range(splen):
#         w = para.split(special1[i])
#         j = "".join(w)
#         para = j
#     # print(para)
#     wordd = para
#
#     word2 = para[69::-1]
#     print(word2)
#     word3 = word2.replace(" ", "")
#     li = []
#     for i in word3:
#         li.append(i)
#     word4 = special2.join(li)
#     print(word4)
#
#     for i in lis:
#         if i in paralis:
#             result = True
#         else:
#             result = False
#             break
#
#     if result:
#         print(f"Every string in  {lis} were present")
#     else:
#         print(f"Every string in  {lis} were not present")
#     word1 = wordd.split()
#     print(word1[:20])
#     list2 = []
#     l = len(word1)
#     for i in range(l):
#         if word1.count(word1[i]) < 3:
#             list2.append(word1[i])
#             if list2.count(word1[i]) != 1:
#                 list2.pop()
#     le = len(list2)
#     print(list2[le - 20:le:1])
#     indexlist = []
#     nll = len(para)
#     i = 0
#     while i < nll + 1:
#         newstr = para[i:]
#         if newstr.startswith(strfind):
#             indexlist.append(i)
#         i += 1
#     print(max(indexlist))

para=input()
special1=input()
special2=input()
n=int(input())
lis=[]
for _ in range(n):
    lis.append(input())
strfind=input()
stringmethod(para,special1,special2,lis,strfind)