def FORLoop():
    # Write your code here
    n = int(input())
    l1 = []
    for i in range(n):
        l1.append(int(input()))
    print(l1)
    iter1 = iter(l1)
    for i in range(n):
        print(next(iter1))
    return iter1


if __name__ == '__main__':
    try:
        d = FORLoop()
        print(type(d))
        print(next(d))

    except StopIteration:
        print('Stop Iteration : No Next Element to fetch')