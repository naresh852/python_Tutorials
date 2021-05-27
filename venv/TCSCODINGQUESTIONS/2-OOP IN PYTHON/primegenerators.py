def primegenerator(num, val):
    # Write your code here
    l=[]
    for num in range(2,num+1):
        for i in range(2,num):
           if num%i == 0:
              break
        else:
            l.append(num)
    lt=len(l)
    if val:
        # yield l
        for i in range(lt):
            if i%2==0:
                yield l[i]
    else:
        for i in range(lt):
            if i%2!=0:
                yield l[i]
if __name__ == '__main__':

    num = int(input().strip())

    val = int(input().strip())

    for i in primegenerator(num, val):
        print(i,end=" ")