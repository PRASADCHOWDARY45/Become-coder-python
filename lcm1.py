def lcm(a,b):
    k=2
    res=1
    while True:
        if a%k==0 and b%k==0:
            a=a//k
            b=b//k
            res*=k
        if a%k!=0 or b%k!=0:
            k+=1
        if a<k:
            break
    print(res*a*b)
a,b=map(int,input().split())
lcm(a,b)

        
    
