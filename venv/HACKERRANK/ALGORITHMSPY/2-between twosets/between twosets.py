from math import gcd
if __name__ == '__main__':
    def get_hcf(arr):
        hcf=arr[0]
        for i in arr:
            hcf=gcd(hcf,i)
        return hcf
    def lcm(a,b):
        return a*b//gcd(a,b)
    def get_lcm(arr):
        l=arr[0]
        for i in arr:
            l=lcm(l,i)
        return l
    input()
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    lcm_a=get_lcm(a)
    hcf_b=get_hcf(b)
    f=[i for i in range(lcm_a,hcf_b+1) if hcf_b%i == 0 and i%lcm_a==0]
    print(len(f))


