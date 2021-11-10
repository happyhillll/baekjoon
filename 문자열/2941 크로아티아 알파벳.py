a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
b = input()
for i in a:
    b = b.replace(i, 'a')
print(len(b))

'''
cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()
cnt = 0
for c in cro:
    if(c in word):
        cnt += 1
        wo = word.split(c)
        word = ''
        for a in wo:
            word += a
cnt += len(word)
print(cnt)
word = input()
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
for i in range(len(cro)):
    cnt += word.count(cro[i])
print(len(word)-cnt)
'''

'''
croa = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()
count = len(word)
for i in range(0, len(word)-1):
	for j in croa:
		if i > 0:
			if word[i-1] + word[i] + word[i+1] == "dz=":
				count -= 2
				i += 1
				if i >= len(word)-1:
					break
				pass
			if word[i] + word[i+1] == j:
				count -= 1
		else:
			if word[i] + word[i+1] == j:
				count -= 1
print(count)	
'''