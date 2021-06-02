def sum_digits(n,data):
    for i in range(n):
        k=0
        while data[i]:
            r=data[i]%10
            data[i]//=10
            k=k+r
        data[i]=k
n=int(input())
data=list(map(int,input().split()))
sum_digits(n,data)
print(*data)
            
