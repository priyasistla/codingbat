def pos_neg(a,b,negative):
	if a<0 and b<0:
		if negative:
			return True
		else:
			return False
	if (a<0 and b>0) or (a>0 and b<0):
		return True
	else:
		return False

print(pos_neg(1,-1,False))
print(pos_neg(-1,1,False))
print(pos_neg(-1,-1,True))
print(pos_neg(-1,-1,False))