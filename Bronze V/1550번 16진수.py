a=input()
six=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
for i in range(5):
    if a in six:
        print(six.find(a),end='')
    else:
        print(a,end='')

#에반데 한줄이면 풀림
print(int(input(),16))

#16진수 수를 받아서, 10진수 int로 변환해서 출력하기