'''
class sentence:
    def __init__(self,sentence):
        self.sentence=sentence
        self.index=0
        self.words=self.sentence.split()
    def __iter__(self):
        return self
    def __next__(self):
        if self.index>=len(self.words):
            raise StopIteration
        index=self.index
        self.index+=1
        return self.words[index]

'''
def sentence(line):
    for word in line.split():
        yield word
# my_sentence='This is a test'
my_sentence=sentence('This is a test')
# for l in my_sentence:
#     print(l)
##we can do same thing using generator


print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
# print(next(my_sentence))