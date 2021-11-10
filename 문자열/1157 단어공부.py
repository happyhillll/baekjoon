word=input().lower() #lower()를 이용해서 소문자로만 입력받음 baaa
word_list= list(set(word)) #set()으로 자료형의 중복 제거한 뒤 list()로 리스트 묶기 ['b','a']
cnt=[] #cnt변수를 리스트로 초기화

for i in word_list:  #i=b,a
    count=word.count(i) #i가 몇번 count 되었는지 
    cnt.append(count) #cnt=[1,3] cnt변수에 append

if cnt.count(max(cnt)) >= 2: #만약 cnt변수 리스트에 가장 큰 값 max(cnt)를 count() 함수를 이용해서 센 개수가 2개 이상이라면, 여러개이기 때문에 ?출력
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))].upper()) #나머지의 경우, 가장 많이 사용된 알파벳을 인덱스에서 설정하여 upper로 출력한다.