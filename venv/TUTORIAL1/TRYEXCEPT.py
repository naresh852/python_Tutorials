try:
     answer = 25 / 0
     number = int(input("enter number : "))
     print(number)

except ValueError as err:
     print(err)
except ZeroDivisionError as brr:
     print(brr)