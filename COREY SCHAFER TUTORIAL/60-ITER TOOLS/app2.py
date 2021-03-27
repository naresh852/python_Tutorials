import itertools



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
counter=itertools.cycle([1,2,3])
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
