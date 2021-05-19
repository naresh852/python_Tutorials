# in how many ways 3 boys chosen from 6 group
# and how many ways 2 girls chosen from 5 group
import math
from itertools import combinations


def dancers():
    '''
    output: ans : Integer
    '''
    # Write your code here
    # Assign your value to variable ans

    b = math.factorial(6) / (math.factorial(3) * math.factorial(3))
    g = math.factorial(5) / (math.factorial(3) * math.factorial(2))
    ans = b * g
    return int(ans)


if __name__ == '__main__':
    print(dancers())