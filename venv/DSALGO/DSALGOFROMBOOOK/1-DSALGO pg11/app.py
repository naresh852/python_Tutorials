
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