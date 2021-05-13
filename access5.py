num=int(input())
temp=num
c=0
d=0
n=k=0
nnum=0
p=1
while num:
    r=num%10
    num=num//10
    c+=1
d=c=c-1
num=temp
if num>0:
    n=num//10**c
    k=num%10
while num:
    r=num%10
    num=num//10
    if c==d:
        r=n
    elif c==0:
        r=k
    nnum=nnum+r*p
    p=p*10
    c-=1
print(nnum)
        
