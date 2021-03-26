x=lambda a:a*a
print(x(2))
def fun(n):
    return lambda a:a*n
doubler = fun(2)
print(doubler(5))
def funv(n):
    return lambda a:a*n
tripler = funv(3)
print(tripler(4))
print(fun(3)(5))