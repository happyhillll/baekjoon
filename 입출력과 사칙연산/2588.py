a=int(input())
b=int(input())

# 방법1
num1=b%10 
num2=b%100//10
num3=b//100
'''
//(몫), %(나머지)
b의 일의 자리 수 : b%10 -> 10으로 나눈 나머지
b의 십의 자리 수 : b%100//10 -> 100으로 나눈 나머지를 10으로 나눈 몫
b의 백의 자리 수 : b//100 -> 100으로 나눈 몫
'''
print(a*num1)
print(a*num2)
print(a*num3)
print(a*b)