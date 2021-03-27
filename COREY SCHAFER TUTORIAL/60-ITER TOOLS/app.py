import itertools
'''itertools.count can also count backward by deco=imal nums also
counter=itertools.count(start=1,step=5) ##there is no stop
'''
counter=itertools.count(5,6)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# for num in counter:
#     print(num)
daily_data=[100,200,300,500]
dates=zip(itertools.count(),daily_data)
dates=list(zip(counter,daily_data))
# # print([n for n in dates])
# print(dates)

