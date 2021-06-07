def is_sorted(n,data):
    s=[]
    k=[]
    for i in data:
        s.append(i)
        k.append(i)
    s.sort()
    k.sort(reverse=True)
    if data==s or data==k:
        return True
    else:
        return False
n=int(input())
data=list(map(int,input().split()))
print(is_sorted(n,data))
