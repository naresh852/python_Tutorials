from scipy import stats


def poisson():
    '''
    output: ans : Float
    '''
    # Write your code here
    # Assign the probability value to the variable ans
    # Round off to 2 decimal places
    k = 15
    mu = 10
    x = stats.poisson.pmf(k, mu)
    ans = round(x, 2)

    return ans


if __name__ == '__main__':
    print(poisson())