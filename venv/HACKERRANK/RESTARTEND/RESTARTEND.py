import re
string = input()
k = input()
m=re.search(k,string)
pattern=re.compile(k)
if not m:
    print("(-1,-1)")
while m:
    print("({0},{1})".format(m.start(),m.end()-1))
    m=pattern.search(string,m.start()+1)


s = input()
k = input()
if k in s:
    print(*[(i.start(), (i.start()+len(k)-1)) for i in re.finditer(r'(?={})'.format(k), s)], sep='\n')
else:
    print('(-1, -1)')