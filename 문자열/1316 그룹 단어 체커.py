# 그룹 단어 찾아서 개수 출력 문제
N = int(input())
result = N
for i in range(0,N):
    word=input()
    for j in range(0,len(word)-1): #인덱스 범위 생성: 0부터 단어개수 -1까지
        if word[j]==word[j+1]: #연달은 두 문자가 다를때,
            pass # 현재 글자 이후 문자열을 새로운 단어로 생성
        elif word[j] in word[j+1:]: 
            result-=1
            break
print(result)
