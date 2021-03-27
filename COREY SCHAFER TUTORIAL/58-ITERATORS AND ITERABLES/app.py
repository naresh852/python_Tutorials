#iterable - a list is an iterbale because it can be looped over.
''' if something is an iterbale then it should have __iter__ dunder inter method
something which has iter method can be looped over and is called iterbale'''
#iterator -is an object withn a state so that it remembers where it is during an iteration s
# and iterators also know how to get their next value,they get their next value with a dunder next method.
#iterators are also iterables but diff is that iter method returns same objector so returns self
'''iteraors can only go forward,cant go back word,resetting or copying.'''
nums=[1,2,3]
# for i in nums:
#     print(i)
# print(dir(nums))
# i_nums=nums.__iter__()  #we can write withput dunders also
i_nums=iter(nums)
# print(i_nums)
# print(dir(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
while True:
    try:
        item=next(i_nums)
        print(item)
    except StopIteration:
        break
        