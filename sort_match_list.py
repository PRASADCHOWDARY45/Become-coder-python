def sort_match(n,data):
    for i in data:
        if i not in orig:
            orig.append(i)
    orig.sort()
    c=0
    for i in range(len(orig)):
        if orig[i]==data[i]:
            c+=1
    return orig,c
n=int(input())
orig=[]
data=list(map(int,input().split()))
print(sort_match(n,data))
