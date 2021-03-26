# Enter your code here. Read input from STDIN. Print output to STDOUT
# from collections import deque
# d=deque()
# for _ in range(int(input())):
#     l=list(map(str,input().split()))
#     if l[0]=='append':
#         d.append(l[-1])
#     elif l[0]=='appendleft':
#         d.appendleft(l[-1])
#     elif l[0]=='pop':
#         d.pop()
#     else:
#         d.popleft()
# print(*d)

# from collections import deque
# d = deque()
# for _ in range(int(input())):
#     inp = input().split()
#     getattr(d, inp[0])(*[inp[1]] if len(inp) > 1 else [])
# print(*[item for item in d])

from collections import deque


# queue = deque()
# for _ in range(int(input())):
#     exec('queue.{0}({1})'.format(*input().split()+['']))
# print(*queue)

from collections import deque

n = int(input())
d = deque()
for _ in range(n):
        func, *num = input().split()
        getattr(d, func)(*num)
print(' '.join(d))