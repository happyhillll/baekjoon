a=int(input())
sum=0 #변수 sum을 입력받은 값까지 더할 수 있도록 0으로 초기화
for i in range(a+1):
    sum=sum+i
print(sum)

'''
i=1일 때, sum=0+1
i=2일 때, sum=1+2
i=3일 때, sum=3+3

마지막으로 print(sum)을 해주면 6이 출력.
* range(a+1)을 하는 이유는 range(a)의 경우네는 3을 입력했을때
i에 0,1,2만 들어가서 결과값이 6이 아니라 3이 나옴..
'''