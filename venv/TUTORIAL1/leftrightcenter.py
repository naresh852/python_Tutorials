# Return a 20 characters long, left justified version of the word "banana":
txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.")
# The ljust() method will left align the string, using a specified character (space is default) as the fill character.
# string.ljust(length, character)
# length	Required. The length of the returned string
# character	Optional. A character to fill the missing space (to the right of the string). Default is " " (space).
txt = "banana"

x = txt.ljust(20, "O")

print(x)