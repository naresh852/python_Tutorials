# Online Python - IDE, Editor, Compiler, Interpreter
def solve(n):
    if n > 2:
        return solve(n - 1) + solve(n - 2)
    if n == 1 or n == 2:
        return 1


try:
    n = int(input())

    if 5 < n <= 20:
        mylis = []
        oddc = 0
        ec = 0
        for i in range(1, n + 1):
            x = solve(i)
            mylis.append(x)
            if x % 2 == 0:
                ec += 1
            else:
                oddc += 1
        print(*mylis)
        print(ec)
        print(oddc)

    else:
        print('INVALID INPUT')
except:
    print("INVALID OUTPUT")



