def rem_duplicates_list(n,data):
    for i in data:
        if i not in orig:
            orig.append(i)
    return orig
n=int(input())
orig=[]
data=list(map(int,input().split()))
print(rem_duplicates_list(n,data))
