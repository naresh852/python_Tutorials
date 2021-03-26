
# s=str(input())
# let=len(s)
# if s[0].isalpha():
#     l = s[0].upper()
#     # print(l+s[1:])
# else:
#     l = s[0]
#     print(l + s[1:])
# for i in range(len(s)):
#     if s[i]==" " and s[i+1].isalpha():
#         k=i+1
#         j=s[k].upper()
#         limit=i
#         print(l + s[1:k] + j + s[k + 1:])
#
def solve(s):
    s = list(s.split(' '))
    p=[]
    for i in s:
        if i.isalpha():
            p.append(i[0].upper()+i[1:]+" ")
        else:
           p.append(i)
           p.append(" ")
    p="".join(p)
    return p
s=input()
print(solve(s))
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     s = input()
#
#     result = solve(s)
#
#     fptr.write(result + '\n')
#
#     fptr.close()





