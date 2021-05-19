import numpy as np
# from scipy import stats
import statistics


def measures(arr):
    # Write your code here
    '''
    Input: arr : numpy array
    Return : mean,median,std_deviation,variance,mode,iqr  : float

    Note:
    1. Assign the values to designated variables
    2. Round off to 2 decimal places
    '''
    mean = round(statistics.mean(arr), 2)
    median = round(statistics.median(arr), 2)
    std_deviation = round(statistics.pstdev(arr), 2)
    variance = round(statistics.pvariance(arr), 2)
    mode = round(statistics.mode(arr), 2)
    q1, q3 = np.percentile(arr, [25, 75])
    iqr = round(q3 - q1, 2)

    return mean, median, std_deviation, variance, mode, iqr


if __name__ == '__main__':
    array1 = []
    n = int(input())
    for i in range(n):
        array1.append(float(input()))
    narray1 = np.array(array1)
    print(measures(narray1))
