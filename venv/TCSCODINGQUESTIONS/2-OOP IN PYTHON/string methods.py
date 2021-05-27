#
# def stringmethod(para, special1, special2, lis, strfind):
#     # Write your code here
#     paralis = []
#     for i in para:
#         paralis.append(i.lower())
#     splen = len(special1)
#     for i in range(splen):
#         w = para.split(special1[i])
#         j = "".join(w)
#         para = j
#     print(para)
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
#     word = "".join(lis).lower()
#     # print(word)
#     # print(paralis)
#     for i in word:
#         if i in paralis:
#             result = True
#         else:
#             result = False
#             break
#
#     if result:
#         print(f"Every string in {lis} were  present")
#     else:
#         print(f"Every string in {lis} were not present")
#     word1 = wordd.split()
#     print(word1[:20])
#     list2 = []
#     l = len(word1)
#     for i in range(l):
#         if word1.count(word1[i]) < 3:
#             list2.append(word1[i])
#             if list2.count(word1[i]) != 1:
#                 list2.pop()
#     # list2.sort(reverse=True)
#     # for j in list2:
#     #     if list2.count(j)>1:
#     #         list2.remove(j)
#     # list2.sort(reverse=True)
#     le = len(list2)
#     print(list2[le - 20:le:1])
#     indexlist = []
#     worde=" ".join(word1).strip()
#     nll=len(worde)
#     i=0
#     # print(nll)
#     while i<nll+1:
#         newstr=para[i:]
#         if newstr.startswith(strfind):
#             indexlist.append(i)
#             # result=i
#             # break
#         i+=1
#     indl=len(indexlist)
#     if indl>1:
#         last=indexlist[-1]
#         print(last)
#     else:
#         first=indexlist[0]
#         print(first)







# def stringmethod(para, special1, special2, lis, strfind):
#     # Write your code here
#     paralis = []
#     for i in para:
#         paralis.append(i.lower())
#     splen = len(special1)
#     for i in range(splen):
#         w = para.split(special1[i])
#         j = "".join(w)
#         para = j
#     # print(word1)
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
#     word = "".join(lis).lower()
#     # print(word)
#     # print(paralis)
#     for i in word:
#         if i in paralis:
#             result = True
#         else:
#             result = False
#             break
#
#     if result:
#         print(f"Every string in {lis} were  present")
#     else:
#         print(f"Every string in {lis} were not present")
#     word1 = wordd.split()
#     print(word1[:20])
#     list2 = []
#     l = len(word1)
#     for i in range(l):
#         if word1.count(word1[i]) < 3:
#             list2.append(word1[i])
#             if list2.count(word1[i]) != 1:
#                 list2.pop()
#     # list2.sort(reverse=True)
#     # for j in list2:
#     #     if list2.count(j)>1:
#     #         list2.remove(j)
#     # list2.sort(reverse=True)
#     le = len(list2)
#     print(list2[le - 20:le:1])
#     lt = 0
#     d = len(strfind)
#     while lt > 0:
#         x = wordd[lt:]
#         if x.startswith(strfind):
#             result = lt
#             break
#         lt += 1
#     print(lt)
#
#
# if __name__ == '__main__':
"best till now"
"passed four testcases"
#
def stringmethod(para, special1, special2, lis, strfind):
    paralis = para.split()
    # paralis=[]
    # for i in parali:
    #     paralis.append(i.lower())
    splen = len(special1)
    for i in range(splen):
        w = para.split(special1[i])
        j = "".join(w)
        para = j
    # print(para)
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
    indexlist = []
    nll = len(para)
    i = 0
    while i < nll + 1:
        newstr = para[i:]
        if newstr.startswith(strfind):
            indexlist.append(i)
        i += 1
    print(max(indexlist))

para=input()
special1=input()
special2=input()
n=int(input())
lis=[]
for _ in range(n):
    lis.append(input())
strfind=input()
stringmethod(para,special1,special2,lis,strfind)