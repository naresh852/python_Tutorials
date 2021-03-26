# def maxipilla(num1,num2,num3):
#     return max(num1,num2,num3)
# result = maxipilla(100,54,23)
# print(result)
def maxpilla(num1,num2,num3):
    if num1>=num2 and num1>= num3:
        print(num1)
    elif num2>=num1 and num2>=num3:
        print(num2)
    else:
        print(num3)

maxpilla(41,56,230)