
# wronginput=input()
# rightinput=input()

from itertools import combinations
str1 = input()
str2 = list(input())
count = 0
for i in combinations(str1 , len (str2) ):
     # print(i)
	if list(i) == str2 :
	    count += 1
print(count)
for i in combinations(str1 , len (str2) ):
    print(i,list(i))
    print(str2)
