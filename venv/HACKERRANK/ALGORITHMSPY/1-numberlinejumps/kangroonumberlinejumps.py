# def kang(x1,v1,x2,v2):
#     return "YES" if v1>v2 and not (x2-x1)%(v2-v1) else "NO"
# if __name__ == '__main__':
#     x1,v1,x2,v2=map(int,input().split())
#     result=kang(x1,v1,x2,v2)
#     print(result)
# USING FILE OPEN WRITE CLOSE
import os


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    return "YES" if v1 > v2 and not (x2 - x1) % (v2 - v1) else "NO"


if __name__ == '__main__':
    fptr = open("kang.txt", 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()