a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(x)
# The sorted() function returns a sorted list of the specified iterable object.
#
# You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically
a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a, reverse=True)
print(x)
# SYNTAX
# sorted(iterable, key=key, reverse=reverse)

# L = ["cccc", "b", "dd", "aaa"]
# 
# print("Normal sort :", sorted(L))
#
# print("Sort with len :", sorted(L, key=len))