# Get the value of the "age" property of the "Person" object:
class Person:
  name = "John"
  age = 36
  country = "Norway"

x = getattr(Person, 'age')
print(x)
# syntax
# getattr(object, attribute, default)
class Person:
  name = "John"
  age = 36
  country = "Norway"

x = getattr(Person, 'page', 'my message')
print(x)
# The delattr() function, to remove an attribute
#
# The hasattr() function, to check if an attribute exist
#
# The setattr() function, to set the value of an attribute
# getattr(object, attribute, value)