#1트
#현재시간
a,b=map(int,input().split())
#요리하는데 필요한 시간
c=int(input())
h=b+c//60
m=b+c%60

if b+c<60:
    print(a,b+c)
elif b+c>=60:
    if a+h>24:
        print((a+h)%24,m)
    elif a+h==24:
        print(24,m)
    else:
        print(a+h,m)
        
#2트
#현재시간
a,b=map(int,input().split())
#요리하는데 필요한 시간
c=int(input())
h=(b+c)//60
m=(b+c)%60

if b+c<60:
    print(a,m)
elif b+c>=60:
    if a+h>24:
        print((a+h)%24,m)
    elif a+h<24:
        print(a+h,m)
    elif a+h==24:
        print(0,m)