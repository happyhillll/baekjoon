def summ(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

num = int(input())    
i=1
while num > summ(i):
    i+=1
a = num-summ(i-1)
b = i-a+1
if(i%2 ==0):
    print(str(a)+"/"+str(b))
else :
    print(str(b)+"/"+str(a))