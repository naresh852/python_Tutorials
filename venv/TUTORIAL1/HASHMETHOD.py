# Syntax : hash(obj)
#
# Parameters :
# obj : The object which we need to convert into hash.
#Python offers hash() method to encode the data into unrecognisable value.
# Returns : Returns the hashed value if possible.

# Python 3 code to demonstrate
# property of hash()

# initializing objects
# tuple are immutable
tuple_val = (1, 2, 3, 4, 5)

# list are mutable
list_val = [1, 2, 3, 4, 5]

# Printing the hash values.
# Notice exception when trying
# to convert mutable object
print("The tuple hash value is : " + str(hash(tuple_val)))
# hash() returns hashed value only for immutable objects,
    # hence can be used as an indicator to check for mutable/immutable objects
print("The list hash value is : " + str(hash(list_val)))