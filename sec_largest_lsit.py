def sec_large(n,data):
    data.sort(reverse=True)
    return data[1]
n=int(input())
data=list(map(int,input().split()))
print(sec_large(n,data))
