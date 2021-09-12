#첫째 줄에 테스트 케이스의 개수 T가 주어진다.
#각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
#각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.

t=int(input())
for i in range(1,t+1):
    a,b=map(int,input().split()) #a,b의 입력값을 map함수로 묶어 빈칸을 기준으로 a,b구별하여 int자료형으로
    0<a and b<10
    ans=a+b
    print("Case #"+str(i)+':',str(a),'+',str(b),'=',ans)

# +를 사용하여 변수의 값들을 붙여서 출력, 띄어서 쓰인 부분은 콤마(,)
# 같은 자료형끼리만 가능하기 때문에 str(문자형)으로 바꾸기

#다른 답
case = int(input())
for i in range(case):
    a,b= map(int,input().split())
    print('Case #%d: %d + %d = %d'%(i+1,a,b,a+b))
    