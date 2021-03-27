class Myrange:
    def __init__(self,start,end):
        self.value=start
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        if self.value>=self.end:
            raise StopIteration
        current=self.value
        self.value+=1
        return current
# num=Myrange(1,10)
# for n in num:
#     print(n)
#my range is an iterator cause it has next,as well as iterable cause it has iter #
#generators are iterators as well but the dunder iter or next method are created automatically so we dont have to create it as in class of my range
def my_range(start,end):
    current=start
    while current<end:
        yield current
        current+=1
nums=my_range(1,10)
print(*nums)
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print([num for num in nums])
#one good thing abut iterators is that they actually dont need to end as long as there is a next value it will keep iterating
#iterators can be used to for password craking ,yield is a iterator it saves memory by yeilding next value at a time

