import cmath
import math
from cmath import *
from math import *
# print(cmath.polar(complex(10,10))[0])
# AC=round(cmath.polar(complex(10,10))[0])
# op=round(AC/2)
# print(math.degrees(cmath.atan(op/10)))
# ab = float(input())
# bc = float(input())
# print(str(int(round(degrees(atan(ab/bc)))))+'°')

AB=float(input())
BC=float(input())
res=str(int(round(math.degrees(math.atan(AB/BC)))))
degree=chr(176)                                #for DEGREE symbol
print(res,degree, sep="")