a=list(map(int,input().split()))
if a == [1,2,3,4,5,6,7,8]:
    print("ascending")
elif a == [8,7,6,5,4,3,2,1]:
    print("descending")
else:
    print("mixed")
    
#다른 풀이 : sorted 사용
a=list(map(int,input().split()))
if a == sorted(a):
    print("ascending")
elif a== sorted(a, reverse=True):
    print("descending")
else:
    print("descending")
    
    
#다른 풀이
n = list(map(int, input().split()))
result = [1, 2, 3, 4, 5, 6, 7, 8]
 
if n == result:
    print('ascending')
elif n == result[::-1]:
    print('descending')
else:
    print('mixed')