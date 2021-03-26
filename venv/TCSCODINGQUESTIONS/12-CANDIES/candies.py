if __name__ == "__main__":

  custOrder = int(input())


  if custOrder < 0 or custOrder > 10:
    print("Invalid Input")
    print("Number of Candies in Jar : 10")
  else:
    print("Number of candies sold : ",custOrder)
    leftCandies = 10 - custOrder

    if leftCandies <= 5:
      print("Number of Candies in Jar : 10")
    else:
      print("Number of Candies in Jar : ", leftCandies)

# Online Python - IDE, Editor, Compiler, Interpreter
'''
i = int(input())
try:
    N = 10
    candies = 0
    assert 0 < i <= 10
    # temp=i
    # while temp<=5:
    #     temp=temp+i
    # temp=temp-i
    if i <= 5:
        # print('no of candies sold',temp)
        print('no of candies sold', i)
        print('no of candies available', N - i)
except:
    print('INVALID INPUT')
    print('No of candies available', 10)'''

