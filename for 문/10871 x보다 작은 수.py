'''
정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.
X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.
'''
n,x=map(int,input().split()) #n,x를 빈칸을 기준으로 정수형 자료형으로 입력값을 받음.
a=list(map(int,input().split())) #수열을 입력하고, x와 비교하기 위해 a라는 list를 만들었다.

if len(a) == n:  #수열의 개수가 앞에서 입력한 n과 개수가 같으면 if 조건문 실행
    for i in a: 
        if i<x:  #x보다 작은 수를 판별하기 위해 for반복문을 사용해서 i에 차례대로 들어가는 a와 x를 비교
            print(i,end=' ') #한 줄에 출력하기 위해 end를 사용해서 한칸씩 띄어 출력.

'''
sep, end 인수
sep='' : 각 연결 사이 구분자를 정의
end='' : 각 출력 끝에 삽입되는 구분자를 변경하는 기능 

'''

# 다른 사람
count,num = map(int,input().split())
inArr = list(map(int,input().split()))
for i in range(count):
    if inArr[i]<num:
        print(inArr[i],end=" ")