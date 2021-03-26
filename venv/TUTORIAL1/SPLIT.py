# Split a string into a list where each word is a list item:
txt = "welcome to the jungle"
x = txt.split()
print(x)
#SYNTAX
# string.split(separator, maxsplit)
# separator	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
# maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x)