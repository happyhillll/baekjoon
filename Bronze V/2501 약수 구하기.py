a,b=map(int,input().split())

yak=[]

for i in range(1,a+1):
    if a%i==0:
        yak.append(i)
        
if len(yak)<b:
    print(0)
else:
    print(yak[b-1])

        
    