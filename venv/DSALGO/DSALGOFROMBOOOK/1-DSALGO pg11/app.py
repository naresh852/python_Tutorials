
# Online Python - IDE, Editor, Compiler, Interpreter
# x=int(3.14)
# y=int(4.2)
# print(x,y)
# s=input()
# print(int(s))
########## string convert to integer ##########
# print(int('7f',16))
# print(float('12.5'))
######## list hello prints individual elemenst as hello is iterable itself ########
# print(list('hello'))
################## comma is necessary for single tuple or else it cnsiders the element as str or numeric class #######
# x=(17,)
# print(x,type(x))
##########\ for escaping special character #######
# print("don't worry")
# print("don\'t worry")
# Python also supports using the delimiter or """ t to begin and end ,to avoid using \n for new line
# print("""Welcome to the GPA calculator.
# Please enter all your letter grades, one per line.
# Enter a blank line to designate the end.""")
########## sets are mutable ,unordered, ###########
##########frozen sets are immutable  #################
# x=set()  but we cant write empty set as x={} as it is a dictionary from historical reasons
# x={'k','l'}
# print(x,type(x))
# x=set('hello')  #hello is a iterable so ouput will be {'l', 'o', 'e', 'h'}
# print(x)
# print(0b0101) ##binary conversion
# print(0x4F)   ###hexadecimal conversion
# print(0o14)   ###octal conversion

###########dict in python ################
# pairs=(('name','naresh'),('age',24))
# print(dict(pairs))
# pairs={('name','naresh'),('age',24)}
# print(dict(pairs))
# pairs=[('name','naresh'),('age',24)]
# print(dict(pairs))
# print(dict(pairs)['name'])

# Python guarantees that q * m+r will equal n. n/m n=dividend,m=divisor
# l1=[5,6,7]
# l2=[5,7]
# if l1<l2:
#     print('l1 is less than l2')
# else:
#     print('l2 is greater than l1')
# we can perform comparison operations on these lists.thats cool i didnt know that
# extende assignment operator +=
# alpha=[1,2,3]
# beta=alpha
# beta+=[4,5]
# beta=beta+[6,7]
# print(alpha)
# j=0
# # data=['A','B','C','G','H']
# data=[]
# while j < len(data) and data[j] != 'X' :
#     print(j)
#     j += 1


# Online Python - IDE, Editor, Compiler, Interpreter
# grades=['A','A+','B']
# points={'A+' :4.0, 'A' :4.0, 'A-' :3.67, 'B+' :3.33, 'B' :3.0, 'B-' :2.67, 'C+' :2.33, 'C' :2.0, 'C' :1.67, 'D':1.0, 'D+':1.33, 'F': 0.0}
# def compute_gpa(grades, points ):
#     num_courses = 0
#     total_points = 0
#     for g in grades:
#         if g in points: # a recognizable grade
#             num_courses += 1
#             total_points += points[g]
#     return total_points / num_courses
# print(compute_gpa(grades,points))
###################### ord and chr usess to find unicode of some value and reverse ################
# Character Encoding: ord and chr relate characters and their integer code points.
# For example, ord( A ) is 65 and chr(65)
############## divmod uses @####################
# x = divmod(5, 2)
# The divmod() function returns a tuple containing the quotient  and the remainder when argument1 (dividend) is divided by argument2 (divisor).
################ pow(x,y,z) uses  ##################
# x = pow(4, 3, 5)  # (same as (4 * 4 * 4) % 5):
# print(x)
# print('helllo '*5)
# print('marron',5)
# print(input().split())


# ########## EXCEPTION HANDLING ############
# an initially invalid choice
# age = -1
# while age <= 0:
#     try:
#         age = int(input( "Enter your age in years: "))
#         if age <= 0:
#             print( "Your age must be positive" )
#     # except (ValueError, EOFError):
#     #     # print( "Invalid response" )
#     #     pass
#     except ValueError:
#         print(" That is an invalid age specification ")
#     except EOFError:
#         print( "There was an unexpected error reading input." )
#         raise

#  For example, the call range(1000000) does not return a list of numbers; it
# returns a range object that is iterable. This object generates the million values one
# at a time, and only as needed. Such a lazy evaluation technique has great advantage.
#############ITERATORS AND ITERABLES #################
# def fibonacci():
#     a = 0
#     b = 1
#     while True:  # keep going...
#         yield a  # report value, a, during this pass
#         future = a + b
#         a = b  # this will be next value reported
#         b = future


# x = fibonacci()
# print(next(x))
# print(next(x))
# print(next(x))
# for i in x:
#
#     if next(x) > 200:
#         break
#     print(next(x))


# Online IDE - Code Editor, Compiler, Interpreter
# def fibonacci( ):
#     a,b= 0,1
#     while True:
#         yield a
#         a, b = b, a+b

# break

# print(next(fibonacci()))
# print(next(fibonacci()))
# print(next(fibonacci()))
# for i in fibonacci():
#     print(next(fibonacci()))
# 'print(fibonacci())'
###################### vars dirs ###########################
# print(dir(list))
# print(vars)  #vars require any module with dic attribute
# https://www.geeksforgeeks.org/vars-function-python/
################## first class objects #######################
# first-class objects are instances of
# a type that can be assigned to an identifier, passed as a parameter, or returned by
# a function. All of the data types we introduced in Section 1.2.3, such as int and
# list, are clearly first-class types in Python. I
# scream = print
# scream('hello')
###### ############## modules ########################
# PAGE49 NECESSARY EXISTING MODULES TO GO THROUGH
# https: // www.geeksforgeeks.org / python - arrays /