txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)
#The startswith() method returns True if the string starts with the specified value, otherwise False.
# string.startswith(value, start, end)
# Check if position 7 to 20 starts with the characters "wel":
txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)
print(x)