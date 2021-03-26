# Join all items in a tuple into a string, using a hash character as separator
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)

print(x)
# The join() method takes all items in an iterable and joins them into one string.
# A string must be specified as the separator.
# string.join(iterable)

# Join all items in a dictionary into a string, using a the word "TEST" as separator:
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)