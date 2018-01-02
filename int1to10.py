 def int1to10(n,outside_mode):
	if outside_mode:
		return True
	elif n>0 and n<=10:
		return True
	else:
		return False

print(in1to10(5, False))
print(in1to10(11, False))
print(in1to10(11, True))
