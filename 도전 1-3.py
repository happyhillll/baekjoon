attend=100
homework=100
mid=100
final=100

attend = attend *0.1
homework = homework*0.3
mid = mid*0.3
final = final*0.3
print("total",attend+homework+mid+final)

#다른 방법
total = attend*0.1
total += homework*0.3
total += mid*0.3
total += final*0.3
print("total %d" % total)