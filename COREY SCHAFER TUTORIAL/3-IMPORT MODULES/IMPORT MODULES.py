'''to change add module to sys path
1.control panel>systemsecurity>system
2.advanced sytem security>environment variables
3.new variables > new >variablename=PYHTONPATH
4.PATH 51-ADD REMOVE ROWS COLS IN DF'''
courses = ['History', 'Math', 'Physics', 'CompSci']
import my_module
from my_module import find_index
from my_module import *
import sys
import os
import calendar
import datetime
x=find_index(courses,"Math")
print(x)
print(sys.path)
print(os.path)
print(sys.platform)