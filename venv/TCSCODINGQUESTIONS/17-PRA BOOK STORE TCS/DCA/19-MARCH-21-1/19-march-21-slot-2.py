n=input()
l=len(n)
forward=n[1:l]+n[0]
print(forward)

bakward=n[l-1]+n[0:l-1]
print(bakward)
if forward==bakward:
    print(1)
else:
    print(0)

# num = input()
# length = len(num)
# if num[length - 1] + num[:length - 1] == num[1:] + num[0]:
#     print 1
# else:
#     print 0