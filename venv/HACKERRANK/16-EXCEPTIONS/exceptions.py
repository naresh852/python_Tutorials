# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for i in range(n):
    a,b=map(str,input().split())
    try:
        print(int(int(a)/int(b)))
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code: "+str(e))
    except ValueError as e:
        print("Error Code: "+str(e))


# Enter your code here. Read input from STDIN. Print output to STDOUT
# n=int(input())
# for i in range(n):
#     a,b=map(str,input().split())
#     try:
#         print(int(a)/int(b))
#     except ZeroDivisionError as e:
#         print("Error Code: integer division or modulo by zero")
#     except ValueError as e:
#         print("Error Code: "+e)