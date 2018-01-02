def makes10(a,b):
	if a==10 or b==10:
		return True
	if (a+b)==10:
		return True
	else:
		return False
	

print(makes10(10,9))
print(makes10(1,9))
print(makes10(11,9))
print(makes10(-2,11))
