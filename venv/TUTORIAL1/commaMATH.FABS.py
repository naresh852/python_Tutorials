import math


def Main():
    num = -85

    # fabs is used to get the absolute
    # value of a decimal
    # FABS RETURNS FLOAT VALUE WHERE AS ABS RETURNS INTEGER
    num1 = abs(num)
    print(num1)
    num = math.fabs(num)

    print(num)
    # Python program to illustrate
    # getting input from user
    name = input("Enter your name: ")

    # user entered the name 'harssh'
    #comma is used for auto spacing and instead +
    print("hello", name)


if __name__ == "__main__":
    Main()