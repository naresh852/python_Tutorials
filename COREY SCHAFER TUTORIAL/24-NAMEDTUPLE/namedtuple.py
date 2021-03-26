from collections import namedtuple
#named tuple is more readable
Color = namedtuple('Color', ['red', 'green', 'blue'])

color = Color(55,155,255)
white = Color(255,255,255)

print(color.blue)