'''
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.
'''

t=int(input())
for i in range(1,t+1):
    a,b=map(int,input().split())
    print("Case #"+str(i)+':',a+b)

#다른 사람
cases=int(input())
for i in range(cases):
    a,b=map(int(),input().split())
    ans= a+b
    print("Case #%s: %s"%(i+1,ans))

#% 사용법
print("%s %s" % ('one','two'))
#첫번째 s에는 뒤에 %()로 연결된 첫번째 단어가 오고
#두번째 s에는 뒤에 %()로 연결된 두번째 단어
# %s: s는 문자열이 와야한다는 지정

#format 사용법
print('{} {}'.format('one','two'))