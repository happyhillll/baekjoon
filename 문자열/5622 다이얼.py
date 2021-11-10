#다이얼 넘버
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
#알파벳 입력
a = input()
#걸리는 시간
ret = 0

for j in range(len(a)):
    for i in dial:
        #만약에 입력받은 값이 dial에 있으면 ret에서 3초를 더해준다.
        if a[j] in i:
            ret += dial.index(i)+3
print(ret)