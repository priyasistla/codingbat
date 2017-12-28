def diff21(n):
	diff = abs(n-21)
	if n > 21:
		diff *= 2
	return diff
	

def diff21_2(n):
	if n < 21:
		return 21 - n
	else:
		return 2 * (n-21)
	
print(diff21(19))
print(diff21(29))
print(diff21(21))
