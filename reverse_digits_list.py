def reverse(n,data):
    for i in range(n):
        k=0
        while data[i]:
            r=data[i]%10
            data[i]//=10
            k=k*10+r
        data[i]=k
n=int(input())
data=list(map(int,input().split()))
reverse(n,data)
print(*data)
            
