import math
import os
import random
import re
import sys


num = int(input())
if num % 2 != 0:
    print("Weird")
elif num%2 == 0 and 6<num<=20 :
    print("Weird")
else:
    print("Not Weird")
