'''
알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
'''
#문자열 입력
s = list(map(str,input()))

#알파벳 리스트
alpha=list('abcdefghijklmnopqrstuvwxyz')

#알파벳 길이만큼 array에 -1
array=[-1 for i in range(len(alpha))]

for i in range(len(s)):
    #알파벳 리스트의 인덱스와 문자열 인덱스가 같으면 i
    if array[alpha.index(s[i])] == -1:
        array[alpha.index(s[i])] == i
for j in array:
    print(j,end=" ")