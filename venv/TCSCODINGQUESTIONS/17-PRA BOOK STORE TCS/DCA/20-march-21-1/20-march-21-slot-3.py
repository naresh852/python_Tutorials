from itertools import combinations
# n=input()
# l=len(n)
# if l<5:

s = input()
ans = 0
for i in range(0, len(s)):
        ans += int(s[i])
        t = s[i]
        for j in range(i + 1, len(s)):
            t += s[j]
            ans += int(t)
print(ans)