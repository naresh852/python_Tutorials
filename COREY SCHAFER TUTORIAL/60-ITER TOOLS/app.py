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


people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]
def get_state(people):
    return people['state']
'''######### returns a tuple of two things key,iterable ##########
groupby is not similar to in sql cause here iterable need to be sorted                                                                      '''
person_grp=itertools.groupby(people,get_state)
# for key,group in person_grp:
    # print(key,*group)
    #   print(key,len(list(group)))
    # print(key)
    # for person in group:
    #     print(person)
    # print()
'''### to make copy of person_grp both copy1 amd copy2 are same i checked
to get iterable from groupby using tee '''
copy1,copy2 = itertools.tee(person_grp)
for key,value in copy2:
    print(key,*value)
