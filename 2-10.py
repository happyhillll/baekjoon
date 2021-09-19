n=396
print(n)
d100=n//100 #백의 자리
n=n%100

d10=n//10
n=n%10
d1=n/1

print("백의 자리",d100)
print("십의 자리",d10)
print("일의 자리",d1)
