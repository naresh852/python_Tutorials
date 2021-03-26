# print(2**4)
def raisepow(basenum,pownum):
    result = 1
    for index in range(pownum):
        result = result * basenum
    return result

print(raisepow(16,2))