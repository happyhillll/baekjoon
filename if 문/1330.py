'''
두 정수 a와 b가 주어졌을 때, a와 b를 비교하는 프로그램을 작성하시오.

1. a가 b보다 크면 >
2. a가 b보다 작으면 <
3. a와 b가 같은 경우에는 ==
'''
a,b=map(int,input().split())

if a>b:
    print(">")
elif a<b:
    print("<")
else: 
    print("==")