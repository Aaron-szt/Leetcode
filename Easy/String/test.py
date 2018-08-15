s = [1,2,3,4,5,6,7,8,9,0]
l = 0
i = 0
while i < len(s):
	for j in range(i, len(s)):
		print("i=",i," j=",j)
		l += 1
		if j == 5:
			i += 1
	i += 1
print(l)