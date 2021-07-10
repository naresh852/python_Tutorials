# from math import floor
#
# n = int(input())
# for _ in range(n):
#     N, K = map(int, input().split())
#     A = list(map(int, input().split()))
#
#     # check if avg<=K
#     ele = 1
#     s = sum(A)
#     avg = s / N
#     # if floor(avg)<=K:
#     #     print(0)
#     # else:
#     #     eq=s-(N*K)
#     #     print(eq-1)
#     num = 0
#     while floor(avg) > K:
#         num += 1
#         s = s + ele
#         N = N + 1
#         avg = s / N
#         ele += 1
#     if len(A) == N:
#         print(0)
#     else:
#         print(num)
from math import floor

T = int(input())

while (T):

  N,K = input().split()

  N = int(N)

  s = sum(list(map(int,input().split())))

  K = int(K)

  x = floor( s/(K+1) - N+1)

  print(max(x, 0))

  T-=1


