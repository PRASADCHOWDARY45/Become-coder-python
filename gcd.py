def gcd(a,b):
    if a>b:
        k=a
        n=b
    else:
        k=b
        n=a
    while n:
        k,n=n,k%n
        return k
a,b=map(int,input().split())
print(gcd(a,b))
