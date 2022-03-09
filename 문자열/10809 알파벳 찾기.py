'''
알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
'''
#1트
#문자열 입력
s = list(map(str,input()))
#알파벳 리스트
alpha=list('abcdefghijklmnopqrstuvwxyz')

dictionary={string:i for i,string in enumerate(alpha)}
print(dictionary)

for i in range(len(alpha)):
    if alpha[i] not in s:
        print(-1,end=" ")
    elif alpha[i] in s:
        print(i,end=" ")


#2트
s=input()
alpha='abcdefghijklmnopqrstuvwxyz'

for i in alpha:
    if i in s:
        print(s.index(i),end=' ')
    else:
        print(-1,end= " ")