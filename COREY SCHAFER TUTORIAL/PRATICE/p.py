# Online Python - IDE, Editor, Compiler, Interpreter
n = int(input())


def bigbinary(B):
    listofshifts = []
    temp = B[1:] + B[0]
    result = 0
    while (temp != B):
        listofshifts.append(temp)
        temp = temp[1:] + temp[0]
        result = max(listofshifts)
    return result


def solve(big, original, times):
    temp = original[1:] + original[0]
    limit = int(times)
    if big == 0:
        result = limit
    else:
        i = 0
        no_of_shifts = 0
        while (i != limit):
            while (temp != big):
                no_of_shifts += 1
                temp = temp[1:] + temp[0]
            temp = temp[1:] + temp[0]
            no_of_shifts += 1
            i = i + 1
        result = no_of_shifts
    return result


for i in range(n):
    length, times = input().split()
    A = input()
    bigb = bigbinary(A)
    x = solve(bigb, A, times)
    print(x)

# frds=['naresh','ajay','chenna']
# animals=['cat','dog']
# # to add list to list like items
# frds.extend(animals)
# print(frds)
# dic={1:"one",
#      "three":4,
#      5:6}
# dic.update({1:100,
#             "three":3,
#             5:"five"})
# # del dic["three"]
# # print(dic.items())
# for key in dic:
#     print(f"{key} {dic[key]}")
# a=[1,2,3]
# b=[1,2,3]
# print(a == b)
# print(a is b)
# b=a
# print(a==b)
# print(id(a))
# print(id(b))
# # check if they are equal in memory,same memory address
# print(a is b)
# print(id(a) == id(b))
# FALSE VALUES
# 1.false
# 2.none
# 3.0
# 4.empty list,tuple,set,''
# 5.empty dic
# these are all false

# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

# condition = False
#
# if condition:
#     print('Evaluated to True')
# else:
#     print('Evaluated to False')
# names=['naresh','ajay','kajal','sony']
# gender=['m','m','f','f']
# print(tuple(zip(names,gender)))