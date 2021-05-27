import itertools
import operator


daily_data=[100,200,300,500]
# dates=zip(itertools.count(),daily_data)
# dates=list(zip(counter,daily_data))
##################################################
''' output is [(0, 100), (1, 200), (2, 300), (3, 500), (4, None), (5, None), (6, None), (7, None), (8, None), (9, None)]'''
# dates=list(itertools.zip_longest(range(10),daily_data))
# print(dates)
##########################################
''' prints [(0, 100), (1, 200), (2, 300), (3, 500)] '''
# dates=list(zip(range(10),daily_data))
# print(dates)
############################################
'''it keeps on cycling'''
# counter=itertools.cycle([1,2,3])
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
#################################
'''it just repeats same'''
# counter=itertools.repeat(2)
counter=itertools.repeat(2,times=3)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# squares=map(pow,range(10),itertools.repeat(2))
# squares=itertools.starmap(pow,[(0,2),(1,2),(2,2)])   ##similar to map but used tuple as input
# print(list(squares))
##########permutaions combinations############
letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
numbers1=[ 1, 2, 3,2,1,0]
names = ['Corey', 'Nicole']
'''both per and comb doesnt give us duplicates like (a,a) or(b,b)'''
# counter=itertools.combinations(letters,2)  ##with combi order does not matter (a,b) but not (b,a) as bith are same
# counter=itertools.permutations(letters,3)  ##if orer matters duplicates allowed (a,b) and (b,a)
#################duplicates are alloed in product ##########################
# counter=itertools.product(letters,repeat=3)
###############combinations repeat allowed ######################
# counter=itertools.combinations_with_replacement(letters,3)
#############chained######################
# counter=letters+numbers+names  #but if elements are in millions this is not efficient
# counter=itertools.chain(letters,numbers,names)  #it loops from letters to names one by one
# print(list(counter))
################## ISLICE (RANGE,STOP)###########
# counter=itertools.islice(numbers,2)  #start,step are optional
# counter=itertools.islice(range(10),1,6,2)  #iterable,start,stop,step
'''how is islice useful because if you want to slice a large file by converting to list is not memmory eff
can use for log files we have millions of data'''
''' files are itorators themselves we can use next to find next'''
# for item in counter:
#     print(item)
##### how to use islice for getting headers from a log file ####
# with open('test.log','r') as f:
#     header=itertools.islice(f,3)
#     for line in header:
#         print(line)
'''####compress function used in DS ######'''
'''this is similar to filter but filter uses function to do that but in compree those values are just passed as an iterable'''
selectors=[True,False,True,False]
# counter=itertools.compress(letters,selectors)
def lt_2(n):
    if n<2:
        return True
    return False
# counter=filter(lt_2,numbers)
'''#########to filter false values###########'''
# counter=itertools.filterfalse(lt_2,numbers)
'''###########drop value stop if value is False once in iterable and prints remaning as it is'''
# counter=itertools.dropwhile(lt_2,numbers1)
'''########take while will stop if Fals and wont print any after that###########'''
# counter=itertools.takewhile(lt_2,numbers1)
'''############ accumulate will add previous values into a new iterable ########'''
# counter=itertools.accumulate(numbers1)
# itertools.accumulate(iterble ,fun)
counter=itertools.accumulate(numbers1,operator.mul)
for item in counter:
    print(item)