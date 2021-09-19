total=int(input("시간의 전체 초 입력: "))
min= total//60
sec= total % 60
print('%d 초 : %d 분 %d 초' % (total,min, sec))