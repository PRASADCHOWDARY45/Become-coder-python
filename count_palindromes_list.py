def count_palindrome(n,data):
    c=0
    for i in range(n):
        k=0
        temp=data[i]
        while data[i]:
            r=data[i]%10
            data[i]//=10
            k=k*10+r
        if k==temp:
            c+=1
    return c
n=int(input())
data=list(map(int,input().split()))
print(count_palindrome(n,data))

