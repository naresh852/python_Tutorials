# from scipy import stats

def binomial():
    '''
    output: ans : Float
    '''
    #Write your code here
    #Assign the probability value to the variable ans
    #Round off to 2 decimal places

    # # failprob=stats.binom.pmf(0,4,0.6)
    # succprob=stats.binom.pmf(1,4,0.4)
    # ans =round(succprob,2)
    li=[1,2,3,4]
    lis=[stats.binom.pmf(k,4,0.6) for k in li]
    an=sum(lis)
    ans=round(an,2)
    return ans

if __name__=='__main__':
	print(binomial())