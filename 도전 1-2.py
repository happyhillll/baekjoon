time = 3700
print(time,"초")

minute = time//60
second = time%60

hour = minute//60
minute = minute%60

print('%d 시간' %hour)
print('%d 분' %minute)
print('%d 초' %second)