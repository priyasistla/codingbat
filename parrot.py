def parrot_trouble(talking,hour):
	if hour<7 or hour>20:
		if talking:
			return True
		else:
			return False
	else:
		return False
print(parrot_trouble(True,12))
print(parrot_trouble(True,22))
print(parrot_trouble(False,5))
print(parrot_trouble(True,6))
