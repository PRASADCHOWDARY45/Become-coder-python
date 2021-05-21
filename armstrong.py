num=int(input())
nnum=num
k=num
c=0
while num:
    c+=1
    num=num//10
tem=0
while k:
    tem+=pow(k%10,c)
    k=k//10
if nnum==tem:
    print(" True ")
else:
    print("false")
