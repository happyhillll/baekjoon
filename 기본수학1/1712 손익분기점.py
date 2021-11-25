#a만원의 고정비용, b만원의 가변 비용, c는 책정된 노트북 가격
a,b,c=map(int,input().split())
if b>=c:
    print(-1)
else:
    print(int(a/(c-b)+1))