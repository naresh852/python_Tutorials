from math import pow
n=input()
if int(n)<0:
    print("Wrong Input")
else:
    ans=pow(int(n),4)
    res=str(int(ans))
    if int(res[-1])==int(n):
        print("True")
    else:
        print("False")

# N = int(input())
# pow = N ** 4
#
# pow = str(pow)
# N = str(N)
#
# if int(N) < 0:
#     print('Wrong input')
#
# elif pow[len(pow) - len(N)::] == N:
#     print('True')

# else:
#     print('False')