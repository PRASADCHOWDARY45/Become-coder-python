def harshad(num):
    res=0
    temp=num
    while num:
        r=num%10
        num=num//10
        res+=r
    if temp%res==0:
        return True
    return False
num=int(input())
print(harshad(num))
