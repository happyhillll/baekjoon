a=int(input("a 입력 :"))
b=int(input("b 입력 :"))

# 방법1
num1=b%100%10
num2=b%100//10
num3=b//100

print(a*num1)
print(a*num2)
print(a*num3)
print(a*b)