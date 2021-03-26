s=input()
r=""
for i in s:
    if i.isupper():
        x=i.lower()
        r=r+x
    elif i.islower():
        y=i.upper()
        r=r+y
    else:
        r=r+i
print(r)

def swap_case(s):
    # r=""
    # for i in s:
    #     if i.isupper():
    #        x=i.lower()
    #        r=r+x
    #     elif i.islower():
    #        y=i.upper()
    #        r=r+y
    #     else:
    #        r=r+i
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

print(*map(lambda x:x.lower() if x.isupper() else x.upper(),s),sep="")