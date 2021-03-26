import string
alpha = string.ascii_lowercase

n = int(input())
L = []
width=n+n-1+(n-1)*2
for i in range(n):
    s = "-".join(alpha[i:n])
    L.append((s[::-1]+s[1:]).center(width, "-"))
print("\n".join(L[:0:-1]+L))
print(L)
# print("-".join(alpha[0:5]))
# k=[]
# ss="-".join(alpha[0:5])
# k.append((ss[::-1]+ss[1:]).center(width,"-"))
# print(ss[::-1])
# print(ss[1:])
# print(k)
# print(ss[:0:-1]+ss)
