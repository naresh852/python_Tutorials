def Handle_Exc1():
    a = int(input())
    b = int(input())
    s = a + b

    if a > 150 or b < 100:
        raise ValueError("Input integers value out of range.")
    elif s > 400:
        raise ValueError("Their sum is out of range")
    else:
        print("All in range")


if __name__ == '__main__':
    try:
        Handle_Exc1()
    except ValueError as exp:
        print(exp)
